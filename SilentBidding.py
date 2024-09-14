import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

flag = True
bidders_data = {}
while flag:
    bidder_name = input("Enter your name :")
    bidding_amount = float(input("Enter the bidding amount :"))
    is_there_more = input("Is there anyine left :")

    bidders_data[bidder_name] = bidding_amount

    clear_console()

    if is_there_more.lower() not in ["y","yes"]:
        max = 0
        for key in bidders_data:
            if bidders_data[key] > max:
                max = bidders_data[key]
            else:
                continue

        for key in bidders_data:
            if bidders_data[key] == max:
                print(f"The winner is {key}")
        flag = False
        

        