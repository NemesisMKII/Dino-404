import arcade
import __main__
import os

class Ground(arcade.Sprite):

    def __init__(self, filename=None, scale=1, image_x=0, image_y=0, image_width=0, image_height=0, center_x=0, center_y=0, repeat_count_x=1, repeat_count_y=1):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y)

        self.state = 0
        self.current_ground = ["Data" + os.sep + "Assets" + os.sep + "Background" + os.sep + "ground_1.png",
                               "Data" + os.sep + "Assets" + os.sep + "Background" + os.sep + "ground_2.png", 
                               "Data" + os.sep + "Assets" + os.sep + "Background" + os.sep + "ground_3.png"]
        self.speed = -10
        
    def draw_ground(self):
        #function that draw ground using self.state to get the right ground part.It returns a sprite.
        if self.state == 0:
            self.ground = arcade.Sprite(self.current_ground[self.state])
            self.ground.center_x = self.ground.width // 2 
            self.ground.center_y = self.ground.height // 2

        if self.state == 1:
            self.ground = arcade.Sprite(self.current_ground[self.state])
            self.ground.center_x = self.ground.width // 2 + 1280
            self.ground.center_y = self.ground.height // 2

        if self.state == 2:
            self.ground = arcade.Sprite(self.current_ground[self.state])
            self.ground.center_x = self.ground.width // 2 + 2560
            self.ground.center_y = self.ground.height // 2

        return self.ground

    def update(self):
        self.center_x += self.speed
