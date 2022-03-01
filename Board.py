import pygame


class Board:
    # создание поля
    def __init__(self):

        self.width, self.height, self.left, self.top, self.cell_size, self.images = self.load_config()

        self.board = [[0] * self.width for _ in range(self.height)]
        self.fps = 2
        self.running = False

    def load_config(self):
        config = open('Life/config.txt', encoding='utf-8')
        data = config.readline().split()
        images = [pygame.image.load(data[5]), pygame.image.load(data[6])]
        images = [pygame.transform.scale(image, (int(data[4]), int(data[4]))) for image in
                  images]
        config.close()
        return int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), images

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(
                    (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                     self.cell_size))
                screen.fill(rect=rect, color=pygame.Color((255, 255, 255, 128)))
                screen.blit(self.images[self.board[i][j]],
                            [self.left + j * self.cell_size, self.top + i * self.cell_size])
                pygame.draw.rect(screen, pygame.Color('black'), rect, 2)

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[0] <= self.left + self.width * self.cell_size and self.top <= \
                mouse_pos[1] <= self.top + self.height * self.cell_size:
            x = (mouse_pos[0] - self.left) // self.cell_size
            y = (mouse_pos[1] - self.top) // self.cell_size
            return y, x

    def on_left_click(self, cell_coords):
        col = self.board[cell_coords[0]][cell_coords[1]]
        col += 1
        col %= len(self.images)
        self.board[cell_coords[0]][cell_coords[1]] = col

    def left_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_left_click(cell)

    def right_click(self):
        self.switch()

    def space_press(self):
        self.switch()

    def switch(self):
        self.running = not self.running

    def scroll(self, y):
        self.fps += y
        if self.fps < 0:
            self.fps = 0
