import random
import os

cards_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def card_selection(list):
    rand_index1 = random.randint(0,len(cards_list)-1)
    rand_index2 = random.randint(0,len(cards_list)-1)

    list.append(cards_list[rand_index1])
    list.append(cards_list[rand_index2])

    return list

def total_calculator(list):
    total = 0
    for i in list:
        total += i
    return total    

user_choice_to_play = input("Do you want to play the game of blackjack? Click 'y' or 'n' ")   

while user_choice_to_play == 'y':

    user_list = []
    dealer_list = []

    user_cards1 = card_selection(user_list)   
    dealer_cards = card_selection(dealer_list)
    score_user = 0
    score_dealer = 0
    

    print(f"Your cards :{user_cards1}")
    
    score_user =  total_calculator(user_cards1)
    print(f"Your score is  :{score_user}")   
    print(f"Computer's first card is :{dealer_cards[0]}")

    user_choice2 = input("Type 'y' to get another card, type 'n' to pass: ")

    if user_choice2 == 'y':
        user_list.append(cards_list[random.randint(0,len(cards_list)-1)])

    
    score_user = total_calculator(user_cards1)
    print(f"Your score is  :{score_user}")
    
    
    score_dealer = total_calculator(dealer_cards)
    print(f"Computer's second card was {dealer_cards[1]}")  
    print(f"Computer's score is {score_dealer}")

    if(score_user > 21):
        print("You Loose!")
    elif(score_dealer > 21):
        print("You Won !!")     
    elif(score_user > score_dealer):
        print("You Won !!")
    elif(score_user < score_dealer):
        print("You Loose !")    
    else:
        print("Draw !")    

        

    user_choice_to_play = input("Do you want to play another game of blackjack? Click 'y' or 'n' ")
    score_user = 0
    score_dealer = 0

    clear_console()   




