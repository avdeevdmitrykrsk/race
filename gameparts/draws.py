import pygame

BOARD_BACKGROUND_COLOR = (106, 250, 151)
SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


def draw_crash(car_main1, car_enemy):

    clock.tick(20)
    screen.fill(BOARD_BACKGROUND_COLOR)

    car_main_get = pygame.image.load('car_objects_png/car_main.png')
    car_main = car_main_get.get_rect(topright=car_main1.last_pos[0])
    screen.blit(car_main_get, car_main)

    car_enemy_get = pygame.image.load(
        'car_objects_png/car_enemy_blue_after_crush.png'
    )
    car_en = car_enemy_get.get_rect(topright=car_enemy.position_next[0])
    screen.blit(car_enemy_get, car_en)

    crashing_get = pygame.image.load('car_objects_png/crash.png')
    crashing_main = crashing_get.get_rect(
        topright=(car_main1.last_pos[0][0] + 20, car_main1.last_pos[0][1] - 60)
    )
    screen.blit(crashing_get, crashing_main)
    pygame.display.update()
