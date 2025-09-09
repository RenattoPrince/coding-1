class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling price:",self.__maxprice)
    def setmaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setmaxPrice(1000)
c.sell()