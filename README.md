# maze-solver
A visual interface (Tkinter) that draws, solves, and animates a maze in Python.

![Maze Generation and Solution](maze.gif)

## Features

- **Maze Generation**: Creates a random maze layout.
- **Wall Breaking with DFS**: Breaks down walls using DFS to ensure a solvable path.
- **Maze Solver**: Finds a solution vis DFS and draws path (gray path for unsolvable path)

## How It Works

1. **Maze Generation**: The maze is generated with walls between cells.
2. **Wall Breaking with DFS**: DFS is used to carve paths through the maze, guaranteeing a single solution path.
3. **Maze Solver**: A solver algorithm finds the solution from the maze start to the end.

## Requirements
- Python 3
- Tkinter:
I've found that the installing the tk-dev or python-tk packages are usually the easiest way to install and link it to your Python version.

You use Arch, btw:
```
sudo pacman -S tk
```

On Ubuntu (Linux), run:
```
sudo apt-get install python3-tk
```
Mac OS:
```
brew install python-tk
```

## Usage

```bash
git clone https://github.com/leesj092/maze-solver.git
cd maze-solver
./main.sh
