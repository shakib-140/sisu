class laptop :
    def __init__(self,brand,age) :
        self.brand=brand
        self.age=age
    def increse_age(self,age=1) :
        self.last_age=self.age
        self.age+=age
    def repear(self,life_increase=-5) :
        self.increse_age(life_increase)




my_laptop=laptop('dell',40)
print(my_laptop.age)
my_laptop.increse_age()
my_laptop.increse_age()
print(my_laptop.last_age)
print(my_laptop.age)
my_laptop.repear(-3)
print(my_laptop.age)
print(my_laptop.__dict__)
        
