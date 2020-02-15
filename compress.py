import sys
from pathlib import Path
from PIL import Image
import math

arguments = sys.argv
try:
    file_path = Path(arguments[1])
except IndexError:
    print("No file specified.")
    sys.exit(0)
if file_path.exists() is False:
    print("The file does not exist.")
    sys.exit(0)
if file_path.is_file() is False:
    print("It's not a file.")
    sys.exit(0)
try:
    image = Image.open(file_path)
except IOError:
    print("It's not an image.")
    sys.exit(0)
x, y = image.size
xfinal, yfinal = math.floor(x / 1.3), math.floor(y / 1.3)
image = image.resize((xfinal, yfinal), Image.ANTIALIAS)
image.save(file_path, optimize=True, quality=90)
