""" Problem 1: The clumsy dishwasher problem.

Imagine five worker commiting five mistakes.
Four of the five mistakes are caused by the same worker.
This worker claims this is random and not a result of his
clumsiness.
"""
import random


def experiment(prob):
    if random.random() < prob:
        return 1
    else:
        return 0


def main():
    simulations = 100000
    N = 5  # participants
    prob_clumsy = 1/N
    count_clumsy = 0
    simulations_clumsy = 0

    number_plates = 5

    for _ in range(simulations):
        for _ in range(number_plates):
            count_clumsy += experiment(prob_clumsy)
        if count_clumsy >= number_plates - 1:
            simulations_clumsy += 1
        count_clumsy = 0

    disp = "The probability of the event occuring where 1 of 5 worker has caused at least 4 of 5 accidents is simulated with {} experiment to be:\n{perc:.3f}%."
    print(disp.format(simulations, perc=simulations_clumsy / simulations * 100))


if __name__ == '__main__':
    main()
