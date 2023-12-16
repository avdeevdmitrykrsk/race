import pygame


GRID_SIZE = 20


class Car:

    def __init__(self):
        self.speed = 10
        self.body_color = (255, 0, 0)
        self.positions = [
            (620, 600), (620, 620), (620, 640),
            (600, 600), (600, 620), (600, 640),
        ]

    def draw(self, surface):
        """Метод отрисовывает машину."""
        for position in self.positions:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)

        head_rect = pygame.Rect(
            (position[0], position[1]), (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, (0, 0, 0), head_rect, 4)
