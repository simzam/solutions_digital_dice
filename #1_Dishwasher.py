
import random as rand

events = 10**7
N = 5 # participants
prob_clumsy = 1/N
count_clumsy = 0
events_clumsy = 0

number_plates = 5


for _ in range(events):
    for _ in range(number_plates):
        trial = rand.random()
        if trial < prob_clumsy:
            count_clumsy += 1
    if count_clumsy >= number_plates - 1:
        events_clumsy += 1
    count_clumsy = 0
        
print(events_clumsy / events)
