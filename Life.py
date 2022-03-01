import pygame

from Board import Board
from copy import deepcopy


class Life(Board):
    def coords_correct(self, x, y):
        if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
            return True
        return False

    def next_move(self):
        temp_board = deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                alive = 0
                a = x
                b = (y - 1) % self.height
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                a = (x + 1) % self.width
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                b = y
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                b = (y + 1) % self.height
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                a = x
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                a = (x - 1) % self.width
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                b = y
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                b = (y - 1) % self.height
                if self.coords_correct(a, b):
                    if temp_board[b][a]:
                        alive += 1
                if self.board[y][x] == 0:
                    if alive == 3:
                        self.board[y][x] = 1
                else:
                    if alive < 2 or alive > 3:
                        self.board[y][x] = 0


# clock = pygame.time.Clock()
#
# running = True
# pygame.init()
#
# config = open('Life/config.txt', encoding='utf-8')
# data = config.readline().split()
# size = width, height = int(data[0]) * int(data[4]) + 2 * int(data[2]), int(data[1]) * int(
#     data[4]) + 2 * int(data[3])
# config.close()
#
# screen = pygame.display.set_mode(size)
# screen.fill(pygame.Color('black'))
# life = Life()
# frame = 0
#
# while running:
#
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 life.left_click(event.pos)
#             if event.button == 3:
#                 life.right_click()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == 32:
#                 life.space_press()
#
#         if event.type == pygame.MOUSEWHEEL:
#             life.scroll(event.y)
#     frame += 1
#
#     if life.running:
#         life.next_move()
#         clock.tick(life.fps)
#     screen.fill((255, 255, 255))
#     life.render(screen)
#     pygame.display.flip()
