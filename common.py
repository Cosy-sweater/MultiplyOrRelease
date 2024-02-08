import pygame


class Node:
    def __init__(self) -> None:
        self.child_nodes: list[Node] = []

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        pass

    def draw(self, surface: pygame.Surface):
        pass


class ConfigLoader:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        else:
            return cls.__init__(*args, **kwargs)

    def __init__(self, *_, **__):
        pass
