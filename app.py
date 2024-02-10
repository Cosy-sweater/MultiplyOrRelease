import pygame
from common import Node, ConfigLoader


class App(Node):
    def __init__(self, window_size=(640, 480), window_flags=tuple(), framerate: int = 90) -> None:
        from common import ConfigLoader
        pygame.init()
        self.screen = pygame.display.set_mode(window_size, *window_flags)
        self.framerate = framerate
        super().__init__()

        self._config = ConfigLoader()

    def run(self):
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
