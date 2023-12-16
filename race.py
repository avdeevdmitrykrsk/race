import pygame
from gameparts import Car

pygame.init()

# Константы для размеров
GRID_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета фона
BOARD_BACKGROUND_COLOR = (106, 250, 151)

# Скорость движения
SPEED = 20

# Настройка игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
screen.fill(BOARD_BACKGROUND_COLOR)

# Заголовок окна игрового поля
pygame.display.set_caption('Гонка')

# Настройка времени
clock = pygame.time.Clock()


def main():

    car1 = Car()

    while True:
        clock.tick(SPEED)
        car1.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
