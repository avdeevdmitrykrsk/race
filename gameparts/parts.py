from random import randrange

import pygame

GRID_SIZE = 10
BOARD_BACKGROUND_COLOR = (106, 250, 151)

CAR_MAIN_GRID = 10
CAR_ENEMY_GRID = 20
BACKWARD_SPEED = 20


class Car:
    def __init__(self):
        self.car_main_get = pygame.image.load('car_objects_png/car_main.png')
        self.position = [(620, 600)]
        self.position_next = []
        self.car_main = self.car_main_get.get_rect(topright=self.position[0])
        self.direction = None
        self.next_direction = None
        self.flleft = False
        self.flright = False
        self.front_side = []
        self.last_pos = []

    def move(self):
        """Метод перемещает машину игрока."""
        if self.position:
            if self.flleft:
                if self.direction == 'Left':
                    self.position_next.append(
                        (
                            self.position[0][0] - CAR_MAIN_GRID,
                            self.position[0][1],
                        )
                    )
                    self.position.clear()
                    self.position.append(self.position_next[0])
                    self.position_next.clear()
                    self.direction = None
            elif self.flright:
                if self.direction == 'Right':
                    self.position_next.append(
                        (
                            self.position[0][0] + CAR_MAIN_GRID,
                            self.position[0][1],
                        )
                    )
                    self.position.clear()
                    self.position.append(self.position_next[0])
                    self.position_next.clear()
                    self.direction = None

            self.last_pos = [self.position[0]]

            self.front_side.clear()
            for i in range(0, 81, 10):
                self.front_side.append(
                    (self.position[0][0] + i, self.position[0][1]),
                )

    def draw(self, surface):
        """Метод отрисовывает машину игрока."""
        if self.position:
            self.car_main = self.car_main_get.get_rect(
                topright=self.position[0]
            )
            surface.blit(self.car_main_get, self.car_main)

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку."""
        if self.next_direction:
            self.direction = self.next_direction


class CarEnemyBlue:
    def __init__(self):
        self.exist = True
        self.car_enemy_crash = pygame.image.load(
            'car_objects_png/car_enemy_blue_after_crush.png'
        )
        self.car_main_get = pygame.image.load(
            'car_objects_png/car_enemy_blue.png'
        )
        self.position = []
        self.randomize_position()
        self.position_next = []
        self.back_side = []
        self.last_pos = []
        self.backward_pos = []

    def move(self):
        """Метод перемещает вражескую машину."""
        if self.exist:
            self.position_next = [
                (self.position[0][0], self.position[0][1] + CAR_ENEMY_GRID)
            ]
            self.position.clear()
            self.position.append(self.position_next[0])

            for i in range(0, 81, 20):
                self.back_side.append(
                    (self.position[0][0] + i, self.position[0][1] + 100),
                )

            self.position_next.clear()
            self.last_pos.clear()
            self.last_pos = [self.position[0]]

    def randomize_position(self):
        pos_x = randrange(500, 800, 20)
        self.position = [(pos_x, -220)]

    def move_back(self):
        """Метод перемещает вражескую машину в обратном направлении."""
        self.position_next.append(self.last_pos[0])
        self.backward_pos.append(
            (
                self.position_next[0][0],
                self.position_next[0][1] - BACKWARD_SPEED,
            )
        )
        self.position_next.clear()
        self.position_next.append(self.backward_pos[0])
        self.backward_pos.clear()

    def draw(self, surface):
        """Метод отрисовывает машину."""
        if self.position:
            self.car_main = self.car_main_get.get_rect(
                topright=self.position[0]
            )
            surface.blit(self.car_main_get, self.car_main)


class CarEnemyRed(CarEnemyBlue):
    def __init__(self):
        super().__init__()
        self.exist = False
        self.car_enemy_crash = pygame.image.load(
            'car_objects_png/car_enemy_red_after_crush.png'
        )
        self.car_main_get = pygame.image.load(
            'car_objects_png/car_enemy_red.png'
        )
        self.position = []
        self.randomize_position()
        self.position_next = []
        self.back_side = None
        self.last_pos = []
        self.backward_pos = []
