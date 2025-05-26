#[REVEIPT GENERATOR]: ask for customer name, 3 items(name and price each), tax %, tip %.
x,y,z,w = str(input("name: ")), 5.0, 3.5, 4.5
tax, tip = 1.3, 2.0
subt = y + z + w
Total = subt + tax + tip
print(f"customer: {x}\nItems:\n     - Coffee: ${y}\n     - Bagel: ${z}\n     - Juice: ${w}\nSubtotal: ${subt}\nTax: ${tip}\nTip: ${tax}\nTotal: ${Total}")