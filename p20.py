import random


def loop_until(population, lim):
    """ loops over list until element is bigger than lim."""
    for p in population:
        if p > lim:
            return p
    return 0


def test_loop_until():
    population = [1, 2, 3, 4]
    lim = 3
    assert loop_until(population, lim) == 4
    lim = 0
    assert loop_until(population, lim) == 1
    lim = 5
    assert loop_until(population, lim) == 0


def simulate(population, sample_size, contentment, simulations):
    hits = 0
    for _ in range(simulations):
        random.shuffle(population)
        # print(population, sample_size, population[:sample_size])
        if sample_size > 0:
            best_sample = max(population[:sample_size])
            chosen_partner = loop_until(population[sample_size:], best_sample)
        else:
            chosen_partner = population[0]
        if chosen_partner == 0:
            continue
        else:
            # is chosen partner satisfactory??
            if chosen_partner >= max(population) - contentment:
                hits += 1
    return hits / simulations


def main():
    simulations = 10000
    population = [i for i in range(1, 51)]
    # contentment = [1, 2, 3, 4, 5]

    sample_sizes = [i for i in range(50)]
    ''
    hit_rates = []
    for sample_size in sample_sizes:
        hit_rates.append(simulate(population, sample_size, 5, simulations))
    for sample_size, hit_rate in zip(sample_sizes, hit_rates):
        print("{} {}".format(sample_size, hit_rate))


if __name__ == '__main__':
    main()
