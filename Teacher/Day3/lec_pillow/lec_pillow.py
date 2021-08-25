from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import os
from icecream import ic

# Get File Information
def get_info(img_file_path):
    img = Image.open(img_file_path)
    ic(img)
    return ({'FileName':img.filename,
             'Format':img.format,
             'Format Desc':img.format_description,
             'Width':img.width,
             'Height':img.height,
             'Mode':img.mode,
             'Bit':img.bits})

# Convert Image Format
def convert_format(img_file_path, format):
    img = Image.open(img_file_path)
    path = img_file_path[:-3] # images/car.jpg -> images/car
    path += format
    img.save(path)

# Make Thumbnail Image
def make_thumbnail(img_file_path, width=300, height=300):
    img = Image.open(img_file_path)
    size = width, height
    img.thumbnail(size)
    dir = os.path.dirname(img_file_path) # images/car.jpg -> images
    file_name = os.path.basename(img_file_path) # car.jpg
    img.save(os.path.join(dir, 'thumb_' + file_name)) # images/car.jpg -> images/thumb_car.jpg

# Crop Image
def crop_image(img_file_path, from_x, from_y, to_x, to_y):
    img = Image.open(img_file_path)
    img = img.crop((from_x, from_y, to_x, to_y))
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    img.save(os.path.join(dir, 'crop_' + file_name))  # images/thumb_car.jpg

# Resize Image
def resize_image(img_file_path, width, height):
    img = Image.open(img_file_path)
    img = img.resize((width, height))
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    img.save(os.path.join(dir, 'resize_' + file_name))  # images/thumb_car.jpg

# Rotate Image
def rotate_image(img_file_path, degree):
    img = Image.open(img_file_path)
    # img = img.rotate(degree)
    img = img.rotate(degree, expand=True)
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    img.save(os.path.join(dir, 'rotate_' + file_name))  # images/thumb_car.jpg

# Type text on image
def draw_text_on_image(img_file_path, xPos, yPos, text, size, color):
    img = Image.open(img_file_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size)
    draw.text((xPos, yPos), text, color, font=font)
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    img.save(os.path.join(dir, 'text_' + file_name))  # images/thumb_car.jpg

# Apply filter
def apply_filter(img_file_path, filter):
    img = Image.open(img_file_path)
    img = img.filter(filter)
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    img.save(os.path.join(dir, filter.name + '_' + file_name))  # images/thumb_car.jpg


if __name__ == '__main__':
    img_info = get_info('비숑.jpg')
    ic(img_info)