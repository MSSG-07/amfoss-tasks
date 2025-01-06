import pytesseract
from PIL import Image

img = Image.open("/home/m-s-surya-gayathri/Pictures/Screenshots/5+5.png")
ex = pytesseract.image_to_string(img).strip()

print(f"Extracted expression: '{ex}'")
res = eval(ex)  
print(f"The result of the expression is: {res}")

