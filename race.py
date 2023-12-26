import pygame

from gameparts import Car, CarEnemyBlue, CarEnemyRed
from gameparts import draw_crash_back_side, draw_window

pygame.init()

score = 0

SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800

BOARD_BACKGROUND_COLOR = (106, 250, 151)

GAME_SPEED = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

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
    if car_enemy.exist:
        for crash in car_main1.front_side:
            for crosh in car_enemy.back_side:
                if crosh == crash:
                    car_enemy.exist = False
                    car_main1.position.clear()
                    draw_crash_back_side(car_main1, car_enemy)
                else:
                    continue
        for crash in car_main1.front_side:
            for crosh in car_enemy.left_side:
                if crosh == crash:
                    car_enemy.exist = False
                    car_main1.position.clear()
                    draw_crash_back_side(car_main1, car_enemy)
                else:
                    continue
        for crash in car_main1.front_side:
            for crosh in car_enemy.right_side:
                if crosh == crash:
                    car_enemy.exist = False
                    car_main1.position.clear()
                    draw_crash_back_side(car_main1, car_enemy)
                else:
                    continue


def car_enemy_timer(car_enemy_blue, car_enemy_red):
    global score
    if car_enemy_blue.exist:
        if car_enemy_blue.position[0][1] == 300:
            car_enemy_red.exist = True
            car_enemy_red.randomize_position()
        elif car_enemy_blue.position[0][1] > 800:
            score += 100
            car_enemy_blue.exist = False
    if car_enemy_red.exist:
        if car_enemy_red.position[0][1] == 300:
            car_enemy_blue.exist = True
            car_enemy_blue.randomize_position()
        elif car_enemy_red.position[0][1] > 800:
            score += 100
            car_enemy_red.exist = False


def check_win():
    pass


def main():
    car_main1 = Car()
    car_enemy_blue = CarEnemyBlue()
    car_enemy_red = CarEnemyRed()

    while True:
        clock.tick(GAME_SPEED)
        handle_keys(car_main1)
        car_main1.update_direction()
        car_main1.move()
        draw_window()
        car_enemy_timer(car_enemy_blue, car_enemy_red)
        car_enemy_blue.move()
        car_enemy_red.move()
        check_collision(car_main1, car_enemy_blue)
        check_collision(car_main1, car_enemy_red)
        car_enemy_blue.draw(screen)
        car_enemy_red.draw(screen)
        car_main1.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
