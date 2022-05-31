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

    partners_management = PartnerManagement()
    clients_management = ClientManagement()
    rent_management = RentManagement()

    option = -1
    while option != 0:

        option = main_menu()

        if option == 1:
            rent_management.rent()
        elif option == 2:
            rent_management.return_bycicle()
        elif option == 3:
            print(rent_management.bycicles_list())
        elif option == 4:
            print(rent_management.bills_list())
        elif option == 5:
            print(rent_management.report())
