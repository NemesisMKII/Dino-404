import arcade
from random import randint
from ground import Ground

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "ARK 404"
SCROLLING_SPEED = 10

GAME_MENU = 0
GAME_RUNNING = 1
GAME_OVER = 2

ground = Ground()

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #initialisation engine
        self.physics_engine = None

        self.player_list = None
        self.ground_list = None
    
    def setup(self):
        #initialization score
        self.score = 0

        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite("charac.png")
        self.player.center_x = 500
        self.player.center_y = 278
        self.player.scale = 0.6

        self.player_list.append(self.player)

        self.ground_list = arcade.SpriteList()
        
        self.ground = ground.draw_ground()

        self.ground_list.append(self.ground)
    
    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        arcade.start_render()
        #draw things here
        self.player_list.draw()
        self.ground_list.draw()

    def on_update(self, delta_time):
        for item in self.ground_list:
            item.center_x -= SCROLLING_SPEED
            if item.center_x + item.width // 2 <= 0:
                item.kill()
                new_ground = ground.draw_ground()
                self.ground_list.append(new_ground)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
        main()
