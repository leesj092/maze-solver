from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + (i * self._cell_size_x)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + (j * self._cell_size_y)
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            can_visit = []

            # can go left
            if i > 0 and not self._cells[i - 1][j].visited:
                can_visit.append((i - 1, j))

            # can go right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                can_visit.append((i + 1, j))

            # can go up
            if j > 0 and not self._cells[i][j - 1].visited:
                can_visit.append((i, j - 1))

            # can go down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                can_visit.append((i, j + 1))

            if len(can_visit) == 0:
                self._draw_cell(i, j)
                return

            next_index = can_visit[random.randrange(len(can_visit))]

            # breaking left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left = False
                self._cells[i - 1][j].has_right = False

            # breaking right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right = False
                self._cells[i + 1][j].has_left = False

            # breaking up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top = False
                self._cells[i][j - 1].has_bottom = False

            # breaking down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom = False
                self._cells[i][j + 1].has_top = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # go left
        if i > 0 and not cell.has_left and not self._cells[i - 1][j].visited:
            cell.draw_move(self._cells[i - 1][j])
            solved = self._solve_r(i - 1, j)

            if solved:
                return True
            else:
                cell.draw_move(self._cells[i - 1][j], undo=True)

        # go right
        if i < self._num_cols - 1 and not cell.has_right and not self._cells[i + 1][j].visited:
            cell.draw_move(self._cells[i + 1][j])
            solved = self._solve_r(i + 1, j)

            if solved:
                return True
            else:
                cell.draw_move(self._cells[i + 1][j], undo=True)

        # go up
        if j > 0 and not cell.has_top and not self._cells[i][j - 1].visited:
            cell.draw_move(self._cells[i][j - 1])
            solved = self._solve_r(i, j - 1)

            if solved:
                return True
            else:
                cell.draw_move(self._cells[i][j - 1], undo=True)

        # go down
        if j < self._num_rows - 1 and not cell.has_bottom and not self._cells[i][j + 1].visited:
            cell.draw_move(self._cells[i][j + 1])
            solved = self._solve_r(i, j + 1)

            if solved:
                return True
            else:
                cell.draw_move(self._cells[i][j + 1], undo=True)

        return False
