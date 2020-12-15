import arcade

class Ground(arcade.Sprite):

    def __init__(self, filename=None, scale=1, image_x=0, image_y=0, image_width=0, image_height=0, center_x=0, center_y=0, repeat_count_x=1, repeat_count_y=1):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y)

        self.state = 0
        self.current_ground = ["Background/ground_1.png","Background/ground_2.png","Background/ground_3.png"]

        self.speed = 10
        
    def draw_ground(self):
        #ground initialization
        self.ground = arcade.Sprite(self.current_ground[self.state])
        self.ground.center_x = self.ground.width // 2
        self.ground.center_y = self.ground.height // 2

        return self.ground

    def update(self):
        self.ground.center_x -= self.speed