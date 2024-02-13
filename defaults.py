from dataclasses import dataclass, field, fields


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
    """Getting called during App.__init__() and other Node's use updated values during init"""
    global WIDTH_RATIO, HEIGHT_RATIO
    WIDTH_RATIO = width / 1920
    HEIGHT_RATIO = height / 1080
