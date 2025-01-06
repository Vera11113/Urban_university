from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'



class Shop:

    def __init__(self):
        self.__filename = 'products.txt'


    def get_products(self):
        try:
            file = open(self.__filename, 'r')
            return file.read()
            file.close()
        except:
            file = open(self.__filename, 'w')
            file.close()


    def add(self, *products):
        for product in products:
            file = open(self.__filename, 'a')
            fileinfo = self.get_products()
            if all(map(lambda x: x in fileinfo, (product.name, product.category))):
                filelines = fileinfo.split('\n')
                file.close()
                for i in range(len(filelines)):
                    if product.name in filelines[i]:
                        new_line = filelines[i].split(', ')
                        new_line[1] = str(int(new_line[1]) + int(product.weight))
                        filelines[i] = ', '.join(a for a in new_line)
                        print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_line[1]}')
                file = open(self.__filename, 'w')
                for line in filelines[:-1]:
                    file.write(line+'\n')
                file.close()
            else:
                file.write(f'{product}\n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 56, 'Veg')
p2 = Product('Potato', 10, 'Veg')
p3 = Product('Tomato', 15, 'Fruit')
s1.add(p1, p2, p3)
print(s1.get_products())


