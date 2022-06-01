import db
from db import clients, partners


class ClientManagement:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.num_of_bikes_rented = 0
        self.list_of_clients = []

    def add_client(self):
        self.list_of_clients.append({'Name': self.name, 'Address': self.address})
        db.clients.append(self)  # To be implemented
        print(self.list_of_clients)
        #print(str(self))
        # obj = ClientManagement(self.name, self.address)
        # with open('db.py', 'r+') as file:
        #     print('File opened')
        #     file.write(str(clients.append(obj)))
        #     print(file.read())
        #     file.close()


class PartnerManagement:
    def __init__(self, name, address, num_of_bikes):
        self.name = name
        self.address = address
        self.num_of_bikes = num_of_bikes
        self.list_of_partners = []

    def add_partner(self):
        self.list_of_partners.append(self.name)
        db.clients.append(self)  # To be implemented
        print(self.list_of_partners)
       #  with open('db.py', 'r+') as file:
       #      print('File opened')
       #      #print(self)
       #      file.write(str(partners.append(self)))
       #      print(file.read())
       #      file.close()
       # # partners.append(self)


class RentManagement(PartnerManagement, ClientManagement):

    def __init__(self):

        self.amount_to_be_paid = 0
        self.list_of_bills = []
        self.Bike_status = None
        self.Bill_status = None
        self.new_id = 0
        self.bike_id = []

    def main_menu(self):
        print("1. choose by age")
        print("2. choose by manufacturer")
        print("3. choose by type")
        print("0. Exit")
        opt = int(input("Type an option >> "))
        return opt

    def sub_menu(self):
        #option = -1
        print("1. Rent by km")
        print("2. Rent by days")
        print("3. Rent by hours")
        print("0. Exit")
        option = int(input('Enter the option'))
        while option != -1:
            if option == 1:
                print('Calculates bill by km')
                num_of_km = float(input('Enter number of kms to drive'))
                bill = GenerateBill_by_KM(num_of_km)
                self.amount_to_be_paid = bill.generate_bill()
                self.new_id = self.new_id + 1
                self.list_of_bills.append({self.new_id: self.amount_to_be_paid})  # Key to be implemented
                self.Bill_status = 'Pending'  # To be implemented in DB
                self.Bike_status = 'Not Available'  # To be implemented in DB

                print(f'Amount: {self.amount_to_be_paid}, Bill Status:{self.Bill_status}')

                #print(self.list_of_bills)
            elif option == 2:
                print('Calculates bill by days')
                num_of_days = int(input('Enter number of days to rent'))
                bill = GenerateBill_by_Days(num_of_days)
                self.amount_to_be_paid = bill.generate_bill()
                self.new_id = self.new_id + 1
                self.list_of_bills.append({self.new_id: self.amount_to_be_paid})
                #self.list_of_bills.append({'Amount': self.amount_to_be_paid})  # Key to be implemented
                self.Bill_status = 'Pending'  # To be implemented in DB
                self.Bike_status = 'Not Available'  # To be implemented in DB
                print(f'Amount: {self.amount_to_be_paid}, Bill Status:{self.Bill_status}')

            elif option == 3:
                print('Calculates bill by hour')
                num_of_hours = int(input('Enter number of hours to rent'))
                bill = GenerateBill_by_hours(num_of_hours)
                self.amount_to_be_paid = bill.generate_bill()
                self.new_id = self.new_id + 1
                self.list_of_bills.append({self.new_id: self.amount_to_be_paid})
                #self.list_of_bills.append({'Amount': self.amount_to_be_paid})
                self.Bill_status = 'Pending'  # To be implemented in DB
                self.Bike_status = 'Not Available'  # To be implemented in DB
                print(f'Amount: {self.amount_to_be_paid}, Bill Status:{self.Bill_status}')

            return

    def rent(self):
        option = self.main_menu()
        if option == 1:
            print('Bike chosen by age ')
            self.sub_menu()
        elif option == 2:
            print('Bike chosen by manufacturer ')
            self.sub_menu()
        elif option == 3:
            print('Bike chosen by type ')
            self.sub_menu()
        return

    def return_bycicle(self):
        count = 0
        bid = int(input('Enter the bike_id to be returned'))
        for i in range(len(self.list_of_bills)):
            print(list(self.list_of_bills[i-1].keys())[i-1])
            if bid == list(self.list_of_bills[i-1].keys())[i-1]:
                self.Bill_status = 'Closed'
                self.Bike_status = 'Available'
                #count = 1
                #self.list_of_bills[i].remove(bid)
        #if count == 1:

        print('Bicycle returned')
        print(f'Bill status: {self.Bill_status}')
        print(f'**** Bike {bid} {self.Bike_status} to rent ***\n')

    def bycicles_list(self):
        for bikes in db.Bikes:
            print(bikes)

    def bills_list(self):
        print(f'List of bills\n')
        for i in range(len(self.list_of_bills)):
            return self.list_of_bills

    def report(self):
        pass


class GenerateBill_by_KM:

    def __init__(self, km):
        self.amount_per_km = 10
        self.num_of_km = km
        self.amount = 0

    def generate_bill(self):
        self.amount = self.amount_per_km * self.num_of_km
        return self.amount


class GenerateBill_by_Days:
    def __init__(self, days):
        self.amount_per_day = 100
        self.num_of_days = days
        self.amount = 0

    def generate_bill(self):
        self.amount = self.amount_per_day * self.num_of_days
        return self.amount


class GenerateBill_by_hours:
    def __init__(self, hours):
        self.amount_per_hour = 20
        self.num_of_hours = hours
        self.amount = 0

    def generate_bill(self):
        self.amount = self.amount_per_hour * self.num_of_hours
        return self.amount
