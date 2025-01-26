import pytesseract
from PIL import Image

img = Image.open("amfoss-tasks/Task-02/5+5.png")
ex = pytesseract.image_to_string(img).strip()

print(f"Extracted expression: '{ex}'")
res = eval(ex)  
print(f"The result of the expression is: {res}")

