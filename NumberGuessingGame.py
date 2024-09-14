import random

print("Welcome to number guessing game ")
print("I am thinking of a number between 1 and 100 ")
difficulty_level = input("Choose difficulty level easy or hard :")

random_number = random.randint(1,100)

print(f"The number is {random_number}")


if difficulty_level.lower() == "easy":
    lives = 10
elif difficulty_level.lower() == "hard":
    lives = 5 

flag = True

while flag:
    user_guess = int(input("Guess a number :"))
    try:
        if user_guess > random_number:
            print("Too large guess")
            lives -= 1
        elif user_guess < random_number:
            print("Too small number")
            lives -= 1
        else:
            print(f"You have won with {lives} lives left")

        if lives == 0:
            print("Out of lives")
            flag = False
            user_choice = input("Do you want to continue ?")
            if user_choice.lower() not in ['y',"yes"]:
                flag = False
                difficulty_level = input("Choose difficulty level again :")
                if difficulty_level.lower() == "easy":
                    lives = 10
                elif difficulty_level.lower() == "hard":
                    lives = 5
    
    except ValueError:
        print("Enter valid guess ")           


