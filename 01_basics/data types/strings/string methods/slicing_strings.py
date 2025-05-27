#[SLICING STRINGS]:You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

#Note: The first character has index 0.
    # b="Hello, world!"
    # print(b[1:5])
    
#[SLICE FROM THE START]:By leaving out the start index, the range will start at the first character:
    #Get the characters from the start to position 5 (not included):
    # b="Hello, world!"
    # print(b[:5])
    
#[SLICE FROM THE END]:By leaving out the end index, the range will go to the end:
    #Get the characters from position 2, and all the way to the end:
    # b="Hello, world!"
    # print(b[2:])
    
#[NEGATIVE INDEXING]: Use negative indexes to start the slice from the end of the string:
    #Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
    # b="Hello, world!"
    # print(b[-5:-2])
    

# x='welcome'
# print(x[3:5])

x='hello world'
print(x[2:5])
    
