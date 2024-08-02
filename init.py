class phone :
    manufacture='china'
    def __init__(self,brand,colour,price):

        self.brand=brand
        self.colour=colour
        self.price=price
    def send_sms(self,text,number) :
        sms=f'send sam {text} to {number}'
        return sms


my_phone=phone('realme','green',24500)
her_phone=phone('iphone','purpole',100000)
dad_phone=phone('nokia','black',1000)

print(my_phone.manufacture,my_phone.brand,my_phone.colour,my_phone.price)
print(my_phone.price,her_phone.price,dad_phone.price)