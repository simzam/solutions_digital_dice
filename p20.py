import random


def simulate_rec(point):
    """for some reason unittest does not immediately seem to work with recursive functions. """
    print(point)
    if point[0] <= 1 or point[1] <= 1:
        if point[0] == point[1]:
            print('memem')
            return 0
        return max(point[0], point[1]) * 1/2
    else:
        if random.random() < 1/2:
            simulate([point[0] - 1, point[1]])
        else:
            simulate([point[0], point[1] - 1])


def simulate(point):
    """non-rec version of above function. """
    while point[0] >= 1 and point[1] >= 1:
        if random.random() < 1/2:
            point[0] -= 1
        else:
            point[1] -= 1
    if point[0] <= 1 and point[1] <= 1:
        return 0
    else:
        return (max(point[0], point[1]) - 1) * 1/2


def main():
    max_grid_size = 1000
    simulations = 1000

    avg_stops = []

    for size in range(max_grid_size + 1):
        counter = 0
        for _ in range(simulations):
            # print(type(counter), counter)
            a = simulate([size, size])
            # print(a)
            counter += simulate([size, size])
        avg_stops.append(counter / simulations)

    print(avg_stops)
    # TODO plot


if __name__ == '__main__':
    main()