from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        print(f'{self.name}, {self.weight}, {self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return file

    def add(self, *products):
        file = open(self.__file_name, 'a')
        #file.write()
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

p2.__str__()
p3.__str__()
p1.__str__()

#s1.add(p1, p2, p3)

s1.get_products()
