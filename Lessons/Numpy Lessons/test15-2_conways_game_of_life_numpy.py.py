import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class GameOfLife:
    def __init__(self, rows: int = 300, columns: int = 600):
        self.grid = np.random.randint(0, 2, size=(rows, columns))
        self.activity = np.zeros(self.grid.shape)

        dpi = 80.0
        figsize = (
            columns / dpi,
            rows / dpi,
        )

        self.fig = plt.figure(
            figsize=figsize,
            dpi=dpi,
        )

        self.ax = self.fig.add_axes(
            [0, 0, 1, 1],
            frameon=False,
        )

        self.image = self.ax.imshow(
            self.activity,
            interpolation="nearest",
            cmap=plt.cm.plasma,
            vmin=0,
            vmax=1,
        )

        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def update(self, frame):
        interior = self.grid[1:-1, 1:-1]

        neighbours = (
            self.grid[:-2, :-2]
            + self.grid[:-2, 1:-1]
            + self.grid[:-2, 2:]
            + self.grid[1:-1, :-2]
            + self.grid[1:-1, 2:]
            + self.grid[2:, :-2]
            + self.grid[2:, 1:-1]
            + self.grid[2:, 2:]
        )

        birth = (
            (neighbours == 3)
            & (interior == 0)
        )

        survive = (
            ((neighbours == 2) | (neighbours == 3))
            & (interior == 1)
        )

        self.grid[...] = 0
        interior[birth | survive] = 1

        # self.activity[self.activity > 0.5] = 0.5
        self.activity *= 0.985
        self.activity[self.grid == 1] = 1

        self.image.set_data(self.activity)

        return (self.image,)

    def run(self):
        self.animation = FuncAnimation(
            self.fig,
            self.update,
            interval=10,
            frames=2000,
            blit=True,
        )

        plt.show()


game = GameOfLife()
game.run()