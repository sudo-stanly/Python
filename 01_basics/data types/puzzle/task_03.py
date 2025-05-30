#Which strings are fully numeric decimals?
    # l1 = ["42", "3.14", "٠١٢", "1000", "ten", ""]
    # r1 = list(map(str.isdecimal, l1))
    # print(r1)
    
#Which strings are strictly lowercase?
    # l2 = ["apple", "Apple", "BANANA", "banana", "Cherry", ""]
    # r2 = list(map(str.islower, l2))
    # print(r2)
    
#Which strings contain only whitespace?
    # l3 = [" ", "\t", "nope", "yes", "", "\n"]
    # r3 = list(map(str.isspace, l3))
    # print(r3)
    
#Which strings are true title case?
    # l4 = ["Ender's Game", "the Hobbit", "War and Peace", "Gone With The Wind", ""]
    # r4 = list(map(str.istitle, l4))
    # print(r4)