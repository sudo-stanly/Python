#[STRING METHODS]: Python has a set of built-in methods that you can use on strings.Python has a set of built-in methods that you can use on strings., All string methods return new values. They do not change the original string.

#[CAPITALIZE]: capitalize() : Converts the first character to upper case
    # txt="hello, world!"; print(txt.capitalize())
    
#[CASE FOLD]: casefold() : 	Converts string into lower case
    # txt="HELLO, world!"; print(txt.casefold())
    # txt="SUZU IS THE BEST!"; print(txt.casefold())
    
#[CENTER]: center(<position index>) : Returns a centered string
    # txt="HELLO, world!"; print(txt.center(55))
    # txt="i like pizza!"; print(txt.center(55))
    
#[COUNT]: count(<string>)	: Returns the number of times a specified value occurs in a string
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
    
#[ENDSWITH]: endswith(<string>) : Returns true if the string ends with the specified value
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
    
#[FORMAT] format(<variable & value>) : Formats specified values in a string
    #Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
        # txt = "For only {price:.2f} dollars!"
        # print(txt.format(price = 49))
        
        # txt="You need atleast ${price:.2f}."
        # format_txt = txt.format(price=1300)
        # print(format_txt)
        
        # txt="The user is {isActive}."
        # format_txt = txt.format(isActive=True)
        # print(format_txt)
        
#[FORMAT MAP]: format_map(<dict>) : 	Formats specified values in a string
        
        # not a format type
        # txt = "The price of this apple is ${price:.2f}"
        # x=txt.format_map(price=50)
        # print(x)

        # format map is a dictionary type or with a dict data type
        # txt="the price is {price}" #specified type int
        # x=txt.format_map({"price":50}) #will print as 50
        # print(x)
        
            #:.2f will cause type error if dict value is an int


#[INDEX]: index(<string>) : Searches the string for a specified value and returns the position of where it was found. (similar to find() method)
    # txt = "Hello, world!"
    # x=txt.index("world")
    # print(x)

        
#[IS ALPHA NUMERIC]: isalnum() : Returns True if all characters in the string are alphanumeric
    # x="11A aa" #false because it contains space and must only include a number, unique character and a capital
    # x="11Aaa" -> correct
    # if(x.isalnum()):
    #     print(True)
    # else:
    #     print(False)  
    
#[IS APLHA]:  isalpha()  : Returns True if all characters in the string are in the alphabet.
    # x="aaAAXXyy"
    # x="aaAAXXyy11" #false because it contains a numeric value.
    # if(x.isalpha()):
    #     print(True)    
    # else:
    #     print(False)
    
#[IS ASCII]: isascii() : Returns True if all characters in the string are ascii characters
    # txt="A" # A has the ascii value of 65
    # if(txt.isascii()):
    #     print(True)    
    # else:
    #     print(False)
    
# [IS DECIMAL] isdecimal(): Returns True if all characters in the string are decimals
    # txt="123"
    # if(txt.isdecimal()):
    #     print(True)    
    # else:
    #     print(False)
    
# [IS DIGIT] isdigit(): Returns True if all characters in the string are digits
    # txt="50800"
    # if(txt.isdigit()):
    #     print(True)    
    # else:
    #     print(False)
    
#[IS PRINTABLE]: isprintable() : Returns True if all characters in the string are digits
    # txt="Hello! are you #1"
    # if(txt.isprintable()):
    #     print(True)    
    # else:
    #     print(False)
    
#[IS SPACE]: isspace() : 	Returns True if all characters in the string are whitespaces
    # txt="                  "
    # if(txt.isspace()):
    #     print(True)    
    # else:
    #     print(False)
    
#[IS TITLE]: istitle() : Returns True if the string follows the rules of a title
    # txt = "Hello, And Welcome To My World!"
    # if(txt.istitle()):
    #     print(True)    
    # else:
    #     print(False)
    
#[IS UPPER]: isupper() : Returns True if all characters in the string are upper case
    # txt = "HELLO WORLD!"
    # if(txt.isupper()):
    #     print(True)    
    # else:
    #     print(False)
    
#[JOIN]: <string>.join(<variable>) : Joins the elements of an iterable to the end of the string

    #[example 1]:
        # x=["Hello", "world"]
        # j = "::".join(x)
        # print(j)
        
    #[example 2]: includes a number in list
        # x=["Hello", "world" , 32]
        # j = "::".join(str(y) for y in x) #y converted to string will turn all in x to string.
        # print(j) 
        
    
#[LEFT JUSTIFIED]: ljust(<position index>) : 	Returns a left justified version of the string
    # txt= "Hello, world"
    # x = txt.ljust(20)
    # print(x, "my name is Masaru!")
    
#[LOWER]: lower() : Converts a string into lower case
    # txt= "hello, world"
    # x = txt.islower()
    # print(x)
    
#[LEFT STRIP]: lstrip() : Returns a left trim version of the string : Remove spaces to the left of the string:
    # txt="apple"
    # x = txt.lstrip()
    # print("of all the fruits there is", x , "is my favourite")
    
#[MAKE TRANSLATION]: maketrans() : Returns a translation table to be used in translations
    #Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
        # translation = {"Masaru": "マサル"}
        # txt = "My name is Masaru"
        # translated_txt = " ".join(translation.get(word, word) for word in txt.split())
        # print(translated_txt)
        

#[PARTITION]: partition(<strign>) : Returns a tuple where the string is parted into three parts
    #search for the word "apples", and return a tuple with three eleemnts
        # 1. everything before the "match", 2. the "match" 3. everything after the "match"
            # txt="I could eat apples all day"
            # x=txt.partition("apples")
            # print(x)
            
# [REPLACE]: replace(<string>, <string to replace>) : Returns a string where a specified value is replaced with a specified value
    # txt = "I like bananas"
    # x = txt.replace("bananas", "apples")
    # print(x)
    
    
#[RIGHT FIND]: rfind(<string>) : Searches the string for a specified value and returns the last position of where it was found (right)
    # txt="Hello, world!"
    # x=txt.rfind("world")
    # print(x)
    
#[RIGHT INDEX]: rindex(<string>) : Searches the string for a specified value and returns the last position of where it was found
    # txt="Hello, world!"
    # x=txt.rindex("world")
    # print(x)
    
#[RIGHT JUSTIFIED] : rjust(<position index>) : Returns a right justified version of the string
    # txt="Hello, world!"
    # x=txt.rjust(20)
    # print(x)
    
#[RIGHT PARTITION]: rpartion(<string>) :	Returns a tuple where the string is parted into three parts
    # txt="I am a box of scraps."
    # x=txt.partition("of")
    # print(x)
    
#[RIGHT SPLIT]: rsplit(<string>) : 	Splits the string at the specified separator, and returns a list
    # txt="Hello, world."
    # x=txt.rsplit(",")
    # print(x)
    
#[RIGHT STRIP]: rstrip() : Returns a right trim version of the string
    # txt="Hello, world."
    # x=txt.rstrip(",")
    # print(x)
    
#[SPLIT]: split() : 	Splits the string at the specified separator, and returns a list
    # txt="Welcome to the jungle."
    # x=txt.split()
    # print(x)

#[SPLIT LINES]: splitlines() : 	Splits the string at line breaks and returns a list
    # txt="Thank you for the music\nWelcome to the jungle."
    # x=txt.splitlines()
    # print(x)
    
#[STARTS WITH]: startswith(<string>) : Returns true if the string starts with the specified value
    # txt="Hello, world!"
    # x=txt.startswith("Hello")
    # print(x)
    
    
 