"""Exercise 12

Let say you arrive in the middle of a marathon where runners were
given numbers randomly. You stand there for a short while observing a
sample S = {x1, x2, ... , xn}, what can you know about the number of
runners N. One estimation formula estimates

N = (n + 1)/n E(max(xi)) - 1

This program is a Monte Carlo simulation to numerically evaluate the
precision of this formula for several different sample percentages
"""
import random
import matplotlib.pyplot as plt


def main():
    min_runners = 100
    max_runners = 1000

    num_simulations = 10000
    num_bins = 100

    sample_size_percentages = [.02, .05, .10, .20]

    fig, axs = plt.subplots(1, len(sample_size_percentages),
                            sharey=True, tight_layout=True)
    fig.suptitle('Error in estimation of $N$ for different sample size percentages $s$')

    for i, sample_size_percentage in enumerate(sample_size_percentages):
        errors = []
        for _ in range(num_simulations):
            N = random.randrange(min_runners, max_runners)
            population = [i for i in range(N)]
            observed = []
            sample_size = 0
            while sample_size / N <= sample_size_percentage:
                observed.append(random.choice(population))
                sample_size += 1

            est_num_runners = (sample_size+1)/sample_size*max(observed)-1
            percentage_diff = (N - est_num_runners) / N
            errors.append(percentage_diff)

        axs[i].hist(errors, num_bins)
        axs[i].set_title("$s$: {}".format(sample_size_percentage))
        axs[i].set_xlim((-0.5, 0.5))
    plt.show()


if __name__ == '__main__':
    main()
