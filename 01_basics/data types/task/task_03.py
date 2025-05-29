#[OBJECTIVE]:Write a Python program that takes a full name (e.g., "Yanagi Masaru") and manipulates it in several ways using string operations.
    # Original Name : Yanagi Masaru
    # Reversed Name : Masaru Yanagi
    # Initials      : Y.M.
    # Uppercase     : YANAGI MASARU
    # Lowercase     : yanagi masaru
    # Codename      : Yama
    
# n="Yanagi Masaru"

#1.original name
    # print(f"Original Name\t:\t{n}")

#2.reversed name
    #first try to find the 2nd name and get the index and length.
        #f2n=n.find("Masaru") # 7:13
        
    #now the first name
        # f1n=n.find("Yanagi") # 0:6
    # print(n[7:13], n[0:6])
    # print(f"Reveresed Name\t:\t{n[7:13]} {n[0:6]}")
    
    #OR use split :)
    
    # s=n.split(" ")
        #     # # print(s)
        #     # #then print them in reverse
        #     # print(s[1], s[0])
    # print(f"Reversed Name\t:\t{s[1]} {s[0]}")


#3.initials
    #list data type
    
    # l=list(n)
    # print(l[0],l[7])
    # print(f"Initials\t\t:\t{l[0]}.{l[7]}.")


#4: upper method
    # print(f"Uppercase\t\t:\t{n.upper()}")

#5. lower method
    # print(f"Uppercase\t\t:\t{n.lower()}")

    
#6.code name
    #get from initial list
    # print(f"Codename\t\t:\t{l[0]}{l[1]}{l[7].casefold()}{l[8]}")