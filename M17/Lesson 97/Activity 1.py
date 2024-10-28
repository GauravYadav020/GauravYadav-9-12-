import random

def pick_ball_experiment():
    balls = [1,2,3,4,5,6]
    result = random.choice(balls)
    pro = balls.count(6) / len(balls)
    print("Probability of picking Red Ballno 6 is:", pro)

    if result == 6:
        return ' six was picked '
    else:
        return 'Better Luck Next time'

# Corrected indentation for function call
res = pick_ball_experiment()
print(res)  # Print the result outside the function
