import pygame

from common import Node
import defaults


class Text(Node):
    def __init__(self, text: str = "", pos: (int, int) = (0, 0), font: str | pygame.font.Font = None,
                 font_size: int = 16,
                 font_color: (int, int, int) = (0, 0, 0), anchor="topleft", **other):
        from scripts import get_default_font
        super().__init__()
        self.text = text
        if font is None:
            self.font = get_default_font(font_size)
        else:
            self.font = font if type(font) is pygame.font.Font else pygame.font.SysFont(font, font_size)
        self.font_size = font_size if font_size else 24
        self.font_color = font_color
        self.pos = pos
        self.anchor = anchor

        self.text_surface = None
        self.rect = None
        self.update_object()

    def update_object(self):
        self.text_surface = self.font.render(self.text, False, self.font_color)
        self.rect = self.text_surface.get_rect()
        exec(f"self.rect.{self.anchor} = self.pos")

    def draw(self, surface) -> None:
        surface.blit(self.text_surface, self.rect)


class FlexibleText(Node):
    def __init__(self, text: str = "", pos: (int, int) = (0, 0), font: str | pygame.font.Font = None,
                 font_size: int = 16, font_color: (int, int, int) = (0, 0, 0),
                 max_width: int | None = None, x_spacing: int = 20, y_spacing: int = 20) -> None:
        super().__init__()
        text = text.replace("\t", "    ").split(" ")
        text_height = font_size * 96 / 72 * defaults.HEIGHT_RATIO
        y = 0
        x = 0
        for subsring in text:
            new_obj = Text(subsring, (pos[0] + x, pos[1] + y), font, font_size, font_color)
            if new_obj.rect.right > max_width:
                y += (text_height + y_spacing) * defaults.HEIGHT_RATIO
                x = 0
                new_obj = Text(subsring, (pos[0] + x, pos[1] + y), font, font_size, font_color)

            x = new_obj.rect.right + x_spacing * defaults.WIDTH_RATIO

            self.child_nodes.append(new_obj)
