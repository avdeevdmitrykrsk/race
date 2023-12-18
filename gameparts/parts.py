import pygame

GRID_SIZE = 20
BOARD_BACKGROUND_COLOR = (106, 250, 151)


class Car:

    def __init__(self):
        self.car_main_get = pygame.image.load('car_objects/car_main.png')
        self.position = [(620, 600)]
        self.position_next = []
        self.car_main = self.car_main_get.get_rect(topright=self.position[0])
        self.direction = None
        self.next_direction = None
        self.flleft = False
        self.flright = False

    def move(self):
        """Метод перемещает машину игрока."""
        if self.flleft:
            if self.direction == 'Left':
                self.position_next.append(
                    (self.position[0][0] - 40, self.position[0][1])
                )
                self.position.clear()
                self.position.append(self.position_next[0])
                self.position_next.clear()
                self.direction = None

        elif self.flright:
            if self.direction == 'Right':
                self.position_next.append(
                    (self.position[0][0] + 40, self.position[0][1])
                )
                self.position.clear()
                self.position.append(self.position_next[0])
                self.position_next.clear()
                self.direction = None

    def draw(self, surface):
        """Метод отрисовывает машину игрока."""
        self.car_main = self.car_main_get.get_rect(topright=self.position[0])
        surface.fill(BOARD_BACKGROUND_COLOR)
        surface.blit(self.car_main_get, self.car_main)

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку."""
        if self.next_direction:
            self.direction = self.next_direction


class CarEnemy:

    def __init__(self):
        self.car_main_get = pygame.image.load('car_objects/car_enemy_blue.png')
        self.position = [(600, -200)]
        self.position_next = []

    def move(self):
        """Метод перемещает вражескую машину."""
        self.position_next.append(
            (self.position[0][0], self.position[0][1] + GRID_SIZE)
        )
        self.position.clear()
        self.position.append((self.position_next[0]))
        self.position_next.clear()

    def draw(self, surface):
        """Метод отрисовывает машину."""
        self.car_main = self.car_main_get.get_rect(topright=self.position[0])
        surface.blit(self.car_main_get, self.car_main)
