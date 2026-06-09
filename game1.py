import random

choices = ["stone", "paper", "scissor"]

while True:

    userInput = input("Enter your choice (stone, paper, scissor): ").lower()
    computerChoice = random.choice(choices)

    print(f"Computer chose: {computerChoice}")
    print(f"You chose: {userInput}")

    if userInput == computerChoice:
        print("It's a tie!")

    elif (userInput == "stone" and computerChoice == "scissor") or \
        (userInput == "paper" and computerChoice == "stone") or \
        (userInput == "scissor" and computerChoice == "paper"):
        print("You win!")
    else:
        print("Computer wins!") 
        
    playAgain = input("Do you want to play again? (yes/no): ").lower()
    if playAgain != "yes":
        print("Thanks for playing!")
        break