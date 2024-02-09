import pygame

import scripts
from defaults import *


class Node:
    def __init__(self) -> None:
        self.child_nodes: list[Node] = []

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        pass

    def draw(self, surface: pygame.Surface):
        pass


class ConfigLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = None
        return cls._instance.load_config()

    def load_config(self) -> AppConfig:
        import tomli
        import logging
        if self._config is None:
            try:
                with open('app_config.toml', 'rb') as f:
                    config_data = tomli.load(f)
                    undefined_fields = [key for key in config_data if key not in AppConfig.__annotations__]
                    if undefined_fields:
                        logging.warning("Найдены неопределенные поля в конфигурации: %s", undefined_fields)
                    valid_config_data = {key: config_data[key] for key in config_data if key in AppConfig.__annotations__}
                    self._config = AppConfig(**valid_config_data)
            except FileNotFoundError:
                scripts.create_default_config()
                return self.load_config()
        return self._config