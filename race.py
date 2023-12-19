import pygame

from gameparts import Car, CarEnemy, draw_crash

pygame.init()

GRID_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

BOARD_BACKGROUND_COLOR = (106, 250, 151)

GAME_SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
screen.fill(BOARD_BACKGROUND_COLOR)

pygame.display.set_caption('Гонка')

clock = pygame.time.Clock()


def handle_keys(game_object):
    """Функция обработки действий пользователя."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_object.next_direction = 'Left'
                    game_object.flleft = True
                elif event.key == pygame.K_RIGHT:
                    game_object.next_direction = 'Right'
                    game_object.flright = True
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    game_object.flleft = False
                    game_object.flright = False
        break


def check_collision(car_main1, car_enemy):
    for crash in car_main1.front_side:
        for crosh in car_enemy.back_side:
            if crosh == crash:
                car_main1.position.clear()
                car_enemy.position.clear()
                car_enemy.move_back()
                draw_crash(car_main1, car_enemy)
            else:
                continue


def main():
    car_main1 = Car()
    car_enemy_blue = CarEnemy()

    while True:
        clock.tick(GAME_SPEED)
        handle_keys(car_main1)
        car_main1.update_direction()
        car_main1.move()
        car_enemy_blue.move()
        screen.fill(BOARD_BACKGROUND_COLOR)
        check_collision(car_main1, car_enemy_blue)
        car_main1.draw(screen)
        car_enemy_blue.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
