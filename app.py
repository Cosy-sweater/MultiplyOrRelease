import logging

import pygame
from common import Node, ConfigLoader


class App(Node):
    def __init__(self, window_size=(640, 480), window_flags=tuple(), framerate: int = 90) -> None:
        from common import ConfigLoader
        import defaults
        pygame.init()
        self.screen = pygame.display.set_mode(window_size, *window_flags)
        self.framerate = framerate
        super().__init__()

        self._config = ConfigLoader()
        defaults.calculate_ratio(*self.screen.get_size())

    def run(self):
        logging.info("Starting app")
        clock = pygame.time.Clock()
        game_loop = True
        dt = 0

        while game_loop:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_loop = False
            self.update(dt, events, {})
            pygame.display.flip()
            self.draw(self.screen)
            dt = clock.tick(self.framerate)

    def update(self, deltatime: int, events: list[pygame.event], dynamic_info: dict) -> None:
        for node in self.child_nodes:
            node.update(deltatime, events, dynamic_info)

    def draw(self, surface: pygame.Surface) -> None:
        for node in self.child_nodes:
            node.draw(surface)
