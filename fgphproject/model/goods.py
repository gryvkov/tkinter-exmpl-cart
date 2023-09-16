class Goods:
    def __init__(self, prod, _count):
        self.prod = prod
        self.name = prod.name
        self.__count = _count
        self.__price = prod.price
        self.__countTotal()

    def setProdCount(self):
        res = self.prod.getStore() - self.__count
        self.prod.setStore(res)

    def __countTotal(self):
        self.__total = self.__price * self.__count
        if self.__count >= 3:
            self.__total = self.__total * 0.7

    def getTotal(self):
        return self.__total

    def setPrice(self, _price):
        self.__price = _price
        self.__countTotal()

    def getPrice(self):
        return self.__price

    def setCount(self, _count):
        self.__count = _count
        self.__countTotal()

    def getCount(self):
        return self.__count

    def show(self):
        return self.name + " количество " + str(self.__count) + " цена " + str(self.__price)
