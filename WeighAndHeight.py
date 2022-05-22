print ('Hello friend this is a BSIprog created by Maksyk Dzhendzhera\n')
w = float(input("Please enter your weight: \n"))
h = float(input("Please enter your height: \n"))
x = w / h**2
if x < 18.5:
    print ("Underweight\n")
elif x >= 18.5 and x < 25:
    print ("Normal\n")
elif x >=25 and x <30:
    print ('Overweight\n')
else:
    print ("Obesity\n")
print ("Thank you for using this programe!")
