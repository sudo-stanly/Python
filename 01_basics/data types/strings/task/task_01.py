#1. store each piece of information in appropriately named variables.
#2. format a result string that looks like this (with score formatted to 1 decimal place)
"""
    Name       : Alice Johnson
    Course     : Mathematics
    Score      : 89.5
    Passed     : True
"""
#3.Apply and print using string methods.
n,c,s,p="\tname\t:\t{name}\n","\tcourse\t:\t{course}\n","\tscore\t:\t{score}\n","\tpassed\t:\t{passed}"
x,y,z,w=n.format_map({"name":"suzu"}).title(), c.format_map({"course":"mathemathics"}).title(), s.format_map({"score":98.45}), p.format_map({"passed":True})
print(x,y,z,w)