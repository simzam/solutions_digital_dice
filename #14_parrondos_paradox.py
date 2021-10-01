import random

import matplotlib.pyplot as plt


def game_a(eps):
    return 1 if random.random() < 0.5 - eps else -1


def game_b(eps, capital):
    if capital % 3 == 0:
        return 1 if random.random() < 0.1 - eps else -1
    else:
        return 1 if random.random() < 0.75 - eps else -1


def run_single_games(k_a, k_b, eps, num_games):
    mk_a = [k_a]
    mk_b = [k_b]
    for _ in range(num_games):
        k_a += game_a(eps)
        k_b += game_b(eps, k_b)
        mk_a.append(k_a)
        mk_b.append(k_b)
    return mk_a, mk_b

def run_random_game(k, eps, num_games):
    mk = [k]
    for _ in range(num_games):
        if random.random() < 0.5:
            k += game_a(eps)
        else:
            k += game_b(eps, k)
        mk.append(k)
    return mk


def component_add_list(lst1, lst2):
    return [elem1 + elem2 for elem1, elem2 in zip(lst1, lst2)]


def component_div_list(lst, num):
    return [elem / num for elem in lst]


def main(k = 0, num_games = 100, simulations = 10000):
    sum_game_a = [0] * (num_games + 1)
    sum_game_b = [0] * (num_games + 1)
    sum_game_mixed = [0] * (num_games + 1)

    eps = 0.005

    for _ in range(simulations):
        tmp_a, tmp_b = run_single_games(k, k, eps, num_games)
        tmp_mixed = run_random_game(k, eps, num_games)
        sum_game_a = component_add_list(sum_game_a, tmp_a)
        sum_game_b = component_add_list(sum_game_b, tmp_b)
        sum_game_mixed = component_add_list(sum_game_mixed, tmp_mixed)
    x_coordinates = [i for i in range(num_games + 1)]


    print(sum_game_a)
    plt.plot(x_coordinates, component_div_list(sum_game_a, simulations))
    plt.plot(x_coordinates, component_div_list(sum_game_b, simulations))
    plt.plot(x_coordinates, component_div_list(sum_game_mixed, simulations))
    plt.show()

if __name__ == '__main__':
    main()
