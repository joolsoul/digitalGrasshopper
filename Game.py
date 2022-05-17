import copy
from enum import Enum


class GameState(Enum):
    PLAYING = 0
    FAIL = 1


class GameCell:
    def __init__(self, block: bool = False, number: int = 0, step: bool = False, is_locked=False, is_active=False):
        self._block = block
        self._number = number
        self._step = step
        self._is_locked = is_locked
        self._is_active = is_active

    @property
    def block(self) -> bool:
        return self._block

    @property
    def number(self) -> int:
        return self._number

    @property
    def step(self) -> bool:
        return self._step

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    @property
    def is_active(self) -> bool:
        return self._is_active


def read_int_multy_array_form_file(level_number: int):
    path = "resources/levels/level " + str(level_number)
    with open(path) as file:
        lst = file.readlines()
    return [[int(n) for n in x.split()] for x in lst]


class Game:
    def __init__(self, start_level: int):
        self._state = None
        self._row_count = 0
        self._col_count = 0
        self._field = []
        self._current_level = start_level
        self.new_game()
        self._current_cell = None
        self._current_cell_row = None
        self._current_cell_col = None
        self._steps = []

    def new_game(self) -> None:
        self.init_game_field()
        self._state = GameState.PLAYING

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def field(self) -> list:
        return self._field

    @property
    def state(self) -> GameState:
        return self._state

    @property
    def current_level(self) -> int:
        return self._current_level

    def init_game_field(self):
        level = read_int_multy_array_form_file(self._current_level)
        self._col_count = len(level[0])
        self._row_count = len(level)

        self._field = [
            copy.deepcopy([GameCell() for c in range(self.col_count)])
            for r in range(self.row_count)
        ]
        for row in range(len(level)):
            for column in range(len(level[0])):
                cell = level[row][column]
                if cell == 1:
                    self._field[row][column] = GameCell(block=True, number=1)
                if cell == 2:
                    self._field[row][column] = GameCell(block=True, number=2)
                if cell == 3:
                    self._field[row][column] = GameCell(block=True, number=3)
                if cell == 4:
                    self._field[row][column] = GameCell(block=True, number=4)

    def find_steps(self, row, column):
        if self._current_cell is None or not self._current_cell.block or self._current_cell.step:
            return
        else:
            step = self._current_cell.number
            self.check_neighbor(row - step, column)
            self.check_neighbor(row + step, column)
            self.check_neighbor(row, column - step)
            self.check_neighbor(row, column + step)
            self.check_neighbor(row - step, column + step)
            self.check_neighbor(row + step, column + step)
            self.check_neighbor(row - step, column - step)
            self.check_neighbor(row + step, column - step)

    def check_neighbor(self, row, column):
        if row < 0 or row >= len(self._field) or column < 0 or column >= len(self.field[row]):
            return
        elif not self._field[row][column].block and not self._field[row][column].step:
            self._field[row][column]._step = True
            self._steps.append([row, column])

    def swap_cells(self, row, col):
        for cell in self._steps:
            if cell[0] == row and cell[1] == col:
                self._steps.remove(cell)
        self._field[row][col] = self._current_cell
        self._field[row][col]._is_locked = True
        self._field[row][col]._is_active = False
        self._field[self._current_cell_row][self._current_cell_col] = GameCell()

    def clear_steps(self):
        for cell in self._steps:
            self._field[cell[0]][cell[1]] = GameCell()
        self._steps.clear()

    def on_button_click(self, row: int, col: int):
        if self.state != GameState.PLAYING:
            return

        if self._field[row][col].block and not self._field[row][col].is_locked:
            if self._current_cell is not None:
                self._current_cell._is_active = False
            self._current_cell = self._field[row][col]
            self._current_cell._is_active = True
            self.clear_steps()
            self._current_cell_row = row
            self._current_cell_col = col
            self.find_steps(row, col)

        if self._field[row][col].step:
            self.swap_cells(row, col)
            self.clear_steps()
