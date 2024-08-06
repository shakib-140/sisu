#def do_something() :
 #   print('do something inside the function')
  #  def inner_function() :
   #     print('do something inner function')
    #inner_function() 


#do_something()
def first_function() :
    print('inside the first function')
    def second_function() :
        print('inside the second function')
    return second_function
        


result=first_function()
result()
first_function()()
    
