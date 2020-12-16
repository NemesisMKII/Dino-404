import arcade
import time
from random import randint
import os

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
        #engine initialization
        self.physics_engine = None
        self.current_state = GAME_MENU
        
        self.button_text_color = None

    def setup(self):
        self.score = 0
        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite("charac.png")
        self.player.scale = 0.6
        self.player.center_x = 200
        self.player.center_y = 268

        self.player_list.append(self.player)
        #ground 1
        self.ground_list = arcade.SpriteList()

        self.ground = arcade.Sprite("Background/ground_1.png")
        self.ground.center_x = 640
        self.ground.center_y = 360

        self.ground_list.append(self.ground)

        #ground 2
        self.ground_2 = arcade.Sprite("Background/ground_2.png")
        self.ground_2.center_x = SCREEN_WIDTH + 640
        self.ground_2.center_y = 360

        self.ground_list.append(self.ground_2)

        #ground 3
        self.ground_3 = arcade.Sprite("Background/ground_3.png")
        self.ground_3.center_x = 2*SCREEN_WIDTH + 640
        self.ground_3.center_y = 360

        self.ground_list.append(self.ground_3)

        #obstacles
        self.obstacle_list = arcade.SpriteList()

        self.obstacle = arcade.Sprite("Obstacle/obstacle.png")
        self.obstacle.scale = 0.6
        self.obstacle.center_x = 880
        self.obstacle.center_y = 272
        
        self.obstacle_list.append(self.obstacle)

        #start button
        self.startbtn_color = arcade.color.BLACK
        #exit button
        self.exitbtn_color = arcade.color.BLACK    
        #retry button
        self.retrybtn_color = arcade.color.BLACK
        #back to menu button
        self.backmenubtn_color = arcade.color.BLACK
        #physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list, gravity_constant=0.45)

    def draw_start_btn(self):
        self.start_button = arcade.draw_text(text="Nouvelle partie",start_x=20, start_y=175,bold=True,font_size=18,color=self.startbtn_color,anchor_x="left",anchor_y="center")
        self.start_button.draw()

    def draw_exit_btn(self):
        self.exit_button = arcade.draw_text(text="Quitter",start_x=20, start_y=145,color=self.exitbtn_color,bold=True,font_size=18,anchor_x="left",anchor_y="center")  
        self.exit_button.draw()

    def draw_game_menu(self):
        self.ground_list.draw()
        self.obstacle_list.draw()
        arcade.draw_text(text="DINO",start_x=640,start_y=640,color=arcade.color.RED,bold=True,font_size=46,anchor_x="center",anchor_y="center")
        arcade.draw_text(text="404",start_x=640,start_y=595,color=arcade.color.RED,bold=True,font_size=46,anchor_x="center",anchor_y="center")
        self.draw_start_btn()
        self.draw_exit_btn()

    def draw_game(self):
        self.ground_list.draw()
        for obstacle in self.obstacle_list:
            obstacle.draw()
        self.player_list.draw()
        if self.current_state == GAME_RUNNING:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 640, 680, arcade.color.WHITE, 28,anchor_x="center",anchor_y="center")

    def draw_selection(self):
        pass
    def draw_retry_btn(self):
        self.retry_button = arcade.draw_text(text="Réessayer",start_x=SCREEN_WIDTH//2,start_y=SCREEN_HEIGHT//2,color=self.retrybtn_color,bold=True,font_size=18,anchor_x="center",anchor_y="center")
        self.retry_button.draw()

    def draw_backtomenu_btn(self):
        self.backtomenu_button = arcade.draw_text(text="Retour au menu principal",start_x=SCREEN_WIDTH//2,start_y=SCREEN_HEIGHT//2 - 50,color=self.backmenubtn_color,bold=True,font_size=18,anchor_x="center",anchor_y="center")
        self.backtomenu_button.draw()
        
    def draw_game_over(self):
        arcade.draw_text(text="GAME OVER",start_x=640,start_y=560, color=arcade.color.WHITE,font_size=42,anchor_x="center",anchor_y="center")
        self.draw_retry_btn()
        self.draw_backtomenu_btn()
        final_output = f"Score final: {self.score}"
        arcade.draw_text(final_output,640, 460,arcade.color.WHITE, 28,anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = 12
        if key == arcade.key.ENTER:
            if self.current_state == GAME_MENU:
                self.setup()
                self.current_state = GAME_RUNNING
            elif self.current_state == GAME_OVER:
                self.setup()
                self.current_state = GAME_RUNNING
        if key == arcade.key.ESCAPE:
            if self.current_state == GAME_OVER:
                self.setup()
                self.current_state = GAME_MENU
            elif self.current_state == GAME_MENU:
                quit()

    def on_key_release(self,key,modifiers):
        pass 

    def on_mouse_motion(self, x, y, dx, dy):
        if self.current_state == GAME_MENU:
            if x > self.start_button.left and x < self.start_button.right and y < self.start_button.top and y > self.start_button.bottom:
                self.startbtn_color = arcade.color.BLANCHED_ALMOND
            elif x > self.exit_button.left and x < self.exit_button.right and y < self.exit_button.top and y > self.exit_button.bottom:
                self.exitbtn_color = arcade.color.BLANCHED_ALMOND
            else:
                self.startbtn_color = arcade.color.BLACK
                self.exitbtn_color = arcade.color.BLACK
        if self.current_state == GAME_OVER:
            if x > self.retry_button.left and x < self.retry_button.right and y < self.retry_button.top and y > self.retry_button.bottom:
                self.retrybtn_color = arcade.color.BLANCHED_ALMOND
            elif x > self.backtomenu_button.left and x < self.backtomenu_button.right and y < self.backtomenu_button.top and y > self.backtomenu_button.bottom:
                self.backmenubtn_color = arcade.color.BLANCHED_ALMOND
            else:
                self.retrybtn_color = arcade.color.BLACK
                self.backmenubtn_color = arcade.color.BLACK
 
    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == GAME_OVER:
            if x > self.retry_button.left and x < self.retry_button.right and y < self.retry_button.top and y > self.retry_button.bottom:
                self.setup()
                self.current_state = GAME_RUNNING
            elif x > self.backtomenu_button.left and x < self.backtomenu_button.right and y < self.backtomenu_button.top and y > self.backtomenu_button.bottom:
                self.current_state = GAME_MENU
        if self.current_state == GAME_MENU:
            if x > self.start_button.left and x < self.start_button.right and y < self.start_button.top and y > self.start_button.bottom:
                self.setup()
                self.current_state = GAME_RUNNING
            elif x > self.exit_button.left and x < self.exit_button.right and y < self.exit_button.top and y > self.exit_button.bottom:
                quit()

    
    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        arcade.start_render()
        #draw things here
        if self.current_state == GAME_RUNNING:
            self.draw_game()
        elif self.current_state == GAME_MENU:
            self.draw_game_menu()
        else:
            self.draw_game()
            self.draw_game_over()

    def on_update(self,delta_time):
        if self.current_state == GAME_MENU:
            self.ground.center_x -= SCROLLING_SPEED
            self.ground_2.center_x -= SCROLLING_SPEED
            self.ground_3.center_x -= SCROLLING_SPEED
            self.obstacle.center_x -= SCROLLING_SPEED
            if self.ground.left <= -1280:
                self.ground.center_x = 2*SCREEN_WIDTH + 640
            if self.ground_2.left <= -1280:
                self.ground_2.center_x = 2*SCREEN_WIDTH + 640
            if self.ground_3.left <= -1280:
                self.ground_3.center_x = 2*SCREEN_WIDTH + 640
            if self.obstacle.right <= 0:
                self.obstacle.center_x = 1500
        if self.current_state == GAME_RUNNING:
            self.physics_engine.update()
            self.ground.center_x -= SCROLLING_SPEED
            self.ground_2.center_x -= SCROLLING_SPEED
            self.ground_3.center_x -= SCROLLING_SPEED
            self.obstacle.center_x -= SCROLLING_SPEED
            for obstacle in self.obstacle_list:
                if self.player.center_x == obstacle.center_x:
                    self.score += 1
                if obstacle.right <= 0:
                    obstacle.center_x = randint(1280,3840)
            if self.ground.left <= -1280:
                self.ground.center_x = 2*SCREEN_WIDTH + 640
            if self.ground_2.left <= -1280:
                self.ground_2.center_x = 2*SCREEN_WIDTH + 640
            if self.ground_3.left <= -1280:
                self.ground_3.center_x = 2*SCREEN_WIDTH + 640
            if arcade.check_for_collision_with_list(self.player, self.obstacle_list):
                self.current_state = GAME_OVER

        

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()