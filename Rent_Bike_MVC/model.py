class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Client(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email)
        self.address = address


class Partner(Person):
    def __init__(self, name, email, bike):
        super().__init__(name, email)
        self.bike = bike


class Bike:

    def __init__(self, bike_type, manufacturer, year):
        self.type = bike_type
        self.manufacturer = manufacturer
        self.year = year


class Bill:
    def __init__(self, client, bill_id, bike_id, amount, status):
        self.client = client
        #self.partner = partner
        #self.billing_method = billing_method
        self.Status = status
        self.Amount = amount
        self.bill_id = bill_id
        self.bike_id = bike_id


class Rent:
    def __init__(self, client, bike_id):
        self.client = client
        self.bike_id = bike_id


#
# class Register(Partner):
#     def __init__(self, name, email, bike):
#         super().__init__(name, email, bike)
