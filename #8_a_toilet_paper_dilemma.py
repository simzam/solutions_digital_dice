import random
import matplotlib.pyplot as plt

def little_chooser(rolls):
    if rolls[0] < rolls[1]:
        rolls[0] -= 1
    else:
        rolls[1] -= 1

    return rolls


def big_chooser(rolls):
    if rolls[0] < rolls[1]:
        rolls[1] -= 1
    else:
        rolls[0] -= 1

    return rolls


def draw_sheets(rolls, p):
    while min(rolls) > 0:
        if rolls[0] == rolls[1]:
            rolls[1] -= 1
            continue

        make_choice = random.random()
        if make_choice < p:
            rolls = big_chooser(rolls)
        else:
            rolls = little_chooser(rolls)

    return max(rolls)    


def toilet_paper_simulation(num_sheets, probabilities, num_simulations):
    toilet_paper_probs = []
    sheets = [num_sheets, num_sheets]
    for prob in probs:
        left = 0
        for i in range(num_simulations):
            sheets = [num_sheets, num_sheets]
            print(rolls, sheets)
            left += draw_sheets(sheets, prob)
        toilet_paper_probs.append(left / num_simulations)

    return toilet_paper_probs

        
if __name__ == '__main__':
    rolls = [200, 200]

    probs = [i/100 for i in range(100)]
    
    sims = 1000
    
    paper_left = toilet_paper_simulation(rolls, probs, sims)

    plt.plot(probs, paper_left)
    plt.xlabel('probability for choosing the longest roll')
    plt.ylabel('number of sheets left on average')
    plt.show()
