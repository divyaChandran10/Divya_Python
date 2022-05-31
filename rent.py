class ClientManagement:
    pass


class PartnerManagement:
    pass


class RentManagement(PartnerManagement, ClientManagement):
    # def __int__(self):
    #     pass
    def __init__(self):
        self.amount_to_be_paid = 0
        self.list_of_bills = []
        self.Bike_status = None
        self.Bill_status = None

    def main_menu(self):
        print("1. choose by age")
        print("2. choose by manufacturer")
        print("3. choose by type")
        print("0. Exit")
        opt = int(input("Type an option >> "))
        return opt

    def sub_menu(self):
        #option = -1
        print("1. choose by km")
        print("2. choose by days")
        print("3. choose by hour")
        print("0. Exit")
        option = int(input('Enter the option'))
        if option == 1:
            print('Calculates bill by km')
            num_of_km = float(input('Enter number of kms to drive'))
            bill = GenerateBill_by_KM(num_of_km)
            self.amount_to_be_paid = bill.generate_bill()
            self.list_of_bills.append({self: self.amount_to_be_paid})  # Key to be implemented
            self.Bill_status = 'Pending'  # To be implemented in DB
            self.Bike_status = 'Not Available'  # To be implemented in DB
            print(self.amount_to_be_paid, self.Bill_status)

            print(self.list_of_bills)
        elif option == 2:
            print('Calculates bill by days')
            num_of_days = int(input('Enter number of days to rent'))
            bill = GenerateBill_by_Days(num_of_days)
            amount_to_be_paid = bill.generate_bill()
            print(amount_to_be_paid)
        elif option == 3:
            print('Calculates bill by hour')
            num_of_hours = int(input('Enter number of hours to rent'))
            bill = GenerateBill_by_hours(num_of_hours)
            amount_to_be_paid = bill.generate_bill()
            print(amount_to_be_paid)

    def rent(self):
        option = self.main_menu()
        if option == 1:
            print('Bike chosen by age ')
            self.sub_menu()
        elif option == 2:
            print('Bike chosen by manufacturer ')
        elif option == 3:
            print('Bike chosen by type ')

    def return_bycicle(self):
        print('Bicycle returned')
        # To be implemented

    def bycicles_list(self):
        pass

    def bills_list(self):
        pass

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
