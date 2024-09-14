from art import logo_coffee_machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

reports = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

print(logo_coffee_machine)

flag = True

def checking_resourses(user_choice,MENU,reports):
    for key in MENU[user_choice]["ingredients"]:
        if reports[key] >= MENU[user_choice]["ingredients"][key]:
            reports[key] = reports[key] - MENU[user_choice]["ingredients"][key]
            return "Here is your coffee enjoy !!"
        else:
            return f"Not enough {key}"

def total_money_calculator(quarter,dime,nickel,penny):
    money = 0
    for key in COIN_VALUES:
        if key == 'quarter':
            money += quarter * COIN_VALUES[key]
        elif key == 'dime':
            money += dime * COIN_VALUES[key]
        elif key == 'nickel':
            money += nickel* COIN_VALUES[key]
        elif key == 'penny':
            money += penny * COIN_VALUES[key]
        else:
            money += 0
    return money


def money_checker(total_money,MENU,user_choice,reports):
    if total_money >= MENU[user_choice]["cost"] :
        reports["money"] += total_money
        return checking_resourses(user_choice,MENU,reports) +f"\n Here is the left over money ${total_money - MENU[user_choice]["cost"]}"
    else:
        return f"Not enough money inserted !! Here is your money ${total_money}"


     
while flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    
    if user_choice.lower() in ["espresso","latte","cappuccino"]:
        quarter = int(input("Enter quaters :"))
        dime = int(input("Enter dimes :"))
        nickel = int(input("Enter nikels :"))
        penny = int(input("Enter pennies :"))

        total_money = total_money_calculator(quarter,dime,nickel,penny)
        total_money = round(total_money,2)
        print(money_checker(total_money,MENU,user_choice,reports))
        flag = True
    
    elif user_choice.lower() == "report":
        print(f"Water : {reports['water']}ml \nMilk : {reports['milk']}ml \nCoffee : {reports['coffee']}g \nMoney : ${reports['money']}")
        flag = True
    
    elif user_choice.lower() == "off":
        flag = False    

    else:
        flag = False    
   
