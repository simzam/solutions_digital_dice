"""
solution of execise #5 in "Digital Dice" by Nahin

Implementation does not care if several elevator have the same shortest distance,
draw one of them at random. Should be a sufficient solution given enough trials.

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
    # elevators = []
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
        # elevators.append([direction, distance])
    # print(elevators)
    # elevators.sort(key=lambda x: [1])
    # print(elevators)
    # return elevators[0][0]
    return tmp_dir

# too simple implementation, it is some trouble with discretizatip
def simple_elevators(num):
    for i in range(num):
        floor = rd.randint(1, 6)
        if floor < 2:
            return 1
    return 0


def elevator_sim(num, trials):
    counter = 0
    for i in range(trials):
        # elevators = build_elevators(num)

        # elevators.sort(key=lambda x: x[1])

        # direction = elevators[0][1]

        # print(elevators)

        # if num > 1 and elevators[0][2] == elevators[1][2]:
        #    i -= 1
        #    continue

        if find_closest_elevator(num) == 1:
            counter += 1

        # if simple_elevators(num) == 0:
        #    counter += 1

    return (counter / trials)


if __name__ == '__main__':
    elevators = 2
    trials = 100000
    exp1 = elevator_sim(elevators, trials)
    print(exp1, 13/18)
