from view import ClientView, BillView
from controller import ClientController, Rent, BillController
from model import Client
import json
from os import path
import sys


def login():
    reg_user = input('Are you the registered user? (yes/no)')
    if reg_user.lower() == 'yes':
        return True
    else:
        return False


def file_load():
    if path.isfile('db.json') is False:
        raise Exception('File not found')
    with open("db.json", "r+") as f:
        data = json.load(f)
    return data


def check_client(user_email):

    data = file_load()

    for elem in data:
        if elem.get("Clients"):
            for index in range(len(elem.get("Clients"))):
                if elem.get("Clients")[index]["email"] == user_email:
                    return True
            return False


if __name__ == '__main__':

    client_controller = ClientController()
    rent = Rent()
    bill_controller = BillController()
    client_view = ClientView(client_controller, bill_controller, rent)

    person = login()

    if person:
        email = input('enter email')
        user_client = check_client(email)
        if user_client:
            opt = client_view.client_menu()

            # Fetch client and pass it in validate_options
            data = file_load()

            for elem in data:
                if elem.get("Clients"):
                    for index in range(len(elem.get("Clients"))):
                        if elem.get("Clients")[index]["email"] == email:
                            name = elem.get("Clients")[index]["Name"]
                            c_email = elem.get("Clients")[index]["email"]
                            address = elem.get("Clients")[index]["address"]
                            #client_object = Client(name, c_email, address)
                            client_object = client_view.validate_options(opt, Client(name, c_email, address))
                            break
                break
        else:
            print('**** Not a registered user!!! Please enter ur details to register ***')
            client_object = client_view.newuser_menu()
    else:
        like_to_reg = input('Would you like to become an user?')
        if like_to_reg.lower() == 'yes':
            client_object = client_view.newuser_menu()
        else:
            like_to_partner = input('Have Bike? Would you like to become a partner?')
            if like_to_partner == 'yes':
                pass
            else:
                sys.exit()

 # for user in range(len(users)):
        #     print(user) # index value
        #     if users[user]["Clients"][user]["email"] == email:
