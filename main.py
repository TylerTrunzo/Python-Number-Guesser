#imports the random module
import random
#imports the math module
import math
#sets the minimum random number to 0
minimum = (0)
#sets the maximum random number to 20
maximum = (20)
#defines x as a random integer between the minimum (0) and the maximum (20)
x = random.randint(minimum, maximum)
#asks for the user's name
name = input("What is your name?: ")
#asks for the users country
country= input("What country are you from?:")
#prints out a string greeting the user using their name and country
print ("Hello", name, "from", country)
#asks the user for input that is yes or no
response = input("Do you want to try a guessing game?: [yes or no]")
#uses a while loop to determine next course of action
while response != 'yes' or 'no':
  #if the answer is yes, moves on to number guessing
  if response =="yes":
    response = True
    print("Great, let's get started! Guess a number from 0-20")
    break
  #if the answer is no, ends the program and the program must run again
  elif response == "no":
    response = True
    print("Okay, see you later!")
    exit()
  #if the input is not 'yes' or 'no', then redirects the user to input one of those two choices
  else:
    response = input("Sorry, I can only read 'yes or 'no':")
 #obtain first guess from user   
guess =int(input(" What is your guess?: "))
#using another while loop to continue guessing, uses a boolean value to determine if the guess is equal to x
while guess != x:
#give user one more random guess
  guess =int(input("Sorry, try again:"))
  #congratulatory message printed for user if x (random number) matches their guess
  if x == guess:
    print("Congratulations! You guessed the correct number!")
#statement printed if guess is higher than 20
  elif guess > 20:
    print("Your guess has to be between 0 and 20:")
#statement printed if guess is lower than 0
  elif guess < 0:
    print("Your guess has to be between 0 and 20:")
  #statement printed if guess is higher than x
  elif x < guess:
    print("Your guess is too high, try again:")
  #statement printed if 
  elif x > guess:
    print("Your guess is too low, try again:")
  
