import random
import time
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

game_images = [rock, paper, scissors] #list of choice
user_score = 0 
computer_score = 0 
play_again = 1 #variable to allow user to play the game again

#loop to play the game over again
while play_again == 1:
    user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. What do you choose?\n"))
    print(game_images[user_choice]) #displaying the choice user chose
    print("Drums rolling . . . . . . . . ")
    computer_choice = random.randint(0, 2)
    time.sleep(2) #sleeping the program to make the user anticipate
    print("Computer chose:")
    print(game_images[computer_choice]) #displaying the choice of computer

    #logic for the game 
    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
        computer_score+=1
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        user_score+=1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        computer_score+=1
    elif computer_choice > user_choice:
        print("You lose")
        computer_score+=1
    elif user_choice > computer_choice:
        print("You win!")
        user_score+=1
    elif computer_choice == user_choice:
        print("It's a draw")
    #prompt to play again
    play_again = int(input("Do you want to play another round? Type 1 for Yes , 0 for No. \n"))

#print the final score of the game
print(f"The final scoreboard:\nYour Score : {user_score}\nComputer Score: {computer_score}")

