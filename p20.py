"""Problem 20: An Optimal Stopping Problem

To choose an element in a population of known size under the rules
below:

1)_Total population of known size.
2) The elements in the population
can be sampled.
3) If an element is sampled and rejected, it can't be
picked later
4) If the population is exhausted the last element sampled
will be chosen.

This program will simulate three different success requirements, top
2, 3, or 4. For each of these sample sizes from 0 to population - 1
woll be plotted
"""
import random
from matplotlib import pyplot as plt


def draw_element(n):
    """ Draws a random int from [1, 2, ... , n] """
    return int((random.random()*n) // 1) + 1


def draw_sample(sample_size, n):
    """ Draws a sample of unique ints from [1, 2, .. , n]. """
    sample = set()
    i = 0
    while i < sample_size:
        sample.add(draw_element(n))
        if len(sample) < 1 + 1:
            continue
        i += 1
    return sample


def experiment(sample_size, n, accepted_size):
    if sample_size > n:
        print("Can't sample whole or more of the population, {} > {}".format(
            sample_size, n))
        return

    top_candidates = (i for i in range(n, n - accepted_size, -1))
    sample = draw_sample(sample_size, n)
    sample_max = max(sample)

    i = sample_size
    while i < n:
        candidate = draw_element(n)
        if candidate in sample:
            continue
        if candidate > sample_max:
            if candidate in top_candidates:
                return 1
            return 0
        i += 1
    return 0


def simulate(population, contentment, simulations):
    hit_rates = []
    for sample_size in range(1, population):
        hits = 0
        for _ in range(simulations):
            hits += experiment(sample_size, population, contentment)
        hit_rates.append(hits / simulations)
    return hit_rates


def main():
    acceptable_places = [2, 3, 4]
    population = 50
    simulations = 1000

    for acceptable in acceptable_places:
        plt.plot(simulate(population, acceptable,
                          simulations), label="top {}".format(acceptable))
    plt.legend()
    plt.xlabel("Sample size")
    plt.ylabel("hitrate")
    plt.show()


if __name__ == '__main__':
    main()
