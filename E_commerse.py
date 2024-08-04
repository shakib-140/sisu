class shopper:
    def __init__(self,name) :
        self.name=name
        self.cart=[]



    def add_to_card(self,item,price,quantity) :
     
        self.cart.append({'item':item, 'price':price,'quantity': quantity})



    def cheaque_out(self,amount) :
        price=0
        for item in self.cart:
            print(item)
            price=price+item['price']*item['quantity']
        print(f'total price of all items is : {price}')  
        print(f'you give me {amount}')
        if amount < price :
            return f'you need to give more money {price-amount}' 
        elif amount > price :
            return f'here are the items and extra money {amount-price}'
        else :
            return 'here are the items'



shopping=shopper('abul')
shopping.add_to_card('t_shirt',400,3)
shopping.add_to_card('pant',500,4)
shopping.add_to_card('watch',300,2)
reply=shopping.cheaque_out(8000)
print(reply)
        
        
        
    
    