import os
from datastore import user_list
from datastore import list_of_transactions
from atm_functions import change_pin


def clear_screen():
    os.system('cls')

def user_menu(user):
    clear_screen()
    print('================================')
    print(f"Hello {user['NAME']}, Menu options:")
    print("1. Change Pin")
    print("2. Withdrawal")
    print("3. Lodgement")
    print("4. View last 10 days statement")
    print("5. Exit\n")
    
    choice= input("Please choose an option (1-5): \n")

    clear_screen()
    if(choice == "1"):
        print("You selected Change Pin!\n")
        change_pin(user)
        user_menu(user)
    elif(choice == "2"):
        print("You selected Option two!\n")
        #see_list_of_books.printbook_list()
        input("Return to continue...")
        user_menu(user)
        
    elif(choice == "3"):
        print("You selected Option three!\n")
        input("Return to continue...")
        user_menu(user)
            
    elif(choice == "4"):
        print("You selected Option four!\n")
        input("Return to continue...")
        user_menu(user)
               
    elif(choice == "5"):
        print("Bye!")

    else:
        print("Please return to menu and select a digit from 1 to 5")
        input("Return to continue...")
        user_menu(user)

