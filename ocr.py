from PIL import Image
import pyocr.builders
import sys

args=sys.argv
input=args[1]

engines = pyocr.get_available_tools()
engine = engines[0]

txt = engine.image_to_string(Image.open(input),lang="jpn",builder=pyocr.builders.TextBuilder(tesseract_layout=6))

path_w = "./test_w.txt"

with open(path_w, mode='w') as f:
    f.write(txt)

with open(path_w) as f:
    print(f.read())
