from PIL import Image
from PIL import ImageOps
import sys

# python shirt.png before1.jpg after1.jpg
#print(f"{sys.argv[0]}, {sys.argv[1]}, {sys.argv[2]}")

if len(sys.argv) != 3:
    sys.exit("Not enough / too much parameters")
if sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith("png") == False and sys.argv[1].endswith(".jpeg") == False:
    sys.exit("Invalid file types")
if sys.argv[2].endswith(sys.argv[1][-3:]) == False:
    sys.exit("File types are not the same")

try:
    with Image.open("shirt.png") as shirt, Image.open(sys.argv[1]) as im1:
        print(shirt.size)
        im1 = ImageOps.fit(im1, (600,600))
        im1.paste(shirt, (0,0), mask=shirt)
        im1 = im1.convert('RGB')
        im1.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File is not found")
