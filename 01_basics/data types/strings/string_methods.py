#[STRING METHODS]: Python has a set of built-in methods that you can use on strings.Python has a set of built-in methods that you can use on strings., All string methods return new values. They do not change the original string.

#[CAPITALIZE]: capitalize() : Converts the first character to upper case
    # txt="hello, world!"; print(txt.capitalize())
    
#[CASE FOLD]: casefold() : 	Converts string into lower case
    # txt="HELLO, world!"; print(txt.casefold())
    
#[CENTER]: center(<position index>) : Returns a centered string
    # txt="HELLO, world!"; print(txt.center(55))
    
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