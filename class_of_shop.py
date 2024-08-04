class shop :
    cart=[]
    def __init__(self,buyer) :
        self.buyer=buyer
    
    def add_to_cart(self,item) :
        self.cart.append(item)



buyer_1=shop('shakib')
buyer_1.add_to_cart('t-shirt')
print(buyer_1.cart)

buyer_2=shop('bina')
buyer_2.add_to_cart('book')
print(buyer_2.cart)

buyer_3=shop('robin')
buyer_3.add_to_cart('pen')
print(buyer_3.cart)
        
                