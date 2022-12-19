# importing modlues
from PIL import Image, ImageEnhance, ImageFilter
import os

# The path to image and were you want the output to come
path = "The Image Editor\img"
pathOut ="The Image Editor\edited"

for filename in os .listdir(path):
    img = Image.open(f"{path}/{filename}")

# editing it
    edit = img.filter(ImageFilter.CONTOUR)

# the amout of effect that the edit put
    factor = 10

# It is enhancing it
    enhancer = ImageEnhance.Sharpness(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")