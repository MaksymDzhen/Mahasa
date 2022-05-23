print ("Hello, this is Miles/Km converter\n\n")
type_1 = ["MILES", "Miles", "miles", "mls", "Mls", "m", "M", "MILE", "Mile", "mile"]
type_2 = ["KM", "Km", "km", "K", "k"]
while True:
    type = str(input("Type what you want to convert MILES or KM: "))
    if type in type_1 or type in type_2:
        if type in type_1 :
            print ("OK\n")
            x = float(input("Emter miles you want to convert: \n"))
            y = x * 1.60934
            print ("It is " + str(y) + " km\n")
            break
        elif type in type_2:
            print("Lets do it\n")
            q = float(input("Enter km you want to convert: "))
            z = q / 1.60934
            print ("It is " + str(z) + " miles\n")
            break
    else:
        print ("Invalid input, please try it again!\n")
       
print ("Thank You for using this programe")
