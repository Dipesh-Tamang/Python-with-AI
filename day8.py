"""
# Game 1
import random

number = random.randint(1, 20)
print(number)
guess = 0
limit = 5

while True:
    user_num = int(input("Enter the number: "))
    guess = guess + 1
    limit = limit - 1
    print(f"Limit remaining {limit}")
    if user_num == number:
        print(f"You guess the number {number} in {guess} try")
        break
    elif limit == 0:
        print("limit has been fulfilled")
        break
    elif user_num <= number:
        print("guess higher")
    elif user_num >= number:
        print("guess lower")
    else:
        print("try again!")


# Game 2
number = random.randint(1, 20)
print("🎯 I'm thinking of a number between 1 and 20.", number)

while True:
    user_num = int(input("\nEnter your guess: "))

    if user_num == number:
        print("🎉 Congratulations! You guessed the correct number.")
        break
    elif number < user_num:
        print("📉 Too high! Try a smaller number.")
    elif number > user_num:
        print("📈 Too low! Try a larger number.")
    else:
        print("❌ Invalid guess. Please try again.")

# Rock Paper Scissor


import random
data = ["R", "P", "S"]
count = 5
while True:
    count -= 1
    computer = random.choice(data)
    user = input("Enter (R/P/S):").upper()
    if user == computer:
        print("Draw!")
    elif (
        user == "R"
        and computer == "S"
        or user == "S"
        and computer == "P"
        or user == "P"
        and computer == "R"
    ):
        print("User Wins!")
        print(f"Computer guessed:{computer}")
    else:
        print("Computer Wins!")
        print(f"Computer guessed:{computer}")
    if count == 0:
        choice = input("Do you want to play again?(Y/N):").upper()
        if choice != "Y":
            print("Thanks for playing!")
            break
        count = 5
"""