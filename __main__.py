import arcade
import os
from random import randint
from ground import Ground
from obstacle import Obstacle

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
        self.obstacle_list = None
    
    def setup(self):
        #initialization score
        self.score = 0

        #player initialization
        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite("Data" + os.sep + "Assets" + os.sep + "Sprites" + os.sep + "player.png")
        self.player.center_x = 250
        self.player.center_y = 270
        self.player.scale = 0.6

        self.player_list.append(self.player)

        #ground initialization from Ground class
        self.ground_list = arcade.SpriteList()

        #boucle that uses Ground class to generate the three parts of the ground, incrementing the state each time to get the right.
        for i in ground.current_ground:
            start_ground = ground.draw_ground()
            self.ground_list.append(start_ground)
            ground.state += 1
            if ground.state > 2:
                ground.state = 0

        self.obstacle_list = arcade.SpriteList()

        start_obstacle = Obstacle.draw_obstacle(750,270)

        self.obstacle_list.append(start_obstacle)

        #physics engine initialization
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list, gravity_constant=0.45)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = 12
        
    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        arcade.start_render()
        #draw things here
        self.player_list.draw()
        self.ground_list.draw()
        self.obstacle_list.draw()

    def on_update(self, delta_time):
        self.obstacle_list.update()
        self.physics_engine.update()
        for item in self.ground_list:
            item.center_x -= SCROLLING_SPEED
            if item.right <= 0:
                item.center_x = item.width // 2 + SCREEN_WIDTH * 2
        for item in self.obstacle_list:
            if item.right <= 0:
                item.kill()
                new_obstacle = Obstacle.draw_obstacle(750,270)
                self.obstacle_list.append(new_obstacle)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
        main()
