"""
solution of execise #5 in "Digital Dice" by Nahin

Implementation does not care if several elevator have the same shortest distance,
draw one of them at random. Should be a sufficient solution given enough simulations.

0 : UP
1 : DOWN
"""
import random as rd


def build_elevators(num):
    elevators = []
    for i in range(num):
        floor = rd.randint(1, 7)

        while floor == 2:
            floor = rd.randint(1, 7)

        if floor == 1:
            elevator = [floor, 1, 1]
        elif floor == 7:
            elevator = [floor, 0, 5]
        elif floor == 2:
            direction = rd.randint(0, 1)
            if direction == 0:
                elevator = [floor, 0, 0]
            else:
                elevator = [floor, 1, 2]
        else:
            direction = rd.randint(0, 1)
            if direction == 0:
                elevator = [floor, 0, 11 - floor]
            else:
                elevator = [floor, 0, floor - 2]
        elevators.append(elevator)
    return elevators


def find_closest_elevator(num):
    tmp_min = 1000
    tmp_dir = -1
    for i in range(num):
        pos = rd.random()
        direction = rd.random()
        if pos < 1./6:
            if direction > 0.5:
                direction = 0
                distance = 1./6 - pos
            else:
                direction = 0
                distance = 1./6 + pos
        else:
            if direction > 0.5:
                direction = 1
                distance = pos - 1./6
            else:
                direction = 1
                distance = 2 - pos - 1./6
        if distance < tmp_min:
            tmp_min = distance
            tmp_dir = direction
    return tmp_dir

# too simple implementation, it is some trouble with discretizatip


# def simple_elevators(num):
#     for i in range(num):
#         floor = rd.randint(1, 6)
#         if floor < 2:
#             return 1
#     return 0


def simulate(num, simulations):
    counter = 0
    for _ in range(simulations):
        if find_closest_elevator(num) == 1:
            counter += 1
    return (counter / simulations)


def main():
    elevators = 2
    simulations = 100000
    exp1 = simulate(elevators, simulations)
    print(exp1, 13/18)


if __name__ == '__main__':
    main()
