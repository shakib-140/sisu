s = 'Programming Hero is the best'
st2=''
for word in s.split() :
     
    for i in range(len(word)-1,-1,-1) :
        if word[i] == '1':
            st2+=' '
        else :
            st2+= word[i]
    st2+=' '        
print(st2)      
