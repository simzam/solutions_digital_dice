
import random

TOTAL_SENATORS = 100

def decide_bill_outcome(num_senators_for, missing_senators):
    num_senators_against = TOTAL_SENATORS - num_senators_for

    for _ in range(missing_senators):
        if random.random() < num_senators_for / TOTAL_SENATORS:
            num_senators_against -= 1
        else:
            num_senators_for -= 1

    if num_senators_for > num_senators_against:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sims = 100000
    count_for_bill = 0
    num_for = 49
    num_missing = 3
    for _ in range(sims):
        count_for_bill += decide_bill_outcome(num_for, num_missing)
    print(count_for_bill / sims)
