# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:26:06 2026

@author: mmerc
"""
import random
import tkinter as tk
# import numpy as np

CELL_SIZE = 15
UPDATE_DELAY_MS = 100


def compute_neighbours(grid: list[list[int]]) -> list[list[int]]:
    # Python implementation
    
    rows = len(grid)
    columns = len(grid[0])

    neighbours = [
        [0] * columns
        for _ in range(rows)
    ]

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            neighbours[row][column] = (
                grid[row - 1][column - 1]
                + grid[row - 1][column]
                + grid[row - 1][column + 1]
                + grid[row][column - 1]
                + grid[row][column + 1]
                + grid[row + 1][column - 1]
                + grid[row + 1][column]
                + grid[row + 1][column + 1]
            )

    return neighbours
    

def iterate(grid: list[list[int]]) -> list[list[int]]:
    neighbours = compute_neighbours(grid)
    next_grid = [row.copy() for row in grid]

    rows = len(grid)
    columns = len(grid[0])

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            alive = grid[row][column] == 1
            count = neighbours[row][column]

            if alive and count not in (2, 3):
                next_grid[row][column] = 0
            elif not alive and count == 3:
                next_grid[row][column] = 1

    return next_grid


def create_random_grid(
    rows: int,
    columns: int,
) -> list[list[int]]:
    grid = [
        [random.randint(0, 1) for _ in range(columns)]
        for _ in range(rows)
    ]

    # Keep the outer boundary dead.
    for column in range(columns):
        grid[0][column] = 0
        grid[-1][column] = 0

    for row in range(rows):
        grid[row][0] = 0
        grid[row][-1] = 0

    return grid


class GameOfLifeGUI:
    def __init__(
        self,
        window: tk.Tk,
        rows: int,
        columns: int,
    ) -> None:
        self.window = window
        self.rows = rows
        self.columns = columns
        self.running = False

        self.grid = create_random_grid(rows, columns)

        self.canvas = tk.Canvas(
            window,
            width=columns * CELL_SIZE,
            height=rows * CELL_SIZE,
            background="white",
        )
        self.canvas.pack()

        controls = tk.Frame(window)
        controls.pack(pady=8)

        tk.Button(
            controls,
            text="Start",
            command=self.start,
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            controls,
            text="Pause",
            command=self.pause,
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            controls,
            text="Step",
            command=self.step,
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            controls,
            text="Randomise",
            command=self.randomise,
        ).pack(side=tk.LEFT, padx=4)

        self.draw_grid()

    def draw_grid(self) -> None:
        self.canvas.delete("all")

        for row_index, row in enumerate(self.grid):
            for column_index, cell in enumerate(row):
                x1 = column_index * CELL_SIZE
                y1 = row_index * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                fill = "black" if cell else "white"

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=fill,
                    outline="white",
                )

    def step(self) -> None:
        self.grid = iterate(self.grid)
        self.draw_grid()

    def start(self) -> None:
        if not self.running:
            self.running = True
            self.update()

    def pause(self) -> None:
        self.running = False

    def update(self) -> None:
        if not self.running:
            return

        self.step()
        self.window.after(UPDATE_DELAY_MS, self.update)

    def randomise(self) -> None:
        self.grid = create_random_grid(
            self.rows,
            self.columns,
        )
        self.draw_grid()


def main() -> None:
    rows = 30
    columns = 50

    window = tk.Tk()
    window.title("Conway's Game of Life")

    GameOfLifeGUI(window, rows, columns)

    window.mainloop()


if __name__ == "__main__":
    main()