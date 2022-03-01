import sys

from PyQt5.QtCore import Qt
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from Life import *
from Board import *
from AnimatedSprite import *
import pygame


class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Life/input.ui', self)
        self.set_default_values()
        self.connect_buttons()

    def set_default_values(self):
        config = open('Life/config.txt', encoding='utf-8')
        data = config.read()
        print(data)
        self.widthSpinBox.setValue(int(data[0]))
        self.heightSpinBox.setValue(int(data[1]))
        self.cellSizeSpinBox.setValue(int(data[4]))
        config.close()

    def connect_buttons(self):
        self.cellTextureButton.clicked.connect(self.cell_texture)
        self.aliveTextureButton.clicked.connect(self.alive_texture)
        self.applyButton.clicked.connect(self.apply_button)

    def cell_texture(self):
        self.cell_texture_fn = QFileDialog.getOpenFileName(self, 'Выбрать текстуру ячеек', '')[0]

    def alive_texture(self):
        self.alive_texture_fn = QFileDialog.getOpenFileName(self, 'Выбрать текстуру существ', '')[0]

    def apply_button(self):
        global life

        error = False
        self.errortext = ''
        if self.widthSpinBox.value() <= 0:
            self.errortext += 'Некорректная ширина поля\t'
            error = True
        if self.heightSpinBox.value() <= 0:
            self.errortext += 'Некорректная высота поля\t'
            error = True
        if self.cellSizeSpinBox.value() <= 0:
            self.errortext += 'Некорректный размер ячейки'
            error = True

        if not error:
            self.width = self.widthSpinBox.value()
            self.height = self.heightSpinBox.value()
            self.cell_size = self.cellSizeSpinBox.value()
            config = open('Life/config.txt', encoding='utf-8', mode='w')
            config.write(str(self.width) + ' ' + str(
                self.height) + ' ' + '10' + ' ' + '10' + ' ' + str(
                self.cell_size) + ' ' + self.cell_texture_fn + ' ' + self.alive_texture_fn)
            config.close()
            self.mainloop()

    def mainloop(self):
        global app

        app.exec_()
        clock = pygame.time.Clock()

        running = True
        pygame.init()

        config = open('Life/config.txt', encoding='utf-8')
        data = config.readline().split()
        size = width, height = int(data[0]) * int(data[4]) + 2 * int(data[2]), int(data[1]) * int(
            data[4]) + 2 * int(data[3])
        config.close()

        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('black'))
        life = Life()
        frame = 0

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        life.left_click(event.pos)
                    if event.button == 3:
                        life.right_click()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print('1')
                        running = False
                        pygame.quit()
                        return None
                    if event.key == 32:
                        life.space_press()

                if event.type == pygame.MOUSEWHEEL:
                    life.scroll(event.y)
            frame += 1

            if life.running:
                life.next_move()
                clock.tick(life.fps)
            screen.fill((255, 255, 255))
            life.render(screen)
            pygame.display.flip()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = InputWindow()
    ex.show()
    sys.exit(app.exec_())
