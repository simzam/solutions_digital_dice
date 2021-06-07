
import random


simulations = 10000
count = 0
for _ in range(simulations):
    matchbox_1 = 40
    matchbox_2 = 40
    while matchbox_1 > 0 and matchbox_2 > 0:
        draw = random.random()
        if draw < 0.5:
            matchbox_1 -= 1
        else:
            matchbox_2 -= 1
        count += 1
print(count / simulations)

