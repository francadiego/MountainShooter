import pygame as pg

from app.Const import WIN_HEIGHT, WIN_WIDTH
from app.Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

