import random as rn
import numpy as np

N_vals = [N for N in range(4, 13)] + [20, 30]
trials = 10**4

# TODO use flag to continue
def check_mutual_pairs(elems):
    mutual_pairs = 0
    skip = 0
    for idx in range(len(elems) - 2):
        if skip == 1:
            skip = 0
            continue
        D1 = elems[idx + 1] - elems[idx]
        D2 = elems[idx + 2] - elems[idx + 1]
      #  print(idx, D1, D2)
        if D1 < D2:
            mutual_pairs += 1
            #print("pair found at idx %d" % idx)
            #print(D1, D2)
            skip = 1
        else:
            skip = 0

    D1 = elems[-2] - elems[-3]
    D2 = elems[-1] - elems[-2]
    #print(D2, D1)
    if D2 < D1:
        mutual_pairs += 1
        #print("in")
    return mutual_pairs


def car_generator(N):
    cars = [rn.random() for _ in range(N)]
    return sorted(cars)

if __name__ == "__main__":
    test_cars = [0, 0.15, 0.26, 0.27, 0.31, 0.311, 0.400001, 0.400002, 0.4000023]
    print(check_mutual_pairs(test_cars)/(len(test_cars)))
    for N in N_vals:
        sum_mutual_pairs = 0
        for _ in range(trials):
            cars = car_generator(N)
            sum_mutual_pairs += check_mutual_pairs(cars)
        #print(check_mutual_pairs(cars))
        #print(["{0:0.3f}".format(i) for i in cars])
        print("N = %d, p = %f, mutual cars: %d" % (N, sum_mutual_pairs / (N * trials), sum_mutual_pairs))
