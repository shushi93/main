cost = 50
while (cost > 0):
    x = int(input("Insert coin: "))
    match x:
        case 5:
            cost -= 5
        case 10:
            cost -= 10
        case 25:
            cost -=25
    if (cost > 0):
        print("Amount Due:", cost)

print("Change Owed:", abs(cost))
