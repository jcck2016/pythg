from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
rnum = randint(1,3)

# Turn that random number into the computer's RPS move
if rnum == 1:
    comp_move = "rock"
elif rnum == 2:
    comp_move = "paper"
elif rnum == 3:
    comp_move = "scissors"
          

# Ask a user to enter their move
player_move = input ("enter your move (can be either rock/paper/scissors only)")


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if player_move == "rock":
    print ("----------you picked rock----------")
    print (rock)
elif player_move == "paper":
    print ("----------you picked paper----------")
    print (paper)
elif player_move == "scissors":
    print ("----------you picked scissors----------")
    print (scissors)    
    
# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if comp_move == "rock":
    print ("----------CPU picked rock----------")
    print (rock)
elif comp_move == "paper":
    print ("----------CPU picked paper----------")
    print (paper)
elif comp_move == "scissors":
    print ("----------CPU picked scissors----------")
    print (scissors)    

# Figure out who wins and print the result!
if comp_move == player_move:
    print ("--- TIE !!! ----------------")
elif comp_move == "rock" and player_move == "paper":
    print ("----YOU WIN !!!! ---------")    
elif comp_move == "paper" and player_move == "scissors":
    print ("----YOU WIN !!!! ---------")
elif comp_move == "scissors" and player_move == "rock":
    print ("----YOU WIN !!!! ---------")
else:
    print (" ------CPU WINS !!!! -------")         