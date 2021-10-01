import random as rn


def vote(N, n):
    voters = [i for i in range(N)]
    candidates = voters[:n]
    votes = dict()
    for voter in voters:
        vote = rn.choice(candidates)
        try:
            votes[vote] += 1
        except KeyError:
            votes[vote] = 1
    return votes


def decide_election(N, M, n):
    votes = vote(N, n)
    for vals in votes.values():
        if vals >= M:
            return 1
    return 0


def simulate(N, M, ns, sims):
    retval = "N = {}, M = {}, n = {}, % at first vote {}"
    for n in ns:
        count = 0
        for _ in range(sims):
            count += decide_election(N, M, n)
        print(retval.format(N, M, n, count / sims))


def main():
    n = [2, 3, 4]
    simulations = 10000

    N = 25
    M = 17
    simulate(N, M, n, simulations)

    N = 7
    M = 4
    simulate(N, M, n, simulations)


if __name__ == '__main__':
    main()
