
import random
#remember that ordere matters
def less_than(nums, lim):
    count = 1
    nums = list(set(nums))
    for num in nums:
        if num < lim:
            count += 1
    return count


def main():
    num_floors = 11
    steve_floor = num_floors - 2
    max_num_riders = 15

    simulations = 100000

    avg_num_stops = []
    # steve is leaving at 15!
    for num_riders in range(max_num_riders):
        count = 0
        for _ in range(simulations):
            sim = [random.randrange(1, 12) for _ in range(num_riders)]
            count += less_than(sim, steve_floor)

        avg_num_stops.append(count / simulations)
    return avg_num_stops


def test_less_than():
    nums = [1, 1, 2, 3, 3, 3, 8]
    retval = less_than(nums, 2)
    print(retval)
    assert retval == 3

if __name__ == '__main__':
    print(main())
