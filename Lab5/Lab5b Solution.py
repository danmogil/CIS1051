
stdIn = 0
while stdIn not in range(1,9):
    stdIn = int(input("Enter a number between 1 and 8 (inclusive): "))

for i in range(1, stdIn + 1):
    temp = stdIn - i
    print(" " * temp + "#" * (stdIn - temp) + " " * 2 + "#" * (stdIn - temp))