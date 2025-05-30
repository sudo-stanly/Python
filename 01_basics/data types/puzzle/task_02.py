#[CHECK FOR DECIMAL NUMBER]
codes = ["12345", "007", "9⅞", "42.0", "٣", ""]
print(codes[0].isdecimal(), codes[1].isdecimal(), codes[2].isdecimal(), codes[3].isdecimal(), codes[4].isdecimal(), codes[5].isdecimal())