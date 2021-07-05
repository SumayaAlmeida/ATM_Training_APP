import os
from datastore import user_list
from datastore import list_of_transactions
from user_menu import user_menu


active_user=""
count=len(user_list)

def clear_screen():
    os.system('cls')
   
def login_menu():
    clear_screen()
    print("============================")
    print(" ")
    print("WELCOME TO ATM TRAINING APP")
    print(" ")
    print("============================")
    
    
    print("Menu Options")
    print(" 1:  User Login")
    print(" 2:  Quit")
    choice=(input("Enter your choice:  "))
    if(choice=="1"):
      user_login()
    elif(choice=="2"):
        print("Thanks for visiting ATM TRAINING APP")
        exit()
    else:
        answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
        answer=answer.upper()
        if (answer=="Y"):
          login_menu()
        else:
           exit()


def user_login():
    found=None
    count = 2
    user_id=input("Enter Your UserID:  ")
    user_pin = None
    for user in user_list:
        if (user['USERID']==user_id):
           user_pin=input("Enter your four digit PIN:  ")
           while(count != 0):
            if (user['PIN']==user_pin):
                
                    found=True
                    global active_user
                    active_user=user
                    break
            else:
                    count -= 1
                    if count == 0:
                        found = False
                    user_pin=input("Wrong PIN. Enter again your four digit PIN:  ") 
                    continue
                             

    if (found==True):
        print("Login Sucessful")
        user_menu(active_user)
    
    elif(found == None):  
            answer = input("Login Unsusessful. Would you like to try again?  [Y/N]")
            answer=answer.upper()
            if (answer=="Y"):
                login_menu()
            else:
                exit()
    
    elif(found==False):
        print("Login Unsuccessful. Your Account is now blocked. Please, go to your branch ASAP ")
        exit()


        
login_menu()