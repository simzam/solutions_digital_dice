"""problem 19: Electing Emperor and Popes

When the cardinals elect a new pope, the all have one vote and they
can only vote on the cardinals. In reality there are probably a
limited number of acceptable candidates. They all vote and if no
cardinal received enough votes to declare a winner, they all vote again.

This simulation explores the probability for winning a vote in a given
round. And how much changes if we refuse or let the candidates vote
for themselves.

1) N: the number of voters.
2) M: the number of votes necessary to win.
3) n: the size of the set voteable candidates.

"""
import random as rn


def vote(N, n, self_vote=True):
    voters = [i for i in range(N)]
    candidates = voters[:n]
    votes = dict()
    for voter in voters:
        vote = rn.choice(candidates)
        if not self_vote:
            while vote == voter:
                vote = rn.choice
        try:
            votes[vote] += 1
        except KeyError:
            votes[vote] = 1
    return votes


def decide_election(N, M, n, self_vote):
    votes = vote(N, n, self_vote)
    for vals in votes.values():
        if vals >= M:
            return 1
    return 0


def simulate(N, M, ns, sims, self_vote=True):
    retval = "N = {:2}, M = {:2}, n = {}, % at first vote {:f}"
    for n in ns:
        count = 0
        for _ in range(sims):
            count += decide_election(N, M, n, self_vote)
        print(retval.format(N, M, n, count / sims))


def main():
    n = [2, 3, 4]
    simulations = 10000

    N = 25
    M = 17
    print("NO SELF-VOTE")
    simulate(N, M, n, simulations, self_vote=False)
    print("\nSELF-VOTE")
    simulate(N, M, n, simulations, self_vote=True)

    N = 7
    M = 4
    print("\nNO SELF-VOTE")
    simulate(N, M, n, simulations, self_vote=False)
    print("\nSELF-VOTE")
    simulate(N, M, n, simulations, self_vote=True)


if __name__ == '__main__':
    main()
