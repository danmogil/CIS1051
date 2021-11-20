date = input("Please enter a date in MM/DD/YYYY format: ").split("/")
month = int(date[0])
day = int(date[1])
year = int(date[2])
out = ""

def isLeap(year):
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

if year > 0:
    if 0 < month <= 12:
        if month in [4, 6, 9, 11] and not 0 < day <= 30:
            out = "invalid day!"
        elif month == 2:
            if isLeap(year):
                if not 0 < day <= 29:
                    out = "invalid day!"
            elif not 0 < day <= 28:
                out = "invalid day!"
        elif not 0 < day <= 31:
            out = "invalid day!"
    else:
        out = "invalid month!"
else:
    out = "invalid year!"

print("valid" if len(out) == 0 else out)