#Which strings are fully numeric decimals?
l1 = ["42", "3.14", "٠١٢", "1000", "ten", ""]
r1 = list(map(str.isdecimal, l1))
print(r1)