"""problem 13

road stretch defined to have length 1. going from left to right.
directions are defined as 1 for left to right and -1 for right
"""
import random
import math


def calculate_distance_grass(police_car, accident_car):
    return abs((police_car % 1) - (accident_car % 1))


def calculate_distance_concrete(police_car, accident_car):
    if accident_car < police_car:
        return 2 - police_car + accident_car
    else:
        return accident_car - police_car


def calculate_responder_distance(police_car, accident_car):
    return [calculate_distance_grass(police_car, accident_car),
            calculate_distance_concrete(police_car, accident_car)]


def component_add_list(lst1, lst2):
    return [elem1 + elem2 for elem1, elem2 in zip(lst1, lst2)]


def component_div_list(lst, num):
    return [elem / num for elem in lst]


def main(num_patrol_cars, simulations):
    summed_resp_dist = [0] * (2 + (2 * num_patrol_cars))
    for _ in range(simulations):
        expr_result = experiment(num_patrol_cars)
        assert isinstance(expr_result, list) == True
        assert len(expr_result) == 2 + (2 * num_patrol_cars), print(len(expr_result))
        summed_resp_dist = component_add_list(summed_resp_dist, expr_result)
    return component_div_list(summed_resp_dist, simulations)


def experiment(num_patrol_cars):
    accident_car = 2 * random.random()
    stationary_car = 0.5
    police_cars = [random.random() for _ in range(num_patrol_cars)]

    responder_distances = calculate_responder_distance(stationary_car, accident_car)

    for patrol_cars_experiment, _ in enumerate(police_cars, start=1):
        tmp_closest_responder_grass = 2
        tmp_closest_responder_concr = 2
        for i in range(patrol_cars_experiment):
            distance = calculate_responder_distance(police_cars[i], accident_car)
            if distance[0] < tmp_closest_responder_grass:
                tmp_closest_responder_grass = distance[0]
            if distance[1] < tmp_closest_responder_concr:
                tmp_closest_responder_concr = distance[1]
        responder_distances += [tmp_closest_responder_grass,
                                tmp_closest_responder_concr]
    return responder_distances


if __name__ == '__main__':
    print(main(2, 1000000))
