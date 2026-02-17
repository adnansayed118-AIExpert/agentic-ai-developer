print("This is BMI calculator program to calculate your BMI! All the best")
name=input("enter your name : ")
weight=float(input('enter your weight in Kgs : '))
height=float(input("what is your preffered unit of height : "))

bmi=weight/(height ** 2)
if bmi < 18.5:
    print("you are underwieght")
elif 18.5>=bmi<=25:
    print("you are normal")
elif 25<=bmi>30:
    print("you are over weight")
else:
    print("you are obesese")
    