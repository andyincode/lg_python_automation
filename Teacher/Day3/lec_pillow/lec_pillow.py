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
             'Mode':img.mode})

if __name__ == '__main__':
    img_info = get_info('')