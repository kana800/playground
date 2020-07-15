
class Customer(object):

    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.cost = 0
        self.customer_record = { 'Name': f"{self.f_name}{self.l_name}",
                                 'Price': self.cost,
                                 'Booking ID': {}
                                }
    def __str__(self):
        return f"{self.customer_record['Name']}\n\t{self.customer_record['Price']}\n\t{self.customer_record['Booking ID']}"
    def __repr__(self):
        return f"{self.customer_record['Name']}\n\t{self.customer_record['Price']}\n\t{self.customer_record['Booking ID']}"
class Booking(object):

    def isAvailable(self,**kwargs):
        raise NotImplementedError

    def makeReservation(self,**kwargs):
        raise NotImplementedError

class Hotel(Booking):

    hotel_rooms = {'One-Bedroom': 50, 
            'Double-Bedroom': 50,
            'Queen-Size Bedroom': 40,
            'King-Size Bedroom': 40,
            'Deluxe Suite':10
            }
    hotel_prices = {'One-Bedroom': 100, 
        'Double-Bedroom': 150,
        'Queen-Size Bedroom': 250,
        'King-Size Bedroom': 300,
        'Deluxe Suite':1000
        }

    def __init__(self,hotel_name):
        self.hotel_name = hotel_name

    def isAvailable(self,room_name):
        return self.hotel_rooms[room_name] > 0

    def makeReservation(self,customer,room_name):
        if self.isAvailable(room_name):
            self.hotel_rooms[room_name] -= 1
            customer.customer_record['Price'] += self.hotel_prices[room_name]
            customer.customer_record['Booking ID']['Room Type'] = room_name
            customer.customer_record['Booking ID']['Room Price'] = self.hotel_prices[room_name]

if __name__ == "__main__":

    # creating a customer
    c1  = Customer("Jim","Halpert")

    # creating a hotel

    h1  = Hotel("Standford Hotel")

    # checking if a room is available
    h1.isAvailable("One-Bedroom")

    # making reservation
    h1.makeReservation(c1,"One-Bedroom")

    # priting out customer record
    print(c1)



