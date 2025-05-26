"""
    Built-in Data Types
    In programming, data type is an important concept.

    Variables can store data of different types, and different types can do different things.

    Python has the following data types built-in by default, in these categories:

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
"""

#[GETTING THE DATA TYPE]:You can get the data type of any object by using the type() function:
    # x = 5
    # print(f"x is a tpye of: {type(x)}")
    
#[SETTING THE DATA TYPE]
    # x,y,z,w=str("Hello world"),int(20),float(20.5),complex(1j)
    # print(f"x is: {type(x), x}\ny is: {type(y), y}\nz is: {type(z), z}\nw is: {type(w), w}")
    
    # x,y,z,w=["apple", "banana", "cherry"], ("apple", "banana", "cherry"), range(6), {"name" : "John", "age" : 36}
    # print(f"x is: {type(x), x}\ny is: {type(y), y}\nz is: {type(z), z}\nw is: {type(w), w}")
    
    # x,y,z,w=set({"apple", "banana", "cherry"}), frozenset({"apple", "banana", "cherry"}), bool(True), b"Hello"
    # print(f"x is: {type(x), x}\ny is: {type(y), y}\nz is: {type(z), z}\nw is: {type(w), w}")    
    
    # x,y,z=bytearray(5), memoryview(bytes(5)), None
    # print(f"x is: {type(x), x}\ny is: {type(y), y}\nz is: {type(z), z}")