class person :
    def __init__(self,name,age,money,height=90) -> None:
        self.name=name
        self.age=age
        self.money=money
        self.height=height


    def __call__(self):
        print(f'this is {self.name} with age {self.age} and have {self.money}')
        

    def __eq__(self, other) :
        return self.age == other.age 
    
    def __len__(self) :
        return self.height
        

    def __ge__(self ,other) :
        return self.money >= other.money
    def __add__(self,other) :
        return self.money + other.money


        
alim=person('alim',23,560)
dalim=person('dalim',24,780,70)
print(alim+dalim)    
alim()
print(alim.age> dalim.age)
print(alim == dalim)
print(alim >=dalim)
friend=[10,20,30,40,50]
print(len(friend))
print(len(dalim))
print(len(alim))
