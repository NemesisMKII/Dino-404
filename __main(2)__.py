import arcade
from random import randint

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "ARK 404"
SCROLLING_SPEED = 10

GAME_MENU = 0
GAME_RUNNING = 1
GAME_OVER = 2

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #initialisation engine
        self.physics_engine = None

        self.player_list = None
    
    def setup(self):
        #initialization score
        self.score = 0

        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite("charac.png")
    
    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        arcade.start_render()
        #draw things here
    def on_update(self, delta_tiem):
        pass

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
        main()
