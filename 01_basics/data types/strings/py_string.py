#[STRINGS]: Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello"
#You can display a string literal with the print() function:
    # print("Hello")
    # print('Hello')
    
#[QUOTES INSIDE QUOTES]: You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
    # print("It's alright")
    # print("He is called 'koneko'")
    # print('He is called "koneko"')
    # print("Hello world! \"Python\"")
    
#[STRING VARIABLE]: Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
    # a="Hello"
    # print(a)
    
#[MULTILINE STRINGS]:You can assign a multiline string to a variable by using three quotes:
    # a=""" Lorem ipsum dolor sit amet,
    # consectetur adipiscing elit,
    # sed do eiusmod tempor incididunt
    # ut labore et dolore magna aliqua. """
    # print(a)
    
    #OR by using three single quotes
    # a=''' Lorem ipsum dolor sit amet,
    # consectetur adipiscing elit,
    # sed do eiusmod tempor incididunt
    # ut labore et dolore magna aliqua. '''
    # print(a)
    
#[STRINGS ARE ARRAYS]: Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
    # a="Hello world"
    # print(a[0])
    
#[LOOPING THROUGH A STRING]: Since strings are arrays, we can loop through the characters in a string, with a for loop.
    # for x in "banana":
    #   print(x)
    
#[STRING LENGTH]: To get the length of a string, use the len() function.
# a="Hello world"
# print(len(a)) 


#[CHECK STRING]:To check if a certain phrase or character is present in a string, we can use the keyword in.
    # Use it in an if statement:
    # a="Hello world"
    # x="free"
    # if x in a:
    #     print(f"yes \"{x}\" is present")
    # else:
    #     print("not present.")
    
    #[CHECK IF NOT IN STRING]:To check if a certain phrase or character is present in a string, we can use the keyword in.
        # Use it in an if statement:
        # a="Hello world"
        # x="free"
        # if x not in a:
        #     print(f"yes \"{x}\" is not present")
        # else:
        #     print("present.")
