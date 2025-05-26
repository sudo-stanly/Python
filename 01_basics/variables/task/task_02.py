# use input() function and print() function

#[NAME BADGE GENERATOR]: ask user for, full name, job title, their company.
    # x,y,z=input("Enter your name: "), input("Enter your title: "), input("Enter your company: ")
    # print(f'[{x}],\nName: {x},\nTitle: {y},\nCompany: {z}')

# [SALARY CALCULATOR]: ask for name, hours worked, pay per hour.
    # x,y,z=input("Enter your name: "), float(input("Enter your hours worked: ")), float(input("Enter your pay per hour: "))
    # pay = y * z
    # print(f"Hi {x}, your total pay is ${y} for {z} hours at ${pay}/hour.")
    
#[DIMPLE INTEREST CALCULATOR]: ask for, princiapl amount, rate(in %), time(in years). Formula: Interest = (P * R * T)/100
    # x,y,z=float(input("Principal amount: ")), float(input("Rate in %: ")), int(input("Time (in years): ")); Interest = (x * y * z) / 100
    # print(f"Total interest earned after {z} years at {y}% is: ${Interest}")

#[TRAVEL PLANNER]: ask for, destination, number of days, daily budget.
    # x,y,z=str(input("Destination: ")), int(input("Number of days: ")), int(input("Daily budget: "));
    # print(f"You're going to {x} for {y} days. You'll need atleast ${z}.")

#[RESTAURANT BILL SPLITTER]: Total bill, Tip percentage, Number of people.
#Formula: total_with_tip = bill + (bill * tip/100)
#Formula: each = total_with_tip / people

x,y,z=int(input("Total bill: $")), int(input("Tip percentage: $")), int(input("Number of people: "));
total_with_tip = x + (x * y/100)
each = total_with_tip / z
print(f"Each person pays: ${round(each, 2)}")