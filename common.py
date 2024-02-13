import logging
import typing

import pygame

import scripts
from defaults import *


class Node:
    """Main game object. Only child objects of Node are meant to be used inside application"""
    node_id = 0
    node_list = []

    def __init__(self, node_name: str = None) -> None:
        if node_name:
            for name in map(Node.get_name, self.node_list):
                if node_name == name:
                    logging.warning(f"Created Node with duplicate name {node_name}")
                    break
            self.name = node_name
        else:
            self.name = self.get_new_node_name()
        self.node_list.append(self)

        self.child_nodes: list[Node] = []

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        for node in self.child_nodes:
            node.update(deltatime, events, dynamic_info)

    def draw(self, surface: pygame.Surface) -> None:
        for node in self.child_nodes:
            node.draw(surface)

    def get_new_node_name(self) -> str:
        self.node_id += 1
        new_name = self.__class__.__name__ + str(self.node_id)
        return new_name

    def add_child_nodes(self, nodes: typing.Iterable["Node"]):
        self.child_nodes.extend(nodes)

    def get_name(self) -> str:
        return self.name


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
                    valid_config_data = {key: config_data[key] for key in config_data if
                                         key in AppConfig.__annotations__}
                    self._config = AppConfig(**valid_config_data)
            except FileNotFoundError:
                scripts.create_default_config()
                return self.load_config()
        return self._config


class Scene(Node):
    """Child class of Node class. Meant to be used as big Node container"""

    def __init__(self, scene_name: str = None, position: tuple[int, int] = (0, 0), size: tuple[int, int] = (100, 100)):
        super().__init__(scene_name)
        self.focused = False

        self.scene_rect = pygame.Rect(position, size)

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        if not self.focused:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.scene_rect.collidepoint(pygame.mouse.get_pos()):
                        self.unfocus_all_scenes()
                        self.focused = True
                        super().update(deltatime, events, dynamic_info)
                        break
        else:
            super().update(deltatime, events, dynamic_info)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (77, 77, 77), self.scene_rect)
        pygame.draw.rect(surface, (44, 44, 44), self.scene_rect, 4)
        super().draw(surface)

    @classmethod
    def unfocus_all_scenes(cls):
        for node in cls.node_list:
            node.focused = False
