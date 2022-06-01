import sys

from rent import PartnerManagement
from rent import ClientManagement
from rent import RentManagement


def main_menu():
    print("1. Rent a Bike")
    print("2. Return a Bike")
    print("3. List Bikes")
    print("4. List Bills")
    print("5. Incoming Report")
    print("0. Exit")
    opt = int(input("Type an option >> "))
    return opt


if __name__ == '__main__':
    option = -1
    print('Welcome to Rent a Rusty Bicycle Portal')
    person1 = input('Are you already a partner(yes/no)?')
    if person1.lower() == 'yes':
        option = main_menu()
    elif person1.lower() == 'no':
        category = input('Would you like to become a partner(yes/no)?')
        if category.lower() == 'yes':
            name = input('Enter your name')
            address = input('Enter your address')
            num_of_bikes = int(input('Enter number of bikes u have'))

            partners_management = PartnerManagement(name, address, num_of_bikes)
            partners_management.add_partner()
            #main_menu()

        elif category.lower() == 'no':
            category2 = input('Would you like to rent a bike(yes/no)?')
            if category2.lower() == 'yes':
                name = input('Enter your name')
                address = input('Enter your address')
                clients_management = ClientManagement(name, address)
                clients_management.add_client()
                #option = main_menu()
    #partners_management = PartnerManagement(name, address, num_of_bikes)
    rent_management = RentManagement()
    option = main_menu()
    while option != 0:

        if option == 1:
            rent_management.rent()
            option = main_menu()
        elif option == 2:
            rent_management.return_bycicle()
            option = main_menu()
        elif option == 3:
            #rent_management.bycicles_list()
            print(rent_management.bycicles_list())
            option = main_menu()
        elif option == 4:
            #rent_management.bycicles_list()
            print(rent_management.bills_list())
            option = main_menu()
        elif option == 5:
            rent_management.report()
            print(rent_management.report())
    else:
            sys.exit()
