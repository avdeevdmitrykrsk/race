import pygame

GRID_SIZE = 10
BOARD_BACKGROUND_COLOR = (106, 250, 151)

CAR_MAIN_SPEED = 20
CAR_ENEMY_SPEED = 10


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
                        (self.position[0][0] - CAR_MAIN_SPEED,
                         self.position[0][1])
                    )
                    self.position.clear()
                    self.position.append(self.position_next[0])
                    self.position_next.clear()
                    self.direction = None
            elif self.flright:
                if self.direction == 'Right':
                    self.position_next.append(
                        (self.position[0][0] + CAR_MAIN_SPEED,
                         self.position[0][1])
                    )
                    self.position.clear()
                    self.position.append(self.position_next[0])
                    self.position_next.clear()
                    self.direction = None

            self.last_pos = [self.position[0]]

            self.front_side = [
                self.position[0],
                (self.position[0][0] + 20, self.position[0][1]),
                (self.position[0][0] + 40, self.position[0][1]),
                (self.position[0][0] + 60, self.position[0][1]),
                (self.position[0][0] + 80, self.position[0][1]),
            ]

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


class CarEnemy:

    def __init__(self):
        self.car_main_get = pygame.image.load(
            'car_objects_png/car_enemy_blue.png'
        )
        self.position = [(620, -200)]
        self.position_next = []
        self.back_side = []
        self.last_pos = []
        self.backward_pos = []

    def move(self):
        """Метод перемещает вражескую машину."""
        if self.position:
            self.position_next.append(
                (self.position[0][0], self.position[0][1] + CAR_ENEMY_SPEED)
            )
            self.position.clear()
            self.position.append(self.position_next[0])
            self.back_side = [
                (self.position[0][0], self.position[0][1] + 100),
                (self.position[0][0] + 10, self.position[0][1] + 100),
                (self.position[0][0] + 20, self.position[0][1] + 100),
                (self.position[0][0] + 30, self.position[0][1] + 100),
                (self.position[0][0] + 40, self.position[0][1] + 100),
                (self.position[0][0] + 50, self.position[0][1] + 100),
                (self.position[0][0] + 60, self.position[0][1] + 100),
                (self.position[0][0] + 70, self.position[0][1] + 100),
                (self.position[0][0] + 80, self.position[0][1] + 100),
                (self.position[0][0] + 90, self.position[0][1] + 100),
                (self.position[0][0] + 100, self.position[0][1] + 100),
            ]
            self.position_next.clear()
            self.last_pos.clear()
            self.last_pos = [self.position[0]]

    def move_back(self):
        """Метод перемещает вражескую машину в обратном направлении."""
        self.position_next.append(self.last_pos[0])
        self.backward_pos.append(
            (self.position_next[0][0],
             self.position_next[0][1] - CAR_ENEMY_SPEED)
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
