weight = input("please enter your weight in lbs: ")
height_ft = input("pleae enter your height in ft unit: ")
height_in = input("please enter your height in inch unit: ")

height_tot_inch = int(height_ft)*12 + int(height_in)
print ("your total height in inches is: ", height_tot_inch)

bmi = (int(weight)*703) / height_tot_inch**2

print ("your bmi is: ", round(bmi,1)) 

if bmi < 16.0:
    print("you are Severely Underweight")
elif bmi >=16.0 and bmi <=18.4:
    print("you are Underweight")
elif bmi >= 18.5 and bmi <=24.9:
       print("you are normal")
elif bmi >= 25.0 and bmi <=29.9:
    print("you are Overweight")
elif bmi >= 30.0 and bmi <=34.9:
       print("you are Underweight")
elif bmi >= 35.0 and bmi <=39.9:
       print("you are Underweight")
       
else:
    print ("you are Morbidly Obeseve ")

"""< 16.0    Severely Underweight 
16.0 - 18.4   Underweight
18.5 - 24.9   Normal
25.0 - 29.9   Overweight
30.0 - 34.9   Moderately Obese
35.0 - 39.9   Severely Obese
> 39.9   Morbidly Obeseve """