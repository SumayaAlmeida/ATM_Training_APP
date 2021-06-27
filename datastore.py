from csv import DictReader

user_list = []

def add_users():
  
    user_list.append({"USERID": "1234", "PIN": "1100", "NAME": "JOHN MAYER", "BALANCE": 670.00, "OVERDRAFT": True})
    user_list.append({"USERID": "5678", "PIN": "3322", "NAME": "KATE WINSLET", "BALANCE": 2494.00, "OVERDRAFT": True})
    user_list.append({"USERID": "9012", "PIN": "5544", "NAME": "XAVIER RUDD", "BALANCE": 1039.00, "OVERDRAFT": False})
    user_list.append({"USERID": "3456", "PIN": "7766", "NAME": "LILI WALSH", "BALANCE": 28.00, "OVERDRAFT": False})
    user_list.append({"USERID": "7890", "PIN": "9988", "NAME": "BETH PORTER", "BALANCE": 14968.00, "OVERDRAFT": True})

add_users()

list_of_transactions = []

# read csv file as a list of dictionaries
with open('transactions.csv', 'r') as read_data:
    # pass the file to reader() to get the read_data
    dict_reader = DictReader(read_data)
    # pass to list() to get a list of Dictionaries
    list_of_transactions = list(dict_reader)
    
