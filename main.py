import logging

from app import App
from common import Scene

logging.basicConfig(filename='logs.log', filemode='w', format='%(levelname)s %(filename)s -> %(message)s at line %('
                                                              'lineno)d')

application = App()

empty_scene = Scene("empty_scene", (0, 0), (200, 200))
empty_scene2 = Scene("empty_scene2", (50, 50), (100, 100))
empty_scene.add_child_nodes([empty_scene2])
application.add_child_nodes([empty_scene])

application.run()
