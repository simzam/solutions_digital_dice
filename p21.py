"""
Problem 21: Chain Reactions, Branching Processes, and Baby Boys


"""
import random


def experiment(probs, stop_gen=10):
    male_descendants = []
    for idx_generations in range(stop_gen):
        if len(male_descendants) == 0:
            sons = generate_sons(probs)
        else:
            sons = 0
            for _ in range(male_descendants[idx_generations - 1]):
                sons += generate_sons(probs)
        if sons == 0:
            break
        male_descendants.append(sons)
    return male_descendants


def generate_sons(sons_prob):
    draw_sons = random.random()
    num_sons = 0
    for prob in sons_prob:
        if draw_sons < prob:
            break
        num_sons += 1
    return num_sons


def generate_sons_probs(max_sons):
    """ generates the probabiliies for a man to have 0 to "max_sons".
    Note "sum(son_probs) != 1". """
    sons_probs = [0.4825]
    for i in range(max_sons):
        sons_probs.append(sons_probs[-1] + (0.2126)*(0.5893)**i)

    return sons_probs


def add_lists(lst1, lst2):
    retlst = []
    for elem1, elem2 in zip(lst1, lst2):
        retlst.append(elem1 + elem2)
    if len(lst1) > len(lst2):
        return retlst + lst1[len(lst2):]
    else:
        return retlst + lst2[len(lst1):]


def main():
    simulations = 1000
    max_sons = 7
    probs = generate_sons_probs(max_sons)
    total_sons = []
    for i in range(simulations):
        # print(len(total_sons))
        male_offspring = experiment(probs)
        if len(male_offspring) == 0:
            continue
        #print(i, male_offspring, total_sons)
        tmp_sons = [elem_prev + elem for elem_prev,
                    elem in zip(total_sons, male_offspring)]
        if len(male_offspring) > len(total_sons):
            total_sons = tmp_sons + male_offspring[len(total_sons):]
        else:
            total_sons = tmp_sons + total_sons[len(male_offspring):]
    return list(map(lambda x: x/simulations, total_sons))


if __name__ == '__main__':
    print(main())
