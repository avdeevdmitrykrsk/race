import pygame

BOARD_BACKGROUND_COLOR = (106, 250, 151)
SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


def draw_window():
    road_get = pygame.image.load('car_objects_png/road.jpg')
    screen.blit(road_get, (0, 0))

def draw_score():
    pass


def draw_crash_back_side(car_main1, car_enemy):
    car_enemy.move_back()

    while car_enemy.position_next[0][1] > -120:
        car_enemy.move_back()

        clock.tick(20)
        draw_window()

        car_main_get = pygame.image.load('car_objects_png/car_main.png')
        car_main = car_main_get.get_rect(topright=car_main1.last_pos[0])
        screen.blit(car_main_get, car_main)

        car_en = car_enemy.car_enemy_crash.get_rect(
            topright=car_enemy.position_next[0]
        )
        screen.blit(car_enemy.car_enemy_crash, car_en)

        crashing_get = pygame.image.load('car_objects_png/crash.png')
        crashing_main = crashing_get.get_rect(
            topright=(
                car_main1.last_pos[0][0] + 20,
                car_main1.last_pos[0][1] - 60,
            )
        )
        screen.blit(crashing_get, crashing_main)
        pygame.display.update()

    pygame.quit()
