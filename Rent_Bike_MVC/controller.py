import json
import random
from os import path
from view import ClientView, BillView
from model import Bill


def data_load(self):
    if path.isfile('db.json') is False:
        raise Exception('File not found')
    with open("db.json", "r") as f:
        data = json.load(f)
    return data


class ClientController:
    def __init__(self):
        pass

    def add_client(self, client):
        print('***   Inside client controller   ***')
        data = data_load(self)
        for elem in range(len(data)):
            print(list(data[elem].keys())[elem])
            if list(data[elem].keys())[0] == "Clients":
                print(type(data[elem]["Clients"]))
                data[elem]["Clients"].append({"Name": client.name, "email": client.email, "address": client.address})
                with open("db.json", 'w') as fw:
                    json.dump(data, fw, indent=4, separators=(',', ': '))
                print('Successfully Registered')
                break
            else:
                print('User invalid')


class Rent:
    def __init__(self):
        #self.bikes_available = False
        self.bike_ID_available = False

    def rent_bike(self, client, bike_id):
        data = data_load(self)

        for elem in data:
            if elem.get("Bikes"):
                for index in range(len(elem.get("Bikes"))):
                    if elem.get("Bikes")[index]["Bike_ID"] == bike_id and elem.get("Bikes")[index]["Status"] == 'Available':
                        self.bike_ID_available = True
                        elem.get("Bikes")[index]["Status"] = "Not_Available"

        if self.bike_ID_available:
            for elem in range(len(data)):
                # print(list(data[elem].keys())[elem])
                if list(data[elem].keys())[0] == "Rent":
                    # print(client.name)
                    # list(users[user].keys()).append({client})  # To do
                    print(type(data[elem]["Rent"]))
                    data[elem]["Rent"].append({"Bill_ID": client.email, "Bike_ID": bike_id})

            with open("db.json", 'w') as fw:
                json.dump(data, fw, indent=4, separators=(',', ': '))
            print(client.email)
            return client
        else:
            print('***  Chosen bike Not_Available  ***')

    def return_bike(self, client):
        contract = False
        bike_id = int(input('Enter the bike id to return'))
        data = data_load(self)

        for elem in data:
            if elem.get("Rent"):
                for index in range(len(elem.get("Rent"))):
                    if elem.get("Rent")[index]["Bill_ID"] == client.email and elem.get("Rent")[index]["Bike_ID"] == bike_id:
                        contract = True

        if contract:
            for elem in data:
                if elem.get("Bills"):
                    for index in range(len(elem.get("Bills"))):
                        if elem.get("Bills")[index]["Bill_ID"] == client.email and elem.get("Bills")[index]["Bike_ID"] == bike_id:
                            if elem.get("Bills")[index]["Status"] == "Pending":
                                elem.get("Bills")[index]["Status"] = "Closed"
                                print('Bill Closed !!  Thanks for returning Bike!!! ')
                            else:
                                print('***  Bill already closed  ***')

            for elem in data:
                if elem.get("Bikes"):
                    for index in range(len(elem.get("Bikes"))):
                        if elem.get("Bikes")[index]["Bike_ID"] == bike_id:
                            elem.get("Bikes")[index]["Status"] = "Available"

            with open("db.json", 'w') as fw:
                json.dump(data, fw, indent=4, separators=(',', ': '))

        return client

    def list_bikes(self, client):
        bikes_available = False
        data = data_load(self)

        for elem in data:
            if elem.get("Bikes"):
                for index in range(len(elem.get("Bikes"))):
                    if elem.get("Bikes")[index]["Status"] == 'Available':
                        bikes_available = True
                        print(elem.get("Bikes")[index])

        if not bikes_available:
            print('Bikes Not_Available')
        return client

    def list_bills(self, client):
        bills_available = False
        data = data_load(self)

        for elem in data:
            if elem.get("Bills"):
                for index in range(len(elem.get("Bills"))):
                    if elem.get("Bills")[index]["Bill_ID"] == client.email:
                        bills_available = True
                        print(elem.get("Bills")[index])

        if not bills_available:
            print('Bills Not_Available')
        return client

    # def incoming_report(self, client):
    #     data = data_load(self)
    #
    #     for elem in data:
    #         if elem.get("Bills"):
    #             for index in range(len(elem.get("Bills"))):
    #                 if elem.get("Bills")[index]["Bill_ID"] == client.email:
    #                     bills_available = True
    #                     print(elem.get("Bills")[index])
    #


class BillController:

    def __init__(self):
        self.amount_per_km = 2
        self.amount_per_hour = 5
        self.amount_per_day = 20
       # self.list_of_bills = []

    def billing_by_km(self, client, km, bike_id):
        print('Calculates bill by distance travelled in km')
        amount = km * self.amount_per_km

        bill = self.bill(client, amount, bike_id)
        return bill

    def billing_by_hour(self, client, hour, bike_id):
        print('Calculates bill by hour travelled')
        amount = hour * self.amount_per_hour

        bill = self.bill(client, amount, bike_id)
        return bill

    def billing_by_days(self, client, days, bike_id):
        print('Calculates bill by hour travelled')
        amount = days * self.amount_per_day

        bill = self.bill(client, amount, bike_id)
        return bill

    def bill(self, client, amount, bike_id):
        status = "Pending"
        bill_id = client.email
        bike_id = bike_id

        bill = Bill(client, bill_id, bike_id, amount, status)

        data = data_load(self)

        for elem in range(len(data)):
            if list(data[elem].keys())[0] == "Bills":
                print(type(data[elem]["Bills"]))
                data[elem]["Bills"].append(
                    {"Bill_ID": bill.bill_id, "Bike_ID": bill.bike_id, "Status": bill.Status, "Amount": bill.Amount})

        with open("db.json", 'w') as fw:
            json.dump(data, fw, indent=4, separators=(',', ': '))
        print('Successfully Rented')

        return bill
