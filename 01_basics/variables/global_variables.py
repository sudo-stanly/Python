# [GLOBAL VARIABLES]: 

#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#can be used inside and outside of a function.
# x = 'awsome'
# def myfunc():
#     print('python is:'+x)
# myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
    # x = 'suzu'
    # def myfunc():
    #     x = 'fantastic'
    #     print('py is:'+x)
    # myfunc()
    # print('py is:'+x)
    
#[GLOBAL KEYWORD]: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
#Also, use the global keyword if you want to change a global variable inside a function.

    # def myfunc():
    #     global x
    #     x = 'fantastic'
    # myfunc()
    # print('py is:'+x)
    
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
    # x='awsome'
    # def myfunc():
    #     global x
    #     x = 'fantastic'
    # myfunc()
    # print('py is:'+x)
    