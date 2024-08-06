class bank :
    def __init__(self,balance) :
         
         self.balance=balance
         self.min_withdraw=100
         self.max_withdraw=10000
    def get_balance(self) :
         return self.balance  
       
    def withdraw(self,amount) :
            if self.balance <amount :
               return'insufficient balance'  
         
            elif amount < self.min_withdraw :
              return f'no withdraw for you.minimum withdraw is {self.min_withdraw}'
            elif amount > self.max_withdraw :
              return 'you cross your daily limit'
          
            else :
               self.balance=self.balance -amount
               return f'here is your money {amount}  now your current balance is {self.get_balance()}'
    def deposite(self,money) :
        self.balance=self.balance + money 
        return self.balance       
           

my_bank=bank(70000)
replay=my_bank.withdraw(300)   
print(replay)  
my_bank.deposite(5000)
print(my_bank.get_balance())      

 