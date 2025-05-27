#[ESCAPE CHARACTER]:
    #To insert characters taht are illegal in a string, use an escape character.
    #an escape character is a backslash '\' followed by the character you want to insert
    #an example of an illegal cahracter is a double qute inside a string that is surrounded by double quotes.
    
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
    #txt=" We are so-called "Vikings" from the north."
        #To fix this problem, use the escape character \":
        #The escape character allows you to use double quotes when you normally would not be allowed:
        #txt=" We are so-called \"Vikings\" from the north."
        
    
#[OTHER ESCAPE CHARACTERS]:
    #\' : single quote
    #\\ : backslash
    #\n : new line
    #\r : carriage return
    #\t : tab
    #\b : backspace
    #\f : form feed
    #\ooo : octal value
    #\xhh : hex value

#hex
    # txt = "\x6d\x61\x73\x61\x72\x75"
    # print(txt)
    
#octal
    # txt = "\155\141\163\141\162\165"
    # print(txt)