#[STRING METHODS]: Python has a set of built-in methods that you can use on strings.Python has a set of built-in methods that you can use on strings., All string methods return new values. They do not change the original string.

#[CAPITALIZE]: capitalize() : Converts the first character to upper case
    # txt="hello, world!"; print(txt.capitalize())
    
#[CASE FOLD]: casefold() : 	Converts string into lower case
    # txt="HELLO, world!"; print(txt.casefold())
    # txt="SUZU IS THE BEST!"; print(txt.casefold())
    
#[CENTER]: center(<position index>) : Returns a centered string
    # txt="HELLO, world!"; print(txt.center(55))
    # txt="i like pizza!"; print(txt.center(55))
    
#[COUNT]: count()	: Returns the number of times a specified value occurs in a string
    # txt="I love apples, apple are my favourite fruit"
    # x= txt.count("apple")
    # print(x)
    
    #DEFINITION & USAGE: The count() method returns the number of times a specified value appears in the string.
        #string.count(value, start, end)
    
        # txt="apples are great which is why apples makes the doctor go away when there's an apple ahead."
        # l=len(txt); x = txt.count("apple", 0, l); print(x)
        
        #PARAMETER & DESCRIPTION:
        #value  :  REQUIRED: A string. The string to value to search for.
        #start  :  OPTIONAL: The position to start the search. Default 0
        #end    :  OPTIONAL: An integer. The position to end the search. Default is the end of the string
        
        #txt = "this is a message about an important message about messages."; l = len(txt); x = txt.count("message", 0 , l); print(x)

#[ENCODE]: encode() : Returns an ecoded verion of the string.
    # txt = "this is an encoded message."
    # x= txt.encode()
    # print(x)
    
    # txt="encoded msg";
    # x=txt.encode()
    # print(x)
    
#[ENDSWITH]: endswith() : Returns true if the string ends with the specified value
    # txt="Lorem ipsum dolor sit amet consectetur, adipisicing elit." 
    # e=txt.endswith(".")
    # print(e)
    
#[EXPAND TABS]: expandtabds(<tab size>) : sets the tab size of a string
    # txt="Lorem\t ipsum dolor\t sit\t amet\t consectetur,\t adipisicing elit." 
    # t = txt.expandtabs(3)
    # print(t)
    
#[FIND]: find(<string>) : Searches the string for a specified value and returns the position of where it was found
    # txt="Lorem ipsum dolor sit amet consectetur, adipisicing elit." 
    # x=txt.find("amet consectetur")
    # print(x)
    
#[FORMAT] format() : Formats specified values in a string
    #Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
        # txt = "For only {price:.2f} dollars!"
        # print(txt.format(price = 49))
        
        # txt="You need atleast ${price:.2f}."
        # format_txt = txt.format(price=1300)
        # print(format_txt)
        
        # txt="The user is {isActive}."
        # format_txt = txt.format(isActive=True)
        # print(format_txt)
        