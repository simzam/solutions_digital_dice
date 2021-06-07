import numpy as np
import random
import copy
import matplotlib.pyplot as plt


def move_umbrella(position, umbrellas):
    if position == 0: # home
        if umbrellas[0] > 0:
            umbrellas[0] -= 1
            umbrellas[1] += 1
            return umbrellas
    else:
        if umbrellas[1] > 0:
            umbrellas[1] -= 1
            umbrellas[0] += 1
            return umbrellas
    return False


def umbrella_sim(init_umbrellas, probabilities, points):
    averages = np.zeros(points)
    simulations = 10000

    for i, prob in enumerate(probabilities):
        counter = 0
        for _ in range(simulations):
            umbrellas = copy.deepcopy(init_umbrellas)
            position = 0 # 0 reps home, 1 reps office
            while umbrellas != False:
                decide_weather = random.random()

                if decide_weather < prob:
                    umbrellas = move_umbrella(position, umbrellas)
                position = (position + 1) % 2
                counter += 1
        averages[i] = counter / simulations

    return averages

    
if __name__ == '__main__':
    points = 200
    probabilities = np.linspace(0.01, 0.99, points)
    avg1 = umbrella_sim([1,1], probabilities, points)

    avg2 = umbrella_sim([2, 2], probabilities, points)

    plt.plot(probabilities, avg1)
    plt.plot(probabilities, avg2)
    plt.ylim((-10,200))
    plt.show()


