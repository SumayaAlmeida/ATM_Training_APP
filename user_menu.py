import os
from datastore import list_of_transactions
from atm_functions import change_pin, online_help
from atm_functions import withdrawal
from atm_functions import lodgement
from atm_functions import statement


def clear_screen():
    os.system('cls')

def user_menu(user):
    clear_screen()
    print('================================')
    print(f"Hello {user['NAME']}, Menu options:")
    print("1. Change Pin")
    print("2. Withdrawal")
    print("3. Lodgement")
    print("4. View last 10 transctions statement")
    print("5. Online_help")
    print("6.Exit\n")
    
    choice= input("Please choose an option (1-6): \n")

    clear_screen()
    if(choice == "1"):
        print("You selected Change Pin!\n")
        change_pin(user)
        user_menu(user)
    elif(choice == "2"):
        print("You selected Withdrawal!\n")
        withdrawal(user)
        input("Return to continue...")
        user_menu(user)
        
    elif(choice == "3"):
        print("You selected Lodgement!\n")
        lodgement(user)
        input("Return to continue...")
        user_menu(user)
            
    elif(choice == "4"):
        print("You selected Statement!\n")
        statement(user, list_of_transactions)
        input("Return to continue...")
        user_menu(user)

    elif(choice == "5"):
        print("You selected Online_Help!\n")
        online_help()
        input("Return to continue...")
        user_menu(user) 

    elif(choice == "6"):
        print("Thanks for using The Green Bank!")
        exit()

    else:
        print("Please return to menu and select a digit from 1 to 6")
        input("Return to continue...")
        user_menu(user)

