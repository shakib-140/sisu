


class phone :
    colour='green'
    brand='samsung'
    feature=['can send sms','can call','can pick pic']
    #def call(self) :
        #print('tik tik tik')

    def send_sms(self,text,number) :
        sms=f'{text}--> {number}'
        return sms

my_phone=phone()
#my_phone.call()
can_you_hear_me='i ,)m,---i,s+,*s-e,d$ y,&o,u, s,o m,u?c!h11'
hey=''
for character in can_you_hear_me :
    if character==' ' :
     hey+=character
    if character>='a'and character<='z' :
        hey+=character+''

you='0,#1,^8>*6...3'
hey_you=''
for character in you:
    if character>='0'and character<='9' :
        hey_you+=character+''

sms=my_phone.send_sms(hey,hey_you)
print(sms)

