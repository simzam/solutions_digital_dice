import random

def calc_waiting_time(traveller, buses):
    for bus in buses:
        if bus >= traveller:
            return bus - traveller

    return 60 - traveller



vals = [i for i in range(60)]
for i in range(10):
    waiting_time = 0
    for _ in range(1000000):
        buses = sorted([0] + [random.choice(vals) for _ in range(i)])
        traveller = random.choice(vals)
        waiting_time += calc_waiting_time(traveller, buses)
    print(i+1, waiting_time / 1000000 / 60)
