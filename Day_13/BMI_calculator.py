weight = int(input("What is your weight?"))
height = int(input("What is you height?"))

bmi = weight / (height ** 2)

if bmi >= 25:
    print("OverWeight.")
elif bmi >= 18.5:
    print("Normal Weight.")
else:
    print("UnderWeight")