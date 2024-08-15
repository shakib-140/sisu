#with open('massage.txt','a') as filewrite :
  # filewrite.write('hello world how are you ?')
  # filewrite.write ('\n')

with open('massage.txt','r') as fileread :
    text=fileread.read()
    print(text)
