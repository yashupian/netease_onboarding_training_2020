class Calculator:
    name = 'good cal'
    price = 18

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def add(self, x, y):
        print('this is add')
        return x + y

    @staticmethod
    def minus(self, x, y):
        print('this is minus')
        return x - y

    def show_price(self):
        return self.price


ele = Calculator("good", 200)
res = Calculator.add(ele, 1, 111)
print(res)
res = Calculator.minus(ele, 222, 999)
print(res)
res = Calculator.show_price(ele)
print(res)

print(ele.price)
print(ele.name)
