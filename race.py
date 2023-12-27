import pygame
import pygame_menu

from gameparts import Car, CarEnemyBlue, CarEnemyRed
from gameparts import draw_crash_back_side, draw_window, score

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1240, 800

BOARD_BACKGROUND_COLOR = (106, 250, 151)

GAME_SPEED = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption('Гонка')

clock = pygame.time.Clock()

user_name = ''


def handle_keys(game_object):
    """Функция обработки действий пользователя."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
                    write_scores()
                    start_the_game()
                else:
                    continue
        for crash in car_main1.front_side:
            for crosh in car_enemy.left_side:
                if crosh == crash:
                    car_enemy.exist = False
                    car_main1.position.clear()
                    draw_crash_back_side(car_main1, car_enemy)
                    write_scores()
                    start_the_game()
                else:
                    continue
        for crash in car_main1.front_side:
            for crosh in car_enemy.right_side:
                if crosh == crash:
                    car_enemy.exist = False
                    car_main1.position.clear()
                    draw_crash_back_side(car_main1, car_enemy)
                    write_scores()
                    start_the_game()
                else:
                    continue


def car_enemy_timer(car_enemy_blue, car_enemy_red):
    global score
    if car_enemy_blue.exist:
        if car_enemy_blue.position[0][1] == 300:
            car_enemy_red.exist = True
            car_enemy_red.randomize_position()
        if car_enemy_blue.position[0][1] > 799:
            score += 100
            car_enemy_blue.exist = False
    if car_enemy_red.exist:
        if car_enemy_red.position[0][1] == 300:
            car_enemy_blue.exist = True
            car_enemy_blue.randomize_position()
        elif car_enemy_red.position[0][1] > 799:
            score += 100
            car_enemy_red.exist = False


def draw_score():
    dr_score = pygame.font.Font(None, 36)
    text = dr_score.render(f'Очки:   {score}', 1, (180, 0, 0))
    screen.blit(text, (10, 50))


def write_scores():
    global user_name
    global score
    with open('scores.txt', 'a', encoding='utf-8') as f:
        f.write(f'{user_name}:    {score} очков!\n')
        score = 0
        pygame.time.wait(700)


def leader_table():
    menu = pygame_menu.Menu(
    f'Таблица лидеров', 1240, 800, theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.button('Назад', start_the_game)
    menu.mainloop(screen)


def check_win():
    pass


def start_the_game():
    global user_name
    user_name = user_name_get.get_value()
    main_menu(user_name)

def main_menu(name):
    menu = pygame_menu.Menu(
    f'Э рон-дон-дон {name}!!!', 1240, 800, theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.button('Начать', main)
    menu.add.button('Таблица лидеров', leader_table)
    menu.add.button('Выход', pygame_menu.events.EXIT)
    menu.mainloop(screen)


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
        car_enemy_blue.move()
        car_enemy_red.move()
        car_enemy_timer(car_enemy_blue, car_enemy_red)
        check_collision(car_main1, car_enemy_blue)
        check_collision(car_main1, car_enemy_red)
        car_enemy_blue.draw(screen)
        car_enemy_red.draw(screen)
        car_main1.draw(screen)
        draw_score()
        pygame.display.update()


menu_name = pygame_menu.Menu(
'               Введите имя', 1240, 800, theme=pygame_menu.themes.THEME_BLUE
)
user_name_get = menu_name.add.text_input('Имя:    ', maxchar=10)
menu_name.add.button('Продолжить', start_the_game)
menu_name.mainloop(screen)


if __name__ == '__main__':
    main()
