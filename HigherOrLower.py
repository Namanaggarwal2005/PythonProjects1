import GameData as gd
import random 
import art

LENGTH = len(gd.data)
flag = True

def selecting_random_person():
    rand_index = random.randint(0,LENGTH - 1)
    random_entity_details = gd.data[rand_index]
    return random_entity_details

print(art.logo)

while flag:
    score = 0

    first_person = selecting_random_person()
    print(f"Compare A: {first_person['name']} , a {first_person['description']} , from {first_person['country']}")

    print(art.vs)

    second_person = selecting_random_person()
    print(f"Against B: {second_person['name']} , a {second_person['description']} , from {second_person['country']}")

    user_guess = input("Guess who have more followers :")

    if first_person["follower_count"] > second_person["follower_count"]:
        answer = 'a'
    else:
        answer = 'b'   

    if user_guess.lower() == answer:
        print("Correct !")
        score += 1
    
    else :
        print("Wrong !")
        print(f"Your score was {score}")
        
        user_choice = input("Do you want to continue playing ? ")
        if user_choice.lower() not in ['y',"yes"]:
            flag = False        

    


