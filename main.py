import logging

from app import App

logging.basicConfig(filename='logs.log', filemode='w', format='%(filename)s -> %(message)s at line %(lineno)d')

application = App()
application.run()