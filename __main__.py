import arcade
import os
from random import randint
from ground import Ground
from obstacle import Obstacle
from button import Button

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
        self.menu_button_list = None


        self.game_state = GAME_MENU
    
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
        start_obstacle_2 = Obstacle.draw_obstacle(1500,270)

        self.obstacle_list.append(start_obstacle)
        self.obstacle_list.append(start_obstacle_2)

        self.menu_button_list = arcade.SpriteList()

        self.start_button = Button.draw_button("start",640,360)

        self.menu_button_list.append(self.start_button)

        #physics engine initialization
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list, gravity_constant=0.45)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = 12
        if key == arcade.key.SPACE:
            if self.game_state == GAME_MENU:
                self.setup()
                self.game_state = GAME_RUNNING
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state == GAME_MENU:
            if x > self.start_button.left and x < self.start_button.right and y > self.start_button.bottom and y < self.start_button.top:
                self.setup()
                self.game_state = GAME_RUNNING 
        
    def on_mouse_motion(self, x, y, button, modifiers):
        for item in self.menu_button_list:
            if x > item.left and x < item.right and y > item.bottom and y < item.top:
                item.color = arcade.color.WHITE

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        arcade.start_render()
        #draw things here
        if self.game_state == GAME_RUNNING:
            self.player_list.draw()
            self.ground_list.draw()
            self.obstacle_list.draw()
            output = f"Score: {self.score}"
            arcade.draw_text(output, 640, 680, arcade.color.WHITE, 28,anchor_x="center",anchor_y="center")
        elif self.game_state == GAME_MENU:
            self.ground_list.draw()
            self.obstacle_list.draw()
            self.menu_button_list.draw()
        elif self.game_state == GAME_OVER:
            pass

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
                new_obstacle = Obstacle.draw_obstacle(randint(SCREEN_WIDTH,SCREEN_WIDTH * 2.5),270)
                self.obstacle_list.append(new_obstacle)
            if self.player.center_x >= item.center_x and item.jumped == False:
                self.score += 1
                item.jumped = True
        if self.game_state == GAME_RUNNING:
            if arcade.check_for_collision_with_list(self.player, self.obstacle_list):
                quit()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
        main()
