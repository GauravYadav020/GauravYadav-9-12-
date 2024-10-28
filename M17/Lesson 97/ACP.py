import random

def dice_roll_experiment():
	# defining all the numbers as lists
	numbers = [1,2,3,4,5,6]

	# "flipping" coins randomly
	result = random.choice(numbers)

	#Finding the probability 
	pro = numbers.count(6)/len(numbers)
	print("Probability of getting a 6 is:", pro)

	# checking if you got a 6
	if result == 6:
		return 'Yeah, you can begin the game'
	else:
		return "Aww snap! You didn't get a 6. Please, Roll Again."
		
res = dice_roll_experiment()
print(res)	


