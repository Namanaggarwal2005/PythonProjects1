print("Welcome to treasure island \nYour Aim is to get to the teasure")

road_crossing = input("You are crossing a road where you want to go ? Left or Right")

if road_crossing.lower() == "left":
    next_ques = input("Do you want to swim or wait ?")
    if next_ques.lower == "swim":
        print("Game Over")
        exit()
    else:
        door_question = input("Whichj door ypu want to select Red / Blur / Yellow")    
        if door_question.lower() in ["red" , "blue"]:
            print("Game Over")
            exit() 
        else: 
            print("You Win")
            exit()    

else:
    print("Game Over")            