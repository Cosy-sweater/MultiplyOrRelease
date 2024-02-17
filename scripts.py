import sys
import os

import pygame.font


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def create_default_config():
    from dataclasses import asdict
    import tomli_w
    from defaults import AppConfig

    with open(resource_path("app_config.toml"), "w") as f:
        f.write(tomli_w.dumps(asdict(AppConfig())))


def get_default_font(font_size: int) -> pygame.font.Font:
    import defaults
    return pygame.font.Font(open(defaults.DEFAULT_FONT_PATH),
                            int(font_size * defaults.HEIGHT_RATIO * defaults.FONT_MULTIPLYER))