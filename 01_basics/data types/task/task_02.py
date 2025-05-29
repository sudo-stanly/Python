#[PERSONAL CARD]: Write a Python program that stores the following information in variables and then prints a nicely formatted "info card" using string manipulation:
#example output:
# ----------------------------
# |      Personal Info Card     |
# ----------------------------
# Name       : John Doe
# Age        : 25
# Height     : 1.75 m
# Hobby      : Reading
# Quote      : "Stay hungry, stay foolish."
# ----------------------------
n,a,h,q="Name\t:\t{name}\n","Age\t:\t{age:.2f}\n","Height\t:\t{height}\n","Quote\t:\t{quote}"; x,y,z,w=n.format_map({"name":str("suzu hime").title()}),a.format_map({"age":int(25)}),h.format_map({"height":float(1.75)}),q.format_map({"quote":str("My world.")}); hdr="-------------------------\n|\tPersonal Info Card \t| \n-------------------------\n"
print(hdr,x,y,z,w,"\n-------------------------")