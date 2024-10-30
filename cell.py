from graphics import Point, Line

class Cell():
    def __init__(self, win):
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
