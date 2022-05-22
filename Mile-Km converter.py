print ("Hello, this is Miles/Km converter\n\n")

type = str(input("Type what you want to convert MILES or KM: "))
if type == "miles" or type == "MILES" or type == "Miles" or type == "mls" or type == "m":
    print ("OK\n")
    x = float(input("Emter miles you want to convert: \n"))
    y = x * 1.60934
    print ("It is " + str(y) + " km\n")
elif type == "km" or type == "KM" or type == "Km" or type == "k":
    print("Lets do it\n")
    q = float(input("Enter km you want to convert: "))
    z = q / 1.60934
    print ("It is " + str(z) + " miles\n")
print ("Thank You for using this programe")
