"""Problem 17: Waiting for the Bus

Given that a bus leaves from the bus stop at every hour. Given that
there are a number of additional buses arriving every hour + random
number of minutes between 0 and 59, How long is the waiting time in
hours.

"""

import random


def calc_waiting_time(traveller, buses):
    for bus in buses:
        if bus >= traveller:
            return bus - traveller

    return 60 - traveller


def generate_random_hourly():
    return int((random.random() * 60) // 1)


def generate_buses(num_buses):
    buses = [0]
    for _ in range(num_buses):
        buses.append(generate_random_hourly())
    return sorted(buses)


def main():
    simulations = 100000
    print("i: number of buses\nwait: waiting time in hours\n")
    for i in range(10):
        waiting_time = 0
        for _ in range(simulations):
            buses = generate_buses(i)
            traveller = generate_random_hourly()
            waiting_time += calc_waiting_time(traveller, buses)
        print("i={:2}, wait={:1.4}".format(
            i + 1, waiting_time / simulations / 60))


if __name__ == '__main__':
    main()
