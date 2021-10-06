"""Problem 16

decision making organ consisting of five separate and indedenpendent
voters.  These voters will make a decision with two possible outcomes,
yes or no. This decision might be right or wrong.

The decision is made by simple majority. The decisions can either be
right or wrong.

"""
import random
from matplotlib import pyplot as plt


def make_case(p):
    if random.random() > p:
        return 0
    else:
        return 1


def evaluate_decision(votes):
    if sum(votes) >= 3:
        return 1
    return 0


def consensus(votes):
    if sum(votes) == len(votes):
        return 1, 0
    elif sum(votes) == 0:
        return 0, 1
    else:
        return 0, 0


def simulate(simulations, guilty_percentage, correct_verdicts, copy_cat_judge):
    all_rights = 0
    all_wrongs = 0

    votes = ['NaN' for _ in correct_verdicts]
    made_correct_verdict = 0

    for _ in range(simulations):
        votes = list(map(make_case, correct_verdicts))
        if copy_cat_judge:
            votes[-1] = votes[0]

        cons = consensus(votes)
        all_rights += cons[0]
        all_wrongs += cons[1]
        made_correct_verdict += evaluate_decision(votes)

    return made_correct_verdict / simulations, all_rights, all_wrongs


def main():
    percentage_correct_verdict = [0.95, 0.95, 0.9, 0.9, 0.8]
    guilty_percentages = [i/100 for i in range(100)]

    simulations = 1000
    indp_x_vals = []
    copy_x_vals = []

    ar, aw = 0, 0

    for guilty_percentage in guilty_percentages:
        indp_judge, iar, iaw = simulate(simulations,
                                        guilty_percentage,
                                        percentage_correct_verdict,
                                        False)
        copy_judge, car, caw = simulate(simulations,
                                        guilty_percentage,
                                        percentage_correct_verdict,
                                        True)
        ar += iar  # + car
        aw += iaw  # + caw

        indp_x_vals.append(indp_judge)
        copy_x_vals.append(copy_judge)
    # uncomment line below for verification of code
    # print(ar / simulations, aw / simulations)

    plt.plot(copy_x_vals, label="Judge 5 always copy judge 1")
    plt.plot(indp_x_vals, label="All judge independent")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
