"""
solution of exercise #4 in "Digital Dice" by Nahin
"""
import random
import time
# import unittests


class CoinFlippingGame():
    def __init__(self, l, m, n, p):
        self.l = l
        self.m = m
        self.n = n
        self.p = p

        self.backup = [l, m, n]
        self.returns = [0, 0, 0]
        self.num_of_games = 0

    def above_zero(self):
        if self.l == 0:
            return False
        elif self.m == 0:
            return False
        elif self.n == 0:
            return False
        else:
            return True

    def flip_coin(self):
        """
        flips coing according to probaility
        HEADS represented by 0
        TAILS represented by 1
        """
        flip = random.random()
        # print(flip)
        if flip <= self.p:
            return 0
        else:
            return 1

    # TODO let me unit test this function
    # order here is given for the three players [l, m, n]
    def calculate_returns(self, coin_flips):
        if coin_flips[0] == coin_flips[1]:
            if coin_flips[1] == coin_flips[2]:
                self.returns = [0, 0, 0]
            else:
                self.returns = [-1, -1, 2]
        else:
            if coin_flips[0] == coin_flips[2]:
                self.returns = [-1, 2, -1]
            else:
                self.returns = [2, -1, -1]

    def coin_flip_till_ruin(self):
        while self.above_zero():
            coin_flips = [self.flip_coin(), self.flip_coin(), self.flip_coin()]
            # print(coin_flips)
            self.calculate_returns(coin_flips)
            # print(self.returns)
            # if self.returns[0] != 0:
            self.book_keeping()
            self.num_of_games += 1

    def reset(self):
        self.l = self.backup[0]
        self.m = self.backup[1]
        self.n = self.backup[2]
        self.num_of_games = 0
        self.returns = 0

    # notice how easy it would be to figure out the bug if unit tested. 
    def book_keeping(self):
        self.l += self.returns[0]
        self.m += self.returns[1]
        self.n += self.returns[2]

        # print(self.l, self.m, self.n)

if __name__ == '__main__':
    num_of_sims = 100000
    l = 1
    m = 2
    n = 3
    p = 0.4
    counter = 0
    game = CoinFlippingGame(l, m, n, p)
    for i in range(num_of_sims):
        game.coin_flip_till_ruin()
        counter += game.num_of_games
        game.reset()
        time.sleep(0.0001)
    print(counter / num_of_sims)
