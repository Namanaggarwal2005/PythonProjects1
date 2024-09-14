import random

word_list = ["camel","baboon","aardvark"]
lives = 6
score = 0
 
random_index = random.randint(0,2)
choosen_word = word_list[random_index]
placeholder = ""
for letter in choosen_word:
    placeholder += "_"
print(choosen_word)
print(placeholder)    
correct_letters =[]
game_over = False

while not game_over:
    display = ""
    guess = input("Guess a letter :")
    guess = guess.lower()

    print(f"You have {lives} live(s) left.")
    


    for letter in choosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
            score +=1
        elif letter in correct_letters:
            display += letter    
        else:
            display += "_"

    print(display)   
    if guess not in choosen_word:
        lives -= 1
        score -= 1  

    print(f"Your score is {score}")       


    if "_" not in display:
        game_over = True
        print("You Win")     

    if lives == 0 or score == -1:
        game_over = True
        print("You loose")       

  




    
