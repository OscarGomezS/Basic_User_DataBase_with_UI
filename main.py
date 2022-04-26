from userModel import UserModel
from interface import Interface

    
def manage_decision():
    n = int(input("Type Here: "))
    
    if n == 1:
        id = user1.get_id_for_next_new_user()
        create_user(id)
    elif n == 2:
        read_user()
    elif n == 3:
        update_user()
    elif n == 4:
        delete_user()
    elif n == 5:
        display_users()
    elif n == 6:
        print("Comeback soon!")
        return False
    
    final_decision = str(input("Do you want to do something else [y/N]: "))
    if final_decision == "y":
        return True
    elif final_decision == "N":
        print("Comeback soon!")
        return False
    else:
        raise ValueError("Type just [y/N], bye!")

def user_data():
    names = str(input("Type the names of the user: "))
    lastnames = str(input("Type the lastnames of the user: "))
    age = str(input("Type the age of the user: "))
    email_address = str(input("Type the email of the user: "))
    return names, lastnames, age, email_address

def create_user(id):
    print("Create new user" + "\n")
    names, lastnames, age, email_address = user_data()
    user1 = UserModel(id, names, lastnames, age, email_address)
    data_dict = user1.create_dict()
    user1.create_user(data_dict)

def read_user():
    id = int(input("Type the id of the user to Read: "))
    user1 = UserModel(id, names, lastnames, age, email_address)
    data_user = user1.read_user(id)
    print(data_user)

def update_user():
    id = int(input("Type the id of the user to Update: "))
    names, lastnames, age, email_address = user_data()
    user1 = UserModel(id, names, lastnames, age, email_address)
    print(user1.get_item_from_json(id))
    data_dict = user1.create_dict()
    user1.modify_user(id, data_dict)

def delete_user():
    id = int(input("Type the id of the user to Delete: "))
    user1.delete_user(id)

def display_users():
    users = user1.display_all_users()
    print(users)

if __name__=='__main__':
    id    = 0
    names = "Pedro Alfonso"
    lastnames = "Gomez Campos"
    age = 28
    email_address = "pedro@gmail.com"
    user1 = UserModel(id, names, lastnames, age, email_address)
    decision = True
    #user1.create_json()
    #user1.save_data(data_json)
    # data_dict = user1.create_dict()
    # user1.create_user(data_dict)
    # print(user1.get_item_from_json(2))
    # data_dict = user1.create_dict()
    # user1.modify_user(2, data_dict)
    # user1.delete_user(2)
    interface1 = Interface()
    interface1.display_welcome_message()
    interface1.display_description_message()
    while decision == True:
        decision = manage_decision()