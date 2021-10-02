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


def main():
    max_sons = 7
    print(generate_sons_probs(max_sons), sum(generate_sons_probs(max_sons)))


if __name__ == '__main__':
    probs = generate_sons_probs(7)
    print(experiment(probs))
