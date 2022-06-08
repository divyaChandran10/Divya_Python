import sys

from model import Client, Partner, Bill, Rent
#from controller import ClientController, Rent, BillController

import json
from os import path


def data_load(self):
    if path.isfile('db.json') is False:
        raise Exception('File not found')
    with open("db.json", "r") as f:
        data = json.load(f)
    return data


class ClientView:

    def __init__(self, client_controller, bill_controller, rent):
        self.client_controller = client_controller
        self.rent = rent
        self.client = None
        self.bill_controller = bill_controller

    def client_menu(self):
        print("1. Rent a Bike")
        print("2. Return a Bike")
        print("3. List Bikes")
        print("4. List Bills")
        print("5. Incoming Report")
        print("0. Exit")
        opt = int(input("Type an option >> "))
        return opt

    def newuser_menu(self):
        name = input('enter your name')
        email = input('enter your email')
        address = input('enter your address')
        self.client = Client(name, email, address)
        self.client_controller.add_client(self.client)
        print('Details saved Successfully')
        client_option = self.client_menu()
        self.validate_options(client_option, self.client)
        return self.client

    def validate_options(self, client_option, client_object):
        bikes_available = False
        print('****   Inside validate options   ****')
        if client_option == 1:
            data = data_load(self)

            for elem in data:
                if elem.get("Bikes"):
                    for index in range(len(elem.get("Bikes"))):
                        if elem.get("Bikes")[index]["Status"] == 'Available':
                            bikes_available = True
                            print(elem.get("Bikes")[index])

            if bikes_available:
                bike_id = int(input('choose bike id'))
                rent = Rent(client_object, bike_id)
                self.rent.rent_bike(client_object, bike_id)
                bill_view = BillView(self.bill_controller, client_object, bike_id)
                bill_view.billing_method()
            else:
                print("Currently Bikes Not_Available")
            return client_object

        elif client_option == 2:

            self.rent.return_bike(client_object)
            return client_object

        elif client_option == 3:

            self.rent.list_bikes(client_object)
            return client_object

        elif client_option == 4:

            self.rent.list_bills(client_object)
            return client_object


class BillView:
    def __init__(self, bill_controller, client_object, bike_id):
        self.bill_controller = bill_controller
        self.client = client_object
        self.bike_id = bike_id
        self.bill = None

    def billing_method(self):
       # bill = Bill(self.client, bill_id= ,self.bike_id,)
        print('**  Inside Generate Bill  **')
        print("1. Rent by distance")
        print("2. Rent by hours")
        print("3. Rent by days")
        print("0. Exit")
        billing_strategy = int(input('Choose Rental type'))
        if billing_strategy == 1:
            distance_travelled_in_km = float(input('Enter the travel distance in km'))

            self.bill = self.bill_controller.billing_by_km(self.client, distance_travelled_in_km, self.bike_id)
            print(f'Rental Details: \n Bill ID: {self.bill.bill_id} \n Bike ID: {self.bill.bike_id} \n Amount to be paid: {self.bill.Amount}')

        elif billing_strategy == 2:
            hour = float(input('Enter the travel hours '))
            self.bill = self.bill_controller.billing_by_hour(self.client, hour, self.bike_id)
            print(
                f'Rental Details: \n Bill ID: {self.bill.bill_id} \n Bike ID: {self.bill.bike_id} \n Amount to be paid: {self.bill.Amount}')

        elif billing_strategy == 3:
            days = float(input('Enter the travel days '))
            self.bill = self.bill_controller.billing_by_hour(self.client, days, self.bike_id)
            print(
                f'Rental Details: \n Bill ID: {self.bill.bill_id} \n Bike ID: {self.bill.bike_id} \n Amount to be paid: {self.bill.Amount}')

        else:
            sys.exit()
