import random
import matplotlib.pyplot as plt

possible_movements = [-2, -1, 1, 2]
records = {1: 0}
simulations = 1000000
    
for _ in range(simulations):
    length_travel = 0
    current_point = 0
    travelled_path = [current_point]

    while True:
        move = random.choice(possible_movements)
        current_point += move
        if current_point in travelled_path:
            length = len(travelled_path)
            try:
                records[length] += 1
            except KeyError:
                records[length] = 1
            break
        
        travelled_path.append(current_point)

recs = []
for key in records.keys():
    recs.append((key, records[key] / simulations))

print(recs)
