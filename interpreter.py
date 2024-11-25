expression = input("What do you want to calculate? ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
#print(y)
if (y == "+"):
    print(x + z)
elif(y == "-"):
    print(x - z)

elif (y == "*"):
    print (x * z)

else:
    print(x / z)

