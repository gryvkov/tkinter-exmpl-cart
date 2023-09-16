import datetime


class Order:
    def __init__(self, name, address, order_id):
        self.date = datetime.datetime.now()
        self.name = name
        self.__list = {}
        self.__total = 0
        self.address = address
        self.id = order_id

    def addItems(self, o):
        self.__list[o.name] = o
        self.__makeTotal()

    # changed for processing with a dict
    def showAll(self):
        for x in self.__list:
            print(self.__list.get(x).show())
        print(self.name + " " + str(self.date) + " адрес: " + self.address + " сумма: " + str(self.__total))

    def __makeTotal(self):
        self.__total = 0
        for x in self.__list:
            val = self.__list.get(x)
            self.__total = self.__total + val.getTotal()

    def printOrder(self):
        print(self.showAll())

    def getName(self):
        return self.name
