def womanBMR(weight, height, age) :
    BMR = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return BMR

def manBMR(weight, height, age) :
    BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    return BMR

chocCals = 214

weight = float(input("What is your weight? (lb)"))
height = float(input("What is your height? (in)"))
age = float(input("What is your age? (yr)"))

outputWoman = round(womanBMR(weight, height, age) / chocCals, 2)
outputMan = round(manBMR(weight, height, age) / chocCals, 2)

print("Woman: " + str(outputWoman) + ", Man: " + str(outputMan))