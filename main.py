
import arcade
import random
from food import Food
from snake import Snake

# definicion de constantes
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Snake"


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.FOREST_GREEN)
        self.last_key = None
        self.sprites = None
        self.snake = None
        self.snake_tail = None

    def setup(self):
        self.last_key = arcade.key.UP  # Para que inicie moviendose hacia arriba
        self.sprites = arcade.SpriteList()
        self.snake_tail = arcade.SpriteList()

        self.new_food()

        self.snake = Snake("sprites/snake2.png", 0.055, 10, 10)
        self.snake_tail.append(self.snake)
        self.sprites.append(self.snake)

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()

        # Dibujar lineas
        for v_l in range(0, SCREEN_WIDTH, 20):
            arcade.draw_line(
                v_l,
                0,
                v_l,
                SCREEN_HEIGHT,
                arcade.color.BEIGE
            )
        for h_l in range(0, SCREEN_HEIGHT, 20):
            arcade.draw_line(
                0,
                h_l,
                SCREEN_WIDTH,
                h_l,
                arcade.color.BEIGE
            )

        # Dibujar score
        arcade.draw_text(f"{self.snake.score}",
                         0,
                         SCREEN_HEIGHT-60,
                         arcade.color.FLUORESCENT_ORANGE,
                         50,
                         width=SCREEN_WIDTH,
                         bold=2,
                         align="center"
                         )
        arcade.finish_render()

    def update(self, delta_time):

        # Si es que choca con su cola o la pared aparezca la pantalla de "Game Over"
        if self.snake.wall_collision(SCREEN_WIDTH, SCREEN_HEIGHT) or self.snake.collision_tail(self.snake_tail):
            self.game_over()
            self.snake.movement = 0
        self.snake.direction = self.last_key

        # Para reiniciar el juego
        if arcade.key.SPACE == self.last_key:
            self.sprites.clear()
            self.setup()

        self.snake_eat()

        self.actualizar_cola()

        self.sprites.update()

    # Para que cuando pulses una tecla, no puedas pulsar la contraria
    def on_key_press(self, key, modifiers):

        if self.last_key == arcade.key.UP and key == arcade.key.DOWN:
            self.last_key = arcade.key.UP
        elif self.last_key == arcade.key.DOWN and key == arcade.key.UP:
            self.last_key = arcade.key.DOWN
        elif self.last_key == arcade.key.LEFT and key == arcade.key.RIGHT:
            self.last_key = arcade.key.LEFT
        elif self.last_key == arcade.key.RIGHT and key == arcade.key.LEFT:
            self.last_key = arcade.key.RIGHT
        else:
            self.last_key = key

    def snake_eat(self):  # Para cuando come una manzana, remueve la que comió y se añade una nueva como tambien una parte de su cola
        if self.snake.eat_food(self.food):

            self.snake_new_segment(20, 20)
            self.food.remove_from_sprite_lists()
            self.new_food()

    # Aqui se añade el nuevo segmento de la cola
    def snake_new_segment(self, center_x, center_y):
        tail = Snake("sprites/snake2.png", 0.055, center_x, center_y)
        self.snake_tail.append(tail)
        self.sprites.append(tail)

    def new_food(self):  # Acá se genera una nueva manzana en una posición "x" o "random"
        numero_aleatorio_x = random.randrange(10, 491, 20)
        numero_aleatorio_y = random.randrange(10, 691, 20)

        self.food = Food("sprites/apple.png", 0.045,
                         numero_aleatorio_x, numero_aleatorio_y)
        self.sprites.append(self.food)

    # Para que se actualice la posicion de la cola y vaya detras de la anterior
    def actualizar_cola(self):
        if (round(self.snake.center_x) % 20 == 10) and (round(self.snake.center_y) % 20 == 10):
            if len(self.snake_tail) > 1:

                for i in range(len(self.snake_tail)-1, 0, -1):
                    segmento_anterior = self.snake_tail[i-1]
                    segmento_actual = self.snake_tail[i]
                    segmento_actual.center_x = segmento_anterior.center_x
                    segmento_actual.center_y = segmento_anterior.center_y

    def game_over(self):  # Muestra los sprites de: spacebar-Reiniciar y el de GameOver
        game_over_sprite = arcade.Sprite("sprites/game_over.png", 1)
        game_over_sprite.center_x = SCREEN_WIDTH / 2
        game_over_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprites.append(game_over_sprite)
        space_bar = arcade.Sprite("sprites/space_bar.png", 0.1)
        space_bar.center_x = SCREEN_WIDTH / 2
        space_bar.center_y = (SCREEN_HEIGHT / 2)-100
        self.sprites.append(space_bar)


def main():
    app = TransformWindow()
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
