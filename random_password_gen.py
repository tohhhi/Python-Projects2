import random
import string

# Ask user if they want to generate a password or not
# If yes, ask for password lenght
# Generate password
# Print password
# if initial response is no, exit program



def generate_password():

    ask_user = input("Do you want to generate a password or not? ").lower()

    if ask_user == "yes":
        
        
        password_lenght = int(input("What lenght do you want your password to be? "))
        
        password_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=password_lenght))
       

        print(password_gen)
    else:
        print("Ok, your choice.")


generate_password()