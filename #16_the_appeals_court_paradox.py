"""problem 16

decision making organ consisting of five separate and indedenpendent voters.
These voters will make a decision with two possible outcomes, yes or no. This
decision might be  right or wrong.

The decision is made by simple majority. The decisions can either be right or wrong.
"""
import math
import random

sims = 10000

def make_case(p):
    if random.random() < p:
        return 0
    else:
        return 1


def decide_case(case, voters):
    votes = [-1] * len(voters)
    for i,voter in enumerate(voters):
        if random.random() < voter:
            votes[i] = case
        else:
            votes[i] = (case + 1) % 2
    #print(case, votes)
    return votes
    #return 1 if sum(votes) > len(voters) / 2 else 0


def decide_case2(case, voters):
    votes = [-1] * len(voters)
    for i,voter in enumerate(voters):
        if random.random() < voter:
            votes[i] = case
        else:
            votes[i] = (case + 1) % 2
    #print(case, votes)
    votes[-1] = votes[0]
    return votes
    #return 1 if sum(votes) > len(voters) / 2 else 0


def evaluate_decision(case, votes):
    if sum(votes) == len(votes) and case == 1:
        return 1
    elif sum(votes) == 0 and case == 0:
        return 1
    else:
        return 0


def main():
    voters_hit_percentages = [0.95, 0.95, 0.9, 0.9, 0.8]
    percentages_false = [0] + [i/100 for i in range(1, 11)]
    decisions = [[-1, -1, -1] for _ in percentages_false]

    all_rights = 0
    all_wrongs = 0

    rights = 0

    for i, p in enumerate(percentages_false):
        #rights = 0
        positive_falses = 0
        false_positives = 0
        for _ in range(sims):
            case = make_case(p)
            votes = decide_case2(case, voters_hit_percentages)
            if sum(votes) > len(votes) / 2:
                decision = 1
            else:
                decision = 0
            # print(case, decision)
            if case == decision:
                rights += 1
            elif case > decision:
                false_positives +=1
            else:
                positive_falses +=1

            evaluation = evaluate_decision(case, votes)
            if evaluation == 0:
                all_wrongs += 1
            elif evaluation == 1:
                all_rights += 1
        simulation_conclusion = [rights, positive_falses, false_positives]
        decisions[i] = simulation_conclusion

    print(1 - (rights / (sims * len(percentages_false))))


if __name__ == '__main__':
    main()
