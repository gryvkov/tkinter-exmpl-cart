from fgphproject.model.item import Item


class Product:
    def __init__(self):
        self.store = {"шкаф": Item("шкаф", 1000),
                      "полка": Item("полка", 100),
                      "тумба": Item("тумба", 300),
                      "стол": Item("стол", 400),
                      "стул": Item("стул", 200),
                      "табурет": Item("табурет", 100),
                      "зеркало": Item("зеркало", 600),
                      "кровать": Item("кровать", 800),
                      "диван": Item("диван", 1500),
                      "кресло": Item("кресло", 700),
                      "обувница": Item("обувница", 150),
                      "вешалка": Item("вешалка", 80)}

    def addItemToStore(self, o):
        if self.store.__contains__(o.name):
            item = self.store.__getitem__(o.name)
            item.count += o.count
        else:
            self.store = [o.name, o]

    def getItems(self):
        items = []
        for item in self.store:
            items.append(item)
        return items
