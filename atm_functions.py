from datastore import list_of_transactions
from datastore import user_list
import user_menu

def change_pin(user):
    current_pin = input("Enter you current four digit PIN number:\n")
    pin_changed=False
    count = 2       
    while(count != 0):
        if (user['PIN']==current_pin):
            print(" ")
            new_pin = input("Enter your new four digit PIN\n")
            while(pin_changed != True):
                if (new_pin != current_pin) and (len(new_pin) == 4) :
                    user['PIN'] = new_pin
                    pin_changed = True
                    count = 0
                    break
                else: 
                    print(" ")
                    print("Your new PIN must be different of your current pin and must contain 4 digits.")
                    new_pin=input("Enter again your new four digit PIN:\n ")
                    continue
        else:
            count -= 1
            if count == 0:
                pin_changed = False
            print(" ")    
            user_pin=input("Wrong PIN. Enter again your four digit PIN:\n  ")
            continue
          
    if (pin_changed==True):
        print(" ")
        print("PIN sucessfully changed")
        print("------------------------")
        input("Return to continue...")
    
    else:
        print(" ")
        ("Your PIN could not be changed")
        print("------------------------ ")
        input("Return to continue...")

        
    user_menu.user_menu(user)
           
    
