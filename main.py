import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = random.randint(0,2)

user_choice = (input("What do you choose? rock,paper or scissors?")).lower()

computer_choice = "hello"

if (choice == 0): 
  computer_choice = "rock"

elif (choice == 1):
  computer_choice = "paper"

else:
  computer_choice = "scissors"

if(computer_choice == user_choice): 
  print("Its a Tie...Try again...")

elif(computer_choice=="rock" and user_choice=="paper"):
  print("You choose")
  print(paper)
  print("computer choose")
  print(rock)
  print("You won!")

elif(computer_choice=="rock" and user_choice=="scissor"):
  print("You choose")
  print(scissors)
  print("computer choose")
  print(rock)
  print("Computer won!")

elif(computer_choice=="paper" and user_choice=="scissor"):
  print("You choose")
  print(scissors)
  print("computer choose")
  print(paper)
  print("You won!")

elif(computer_choice=="paper" and user_choice=="rock"):
  print("You choose")
  print(rock)
  print("computer choose")
  print(paper)
  print("Computer won!")

elif(computer_choice=="scissor" and user_choice=="rock"):
  print("You choose")
  print(rock)
  print("computer choose")
  print(scissors)
  print("You won!")

elif(computer_choice=="scissor" and user_choice=="paper"):
  print("You choose")
  print(paper)
  print("computer choose")
  print(scissors)
  print("Computer won!")
else:
  print("Input is incorrect")
