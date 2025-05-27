#[3 TYPES OF NUMERIC TYPES IN PYTHON]: int, float, complex
    # x = 1    # int
    # y = 2.8  # float
    # z = 1j   # complex

#To verify the type of any object in Python, use the type() function:
    # print(type(x))
    # print(type(y))
    # print(type(z))
    
    
#[INT]: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    # x,y,z = 1, 300000000000, -300000000
    # print(type(x),type(y),type(z))
    
#[FLOAT]:Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
    # x,y,z = 1.10, 1.0, -35.59
    # print(type(x),type(y),type(z))
    
    #Float can also be scientific numbers with an "e" to indicate the power of 10.
    # x,y,z = 35e3, 12E4, -87.7e100
    # print(type(x),type(y),type(z))
    
#[COMPLEX]: Complex numbers are written with a "j" as the imaginary part:
    # x,y,z = 3+5j, 5j, -5j
    # print(type(x),type(y),type(z))
    


#[TYPE CONVERSION]:You can convert from one type to another with the int(), float(), and complex() methods.
    #Note: You cannot convert complex numbers into another number type.
    # x,y,z= 1, 2.8, 1j
    # a= float(x)
    # b=int(y)
    # c=complex(z)
    # print(type(x),type(y),type(z))
    
#[RANDOM NUMBER]: Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
    # import random
    # print(random.randrange(1, 10))
