from dataclasses import dataclass, field, fields

from scripts import resource_path


@dataclass
class AppConfig:
    from typing import Any
    field1: Any = field(default=0)

    def __str__(self) -> str:
        field_strings = [f"{f.name}={getattr(self, f.name)!r}" for f in fields(self)]
        return f"{self.__class__.__name__}({', '.join(field_strings)})"


WIDTH_RATIO: float = 1.0
HEIGHT_RATIO: float = 1.0


def calculate_ratio(width: int, height: int) -> None:
    """Getting called during App.__init__() and being used by other Nodes init"""
    global WIDTH_RATIO, HEIGHT_RATIO
    WIDTH_RATIO = width / 1920
    HEIGHT_RATIO = height / 1080


DEFAULT_FONT_PATH: str = resource_path("assets/Inconsolata.ttf")
FONT_MULTIPLYER = 3/2

