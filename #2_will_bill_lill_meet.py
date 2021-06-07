import random as rn 

limit = 30
bill_waiting_time = 5
lill_waiting_time = 5

trial_number = 0
N = 10**5
counter_met = 0 

while trial_number < N:
    bill_appearance = limit * rn.random()
    lill_appearance = limit * rn.random()

    """
    if bill_appearance + bill_waiting_time > limit or lill_appearance + lill_waiting_time > limit:
        continue
    """
    trial_number += 1
    
    # Bill arrives first
    if bill_appearance < lill_appearance:
        if lill_appearance < bill_appearance + bill_waiting_time:
            counter_met += 1
    else:
        if bill_appearance < lill_appearance + lill_waiting_time:
            counter_met += 1

print("the probability that Bill meets Lill, %f, corresponding to the theoretical value of %f" % (counter_met / N, (2*bill_waiting_time)/(limit)))
