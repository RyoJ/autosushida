import pyocr
import pyocr.builders
from PIL import Image
 
tools = pyocr.get_available_tools()
tool = tools[0]
res = tool.image_to_string(Image.open("./my_jpn_test.png"), lang="jpn", builder=pyocr.builders.TextBuilder(tesseract_leyout=6))
 
print(res)