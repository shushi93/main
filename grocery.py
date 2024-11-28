items = {}
while True:
    try:
        x = input().upper()
        y = items.get(x, 0)
        y += 1
        items[x] = y
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    except KeyError:
        print("Item is not a string")
print()
for i in sorted(items.keys()):
    print(items[i], i)
