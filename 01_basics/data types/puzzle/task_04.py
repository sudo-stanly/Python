#pure digit check
    # l1=["100", "3.0", "⅔", "42", "eight", ""]
    # r1=list(map(str.isdecimal, l1))
    # print(r1)
    
#decimal characters only
    # l2=["٢", "4.5", "5", "٩", "0", ""]
    # r2=list(map(str.isdecimal, l2))
    # print(r2)

#fully numeric
    # l3=["⑦", "123", "二", "5.0", "003", ""]
    # r3=list(map(str.isnumeric, l3))
    # print(r3)
    
#ascii digits only
    # l4=["123", "٧٨٩", "42", "𝟙𝟚", "999", ""]
    # r4=list(map(str.isascii, l4))
    # print(r4)
    
#lowercase
    # l5=["abc", "Abc", "aBC", "lower", ""]
    # r5=list(map(str.islower, l5))
    # print(r5)
    
#uppercase
    # l6=["LOUD", "Loud", "up", "UP", ""]
    # r6=list(map(str.isupper, l6))
    # print(r6)
    
#titlecase
    # l7=["Star Wars", "the Empire Strikes Back", "Return Of The Jedi", "A New Hope", ""]
    # r7=list(map(str.istitle, l7))
    # print(r7)