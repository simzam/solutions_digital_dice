"""
Problem 21: Chain Reactions, Branching Processes, and Baby Boys


Does not actually solve problenm 21.
"""
import random


def experiment(reg, probs):
    prev_gen_sons = 1
    for i, generation in enumerate(reg):
        next_gen_sons = 0
        for _ in range(prev_gen_sons):
            tmp = generate_sons(probs)
            next_gen_sons += tmp
            generation[tmp] += 1
            reg[i] = generation
        if next_gen_sons == 0:
            return
        prev_gen_sons = next_gen_sons


def generate_sons(sons_prob):
    draw_sons = random.random()
    num_sons = 0
    for prob in sons_prob:
        if draw_sons < prob:
            break
        num_sons += 1
    return num_sons % 3


def generate_sons_probs(max_sons):
    """Generates the probabiliies for a man to have 0 to "max_sons".
    Note "sum(son_probs) != 1". """
    sons_probs = [0.4825]
    for i in range(max_sons):
        sons_probs.append(sons_probs[-1] + (0.2126)*(0.5893)**i)

    return sons_probs


def setup_register(generations, max_num_sons=7):
    """Create a list of dicts. """
    reg = [{i: 0 for i in range(max_num_sons)} for _ in range(generations)]

    return reg


def main():
    simulations = 100000

    max_generations = 10
    max_sons = 7

    probs = generate_sons_probs(max_sons)
    register = setup_register(max_generations, max_sons)

    for i in range(simulations):
        experiment(register, probs)
    return register


if __name__ == '__main__':
    print(main())
