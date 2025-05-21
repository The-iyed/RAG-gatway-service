import yaml
import os
from pathlib import Path
from typing import Dict, Optional
import re

class Config:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.topics: Dict[str, Dict[str, str]] = {}
        self.default_agent: Optional[str] = None
        self.load_config()

    def _substitute_env_vars(self, value: str) -> str:
        """Substitute environment variables in a string."""
        def replace_var(match):
            var_name = match.group(1)
            return os.getenv(var_name, match.group(0))
        
        return re.sub(r'\${([^}]+)}', replace_var, value)

    def load_config(self) -> None:
        """Load configuration from YAML file."""
        config_path = Path(self.config_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # Process topics and substitute environment variables
        self.topics = {}
        for topic, topic_config in config.get('topics', {}).items():
            self.topics[topic] = {
                'route': self._substitute_env_vars(topic_config['route'])
            }

        self.default_agent = self._substitute_env_vars(config.get('default_agent'))

        if not self.default_agent:
            raise ValueError("Default agent URL not specified in configuration")

    def get_agent_url(self, topic: str) -> str:
        """Get the agent URL for a given topic."""
        if topic in self.topics:
            return self.topics[topic]['route']
        return self.default_agent 