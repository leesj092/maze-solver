from window import Window
from point import Point, Line

def main():
    win = Window(800, 600)

    line = Line(Point(80,80), Point(160, 160))
    win.draw_line(line, 'black')

    win.wait_for_close()


if __name__ == '__main__':
    main()
