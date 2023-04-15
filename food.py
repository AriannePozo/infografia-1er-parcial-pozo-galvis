import arcade


class Food(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
