from dataclasses import dataclass, field, fields


@dataclass
class AppConfig:
    from typing import Any
    field1: Any = field(default=0)

    def __str__(self):
        field_strings = [f"{f.name}={getattr(self, f.name)!r}" for f in fields(self)]
        return f"{self.__class__.__name__}({', '.join(field_strings)})"