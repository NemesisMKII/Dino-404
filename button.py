import arcade
import os

class Button():

    def __init__(self, filename=None, scale=0.6, image_x=0, image_y=0, image_width=0, image_height=0, center_x=0, center_y=0, repeat_count_x=1, repeat_count_y=1):
        super().__init__(filename=filename, scale=scale, image_x=start_x, image_y=start_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y)

        self.pressed = False
        self.color = arcade.color.BLACK
        
    @classmethod
    def draw_button(cls,text,start_x,start_y):

        button = arcade.draw_text(text,start_x,start_y,color=cls)
        button.start_x = start_x
        button.start_y = start_y
        button.font_size = 48
        button.anchor_x = "center"
        button.anchor_y = "center"

        return button 

    

