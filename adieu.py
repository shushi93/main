import inflect
p = inflect.engine()
arr = []
while True:
    try:
        x = input("Name: ")
        arr.append(x)
    except EOFError:
        break
    except KeyboardInterrupt:
        break
result = p.join(arr)
print ("Adieu, adieu, to", result)
