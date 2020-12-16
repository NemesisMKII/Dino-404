import arcade
import os

obstacle = "Data" + os.sep + "Assets" + os.sep + "Sprites" + os.sep + "enemy.png"

class Obstacle(arcade.Sprite):

    def __init__(self, filename=None, scale=0.6, image_x=0, image_y=0, image_width=0, image_height=0, center_x=0, center_y=0, repeat_count_x=1, repeat_count_y=1):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y)

        #class initialization
        self.speed = -10

        #initialization for score condition: if player jump over the obstacle, then he scores a point.
        self.jumped = False

    @classmethod
    def draw_obstacle(cls, center_x,center_y):
        #function that draw obstacle in front of the player, with a bit of randomizing in x pos, and and min gap between each obstacle in order to prevent obstacles to be over other ones.

        obstcle = cls(obstacle)
        obstcle.center_x = center_x
        obstcle.center_y = center_y
        obstcle.scale = 0.60

        return obstcle

    def update(self):
        self.center_x += self.speed 
        