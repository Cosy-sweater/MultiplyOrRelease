import pygame
from common import Node


class App(Node):
    def __init__(self, window_size=(640, 480), window_flags=tuple()) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(window_size, *window_flags)
        super().__init__()

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        pass

    def draw(self, surface: pygame.Surface):
        pass

    def run(self):
        pass
