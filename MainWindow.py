import os

from MainWundowUI import Ui_MainWindow as MainWindowUI
from Game import *

from PyQt5 import QtSvg
from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        images_dir = os.path.join(os.path.dirname(__file__), 'resources/images')
        self._images = {
            os.path.splitext(f)[0]: QtSvg.QSvgRenderer(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }

        self.game = Game(1)
        self.game_resize(self.game)

        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                painter.restore()

        self.game_field.setItemDelegate(MyDelegate(self))
        self.new_game_Button.clicked.connect(self.new_game)

        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.game_field.indexAt(e.pos())
            self.on_item_clicked(idx, e)

        self.game_field.mousePressEvent = new_mouse_press_event

    def game_resize(self, game: Game) -> None:
        model = QStandardItemModel(game.row_count, game.col_count)
        self.game_field.setModel(model)
        self.resize(game.col_count * 60 + 20, game.row_count * 50 + 116)
        self.update_view()

    def new_game(self):
        self.game = Game(self.level_number.value())
        self.update_view()

    def update_view(self):
        self.game_field.viewport().update()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        cell = self.game.field[e.row()][e.column()]
        img = self._images['default']
        if cell.block:
            name = ""
            if cell.is_active:
                name = name + "active "
            if cell.is_locked:
                name = name + "locked "
            if cell.number == 1:
                name = name + "1"
            if cell.number == 2:
                name = name + "2"
            if cell.number == 3:
                name = name + "3"
            if cell.number == 4:
                name = name + "4"
            img = self._images[name]
        if cell.step:
            img = self._images['step']
        img.render(painter, QRectF(option.rect))

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton or me.button() == Qt.RightButton:
            self.game.on_button_click(e.row(), e.column())
            self.is_game_over()
        self.update_view()

    def is_game_over(self):
        pass
