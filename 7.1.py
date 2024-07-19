class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name):
        self.__file_name = __file_name

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            list_products = self.get_products()
            if product.name and str(product.weight) not in list_products:
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} {product.weight} уже есть в магазине! (См. список: {self.__file_name})')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()  # Что бы что то вернуть, нужно сохранить это в переменную!
        file.close()
        return products


s1 = Shop('products.txt')
s2 = Shop('prod_2.txt')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Apple', 20.3, 'Fruits')
p5 = Product('Spaghetti', 3.4, 'Groceries')
p6 = Product('Spaghetti', 3.6, 'Groceries')

print(p2)  # __str__
print()
s1.add(p1, p2, p3, p4)
print(s1.get_products())
s1.add(p5)
s1.add(p6)
print(s1.get_products())
s1.add(p3, p6)
print(s1.get_products())
s2.add(p2, p4)
print(s2.get_products())
