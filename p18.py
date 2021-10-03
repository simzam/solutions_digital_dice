"""problem 18: Waiting for Stoplights

Imagine a quadratic grid (m, m) large. Our goail is to reach (1, 1)
from the starting point (m, m) to the finish (1,1). When at a point
(i, j) there are two options either (i - 1, j) or (i, j - 1). If
either i or j equals 1 there are only one option.

In the problem the grid is described as blocks in a city. Where the
choice to move either south (i, j - 1) or east (i - 1, j)depends on
which direction is allowed by the traffic lights without waiting.

The text asks what the average number traffic lights a person moving
using the above algorithm will encounter on a trip from (m, m) to (1,
1).
"""

import random
import matplotlib.pyplot as plt


def experiment(size):
    x = size
    y = size
    while x > 1 and y > 1:
        if random.random() < 1/2:
            x -= 1
        else:
            y -= 1
    if x <= 1 and y <= 1:
        return 0
    else:
        return (max(x, y) - 1) * 1/2


def plot(lst, sims):
    plt.plot(lst)
    title = "Simulation of problem 18, with {} simulations"
    plt.title(title.format(sims))

    plt.xlabel("Size of grid")
    plt.ylabel("Average number of stops")
    plt.show()


def main():
    max_grid_size = 100
    simulations = 200

    avg_stops = []

    for size in range(2, max_grid_size + 1):
        counter = 0
        for _ in range(simulations):
            counter += experiment(size)
        avg_stops.append(counter / simulations)
    plot(avg_stops, simulations)


if __name__ == '__main__':
    main()
