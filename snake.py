import arcade


class Snake(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.score = 0
        self.movement = 2
        self.direction = None

    def eat_food(self, food):  # Para cuando la comida se coma se añade un punto al score
        if self.collides_with_sprite(food):
            self.score += 1
            return True
        return False

    # Para definir los margenes del tablero en los cuales la serpiente puede colisionar
    def wall_collision(self, width, height):
        if self.center_x <= 0 or self.center_x >= width or self.center_y <= 0 or self.center_y >= height:
            return True
        return False

    def collision_tail(self, tails):  # Para verificar si colisiona con la cola la spiente
        for i in range(3, len(tails)-1, +1):
            if self.collides_with_sprite(tails[i]):
                return True
        return False

    def move(self):  # Establecer el movimiento de la serpiente

        if arcade.key.UP == self.direction:
            if self.center_x % 20 != 10:
                self.center_x += (10 - self.center_x % 20)
                return True
            self.center_y += self.movement
        elif arcade.key.DOWN == self.direction:
            if self.center_x % 20 != 10:
                self.center_x += (10-self.center_x % 20)
                return True
            self.center_y -= self.movement
        elif arcade.key.LEFT == self.direction:
            if self.center_y % 20 != 10:
                self.center_y += (10-self.center_y % 20)
                return True
            self.center_x -= self.movement
        elif arcade.key.RIGHT == self.direction:
            if self.center_y % 20 != 10:
                self.center_y += (10-self.center_y % 20)
                return True
            self.center_x += self.movement

    def update(self):
        self.move()
