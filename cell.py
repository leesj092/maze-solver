from graphics import Point, Line

class Cell():
    def __init__(self, win=None):
        self.has_left = True
        self.has_right = True
        self.has_top = True
        self.has_bottom = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if not self._win:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        from_x = (self._x1 + self._x2) / 2
        from_y = (self._y1 + self._y2) / 2
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(from_x, from_y), Point(to_x, to_y))

        if undo:
            self._win.draw_line(line, fill_color='gray')
        else:
            self._win.draw_line(line, fill_color='red')

