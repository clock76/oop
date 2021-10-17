class Laptop:
    def __init__(self, brand, model, price):
        print('конструктор работает')
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model

laptop = Laptop('Acer', 'aspire 1', 30000)
print('цена =', laptop.price)

print(laptop.laptop_name)