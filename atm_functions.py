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
            current_pin=input("Wrong PIN. Enter again your four digit PIN:\n  ")
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
           
def withdrawal(user):
    amount = int(float(input("Enter the amount you would like to withdrawal:\n")))
    while (amount%10 != 0):
        print('')
        print('We have available the following notes: 10, 20, 50\n')
        amount = int(float(input('Please enter an amount that is multiple of 10:\n')))
    
    if user['OVERDRAFT'] == True:
        if amount <= 400.00:
            user['BALANCE'] -= amount
            print(" ")
            print("Withdrawal authorized. Your money is being released now")
            print("------------------------")
            input("Return to continue...")
        else:
            print(" ")
            print("Withdrawal off limits")
            print("------------------------ ")
            input("Return to continue...")
    
    else:
        if amount <= user['BALANCE'] and amount <=400:
            user['BALANCE'] -= amount
            print(" ")
            print("Withdrawal authorized. Your money is being released now")
            print("------------------------")
            input("Return to continue...")
            
        else:
            print(" ")
            print("Withdrawal off limits")
            print("------------------------ ")
            input("Return to continue...")
        
        user_menu.user_menu(user)

       
def lodgement(user):
    try:
        amount = float(input("Enter the amount you would like to Lodge:\n"))
    except ValueError:
        amount = float(input('Please enter a number:\n'))

    while (not amount > 0):
        print('')
        print('Lodgement amount must be a number be greater than 0\n')
        amount = float(input('Please enter an amount:\n'))
     
    user['BALANCE'] += amount
    print(" ")
    print(f"Lodgement of {amount} in now added to you account balance.\nThank you!")
    print("------------------------")
    input("Return to continue...")

    user_menu.user_menu(user)

def statement(user, transactions):
    format_balance = "{:.2f}".format(user['BALANCE'])
    print(f"User_ID: {user['USERID']}") 
    print(f"Name: {user['NAME']}")
    print(f"Balance: {format_balance}")

    user_transactions = []

    if user['OVERDRAFT'] == True:
        print(f"Overdraft falicility: Yes")
        print("---------------------")
        print(" ")
        print("Date".ljust(15), "Transaction".ljust(15), "Amount (€)".ljust(15), "Balance (€)".ljust(20))
        print("----".ljust(15), "-----------".ljust(15), "---------".ljust(15), "----------".ljust(20))
        print(format_balance.rjust(54))
        

    else:
        print(f"Overdraft facility: No")
        print("---------------------")
        print(" ")
        print("Date".ljust(15), "Transaction".ljust(15), "Amount".ljust(15), "Balance".ljust(20))
        print("----".ljust(15), "-----------".ljust(15), "------".ljust(15), "-------".ljust(20))
        print(format_balance.rjust(54))

    for transaction in transactions:
        if transaction['USERID'] == user['USERID']:
            user_transactions.append(transaction)
            
    user_transactions.reverse()
    count = 0
    while count < 10:
        for transaction in user_transactions:
            print(f"{transaction['DATE'].ljust(15)} {transaction['TRANSACTION'].ljust(15)} {transaction['AMOUNT'].ljust(15)} {transaction['BALANCE_AFTER'].ljust(20)}")
            count += 1
           
    