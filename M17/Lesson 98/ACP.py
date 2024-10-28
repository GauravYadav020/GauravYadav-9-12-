import random


Dependence= "We pick out two cards from a standard deck of 52 cards without replacement. Event A is that we pick an Ace on the first draw. Event B is that we pick an Ace on the second draw."
#it is dependent 

mutually_exclusive= "Suppose we flip a coin ten times. Event A is that we flip all heads on the first five flips. Event B is that we flip all heads on the second five flips." 

#mutually exclusive

notmutuallyexclusive= "We roll a dice once. Event A is rolling an odd number. Event B is rolling a number greater than four."

#notmutuallyexclusive

indipendent = "We have a bag of five marbles: three are green and two are blue. Suppose that we pick one marble from the bag. Event A is that the marble is green. Event B is that the marble is blue."
#not dependence

event_lst = [Dependence, mutually_exclusive,notmutuallyexclusive,indipendent]

def guess_the_type(event):
  
    print(
        "Guess whether this is a \n 1)dependent \n 2)independent \n 3)mutually exclusive \n 4)not mutually exclusive event \n"
    )
    print(event)
    answer = int(input("Enter your answer : "))
    if event == Dependence:
        if answer == 1:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == mutually_exclusive:
        if answer == 3:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == notmutuallyexclusive:
        if answer == 4:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == indipendent:
        if answer == 2:
            print("\n You guessed it right! \n \n \n")
            return 'correct'

        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
firstanswer=guess_the_type(Dependence)
secondanswer=guess_the_type(mutually_exclusive)
thirdanswer=guess_the_type(notmutuallyexclusive)
fourthanswer=guess_the_type(indipendent)
if firstanswer=='correct' and secondanswer=='correct' and thirdanswer=='correct' and fourthanswer=='correct':
      print("\n \n \n You have guessed all the events correctly! Here's some cookies: 🍪🍪🍪 \n \n \n")