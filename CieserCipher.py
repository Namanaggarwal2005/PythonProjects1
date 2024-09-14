array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice = input("Do you want to encode or decode ? ").lower()
user_message =input("Enter your message ").lower()
user_key = int(input("Enter key "))

def ceasar(user_message, user_key, direction):
    output_string = ""
    if direction == "encode":
        for i in range(0,len(user_message)):
            if(user_message[i] not in array):
                output_string += user_message[i]
            else:    
                index = array.index(user_message[i])
                index = (index + user_key) % 26
                output_string += array[index]

        print(f"Encrypter text is : {output_string}")

    elif direction == "decode":
        for i in range(0,len(user_message)):
            if(user_message[i] not in array):
                output_string += user_message[i]
            else:    
                index = array.index(user_message[i])
                index = (index - user_key + 26) % 26
                output_string += array[index]
        print(f"Decoded text is : {output_string}")  

    else:
        print("Check your choice..")

ceasar(user_message,user_key,user_choice)        

continue_or_not = input("Do you want to continue ? ")


while continue_or_not.lower() in ['y',"yes"]:
    user_choice = input("Do you want to encode or decode ? ").lower()
    user_message =input("Enter your message ").lower()
    user_key = int(input("Enter key "))
    
    ceasar(user_message,user_key,user_choice)

    continue_or_not = input("Do you want to continue ? ")


            

