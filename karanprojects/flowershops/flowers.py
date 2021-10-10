'''
Create a flower shop application which deals in flower objects and 
use those flower objects in a bouquet object which can then be sold. 
Keep track of the number of objects and when you may need to order more.
'''

flower_type = ['Rose','Carnation','Tulip','Lily','Orchid']



class flower:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

class Bouquet:

    def __init__(self,name,flower):
        self.name = name
        self.flower = flower

    @property
    def price(self):
        p = 0 # price of the bouquet
        for i,x in self.flower.items():
            p += i.price * x
        return p

class Shop:

    def __init__(self,name,items):
        self.name = name
        self.items = items
        self.income = 0

    def sell(self,bouquet_name,quantity):
        q = self.items[bouquet_name]
        if quantity > q:
            return "Item Not Available"
        else:
            quantity -= 1
            self.items[bouquet_name] = quantity
            self.income += bouquet_name.price


    @property
    def availablestuff(self):
        print("ITEMS\n")
        for i,j in self.items.items():
            print(f"\tname: {i.name}\tquantity: {j}\tprice: ${i.price}")

if __name__ == '__main__':
    # flowers
    rose = flower('rose',4.50)
    tulip = flower('tulip',9.99)
    orchid = flower('orchid',4.33)

    justfriends=Bouquet('Just Friends',{rose:5,tulip:2})
    justmarried=Bouquet('Just Married',{rose:200,tulip:400})
    s = Bouquet('Sorry for forgetting your bday',{rose:50,tulip:40,orchid:40})

    shop = Shop('flower hub',{justfriends:40,justmarried:30,s:1})
    print("income @ start\n",shop.income)
    shop.sell(justfriends,4)
    print("income after first sale\n",shop.income)
    shop.sell(s,25) # over ordering!
    shop.availablestuff
