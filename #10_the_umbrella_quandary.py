
import numpy as np
import random
import matplotlib.pyplot as plt

points = 80

probabilities = np.linspace(0.01, 0.99, points)
averages = np.zeros(points)
simulations = 30000

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

for i, prob in enumerate(probabilities):
    counter = 0
    for _ in range(simulations):
        umbrellas = [2, 2]
        position = 0 # 0 reps home, 1 reps office
        while umbrellas:
            decide_weather = random.random()
            if decide_weather < prob:
                umbrellas = move_umbrella(position, umbrellas)

            position = (position + 1) % 2
            counter += 1
    averages[i] = counter / simulations
        
plt.plot(probabilities, averages)
plt.show()
