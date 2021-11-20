
stdIn = input("Enter a credit card #: ").strip()
f2d = int(stdIn[:2])
if len(stdIn) not in [13, 15, 16]:
    print("Invalid")
else:
    stdIn = int(stdIn)
    s1 = 0
    s2 = 0
    while stdIn != 0:
        s1 += stdIn % 10
        stdIn //= 10
        temp = (stdIn % 10) * 2
        if temp < 10:
            s2 += temp
        else:
            s2 += temp % 10
            temp //= 10
            s2 += temp % 10
        stdIn //= 10
    if (s1 + s2) % 10 != 0:
        print("Invalid")
    else:
        if f2d in [34, 37]:
            print("AMEX")
        elif f2d in range(51, 56):
            print("MasterCard")
        elif f2d in range(40, 50):
            print("Visa")
        else:
            print("Invalid")

