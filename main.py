import logging

from app import App
from common import Scene, Node
from GUI import FlexibleText

logging.basicConfig(filename='logs.log', filemode='w', format='%(levelname)s %(filename)s -> %(message)s at line %('
                                                              'lineno)d')

application = App()

empty_scene = Scene("empty_scene", (100, 0), (200, 200))
flex_text_test = FlexibleText("123 123 123 123 123 123 123 123 123 123 123 123 123 123 123 123 13", font_size=32, font_color=(255, 255, 255), max_width=123)
empty_scene.add_child_nodes([flex_text_test])
application.add_child_nodes([empty_scene])

# print(list(map(Node.get_name, Node.node_list)))

application.run()
