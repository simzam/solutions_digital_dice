"""
Problem 21: Chain Reactions, Branching Processes, and Baby Boys


"""
import random


def simulate():
    random.random()


def generate_sons(max_sons):
    """ generates the probabiliies for a man to have 0 to "max_sons".
    Note "sum(son_probs) != 1". """
    sons_probs = [0.4825]
    for i in range(max_sons):
        sons_probs.append(sons_probs[-1] + (0.2126)*(0.5893)**i)

    return sons_probs


def main():
    max_sons = 7
    print(generate_sons(max_sons), sum(generate_sons(max_sons)))


if __name__ == '__main__':
    main()
