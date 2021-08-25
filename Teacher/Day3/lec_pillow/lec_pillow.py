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
"""
Make this image into a thumbnail.  This method modifies the
image to contain a thumbnail version of itself, no larger than
the given size.  This method calculates an appropriate thumbnail
size to preserve the aspect of the image, calls the
:py:meth:`~PIL.Image.Image.draft` method to configure the file reader
(where applicable), and finally resizes the image.

Note that this function modifies the :py:class:`~PIL.Image.Image`
object in place.  If you need to use the full resolution image as well,
apply this method to a :py:meth:`~PIL.Image.Image.copy` of the original
image.

:param size: Requested size.
:param resample: Optional resampling filter.  This can be one
   of :py:data:`PIL.Image.NEAREST`, :py:data:`PIL.Image.BOX`,
   :py:data:`PIL.Image.BILINEAR`, :py:data:`PIL.Image.HAMMING`,
   :py:data:`PIL.Image.BICUBIC` or :py:data:`PIL.Image.LANCZOS`.
   If omitted, it defaults to :py:data:`PIL.Image.BICUBIC`.
   (was :py:data:`PIL.Image.NEAREST` prior to version 2.5.0).
   See: :ref:`concept-filters`.
:param reducing_gap: Apply optimization by resizing the image
   in two steps. First, reducing the image by integer times
   using :py:meth:`~PIL.Image.Image.reduce` or
   :py:meth:`~PIL.Image.Image.draft` for JPEG images.
   Second, resizing using regular resampling. The last step
   changes size no less than by ``reducing_gap`` times.
   ``reducing_gap`` may be None (no first step is performed)
   or should be greater than 1.0. The bigger ``reducing_gap``,
   the closer the result to the fair resampling.
   The smaller ``reducing_gap``, the faster resizing.
   With ``reducing_gap`` greater or equal to 3.0, the result is
   indistinguishable from fair resampling in most cases.
   The default value is 2.0 (very close to fair resampling
   while still being faster in many cases).
:returns: None
"""
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
"""
Returns a resized copy of this image.

:param size: The requested size in pixels, as a 2-tuple:
   (width, height).
:param resample: An optional resampling filter.  This can be
   one of :py:data:`PIL.Image.NEAREST`, :py:data:`PIL.Image.BOX`,
   :py:data:`PIL.Image.BILINEAR`, :py:data:`PIL.Image.HAMMING`,
   :py:data:`PIL.Image.BICUBIC` or :py:data:`PIL.Image.LANCZOS`.
   If the image has mode "1" or "P", it is always set to
   :py:data:`PIL.Image.NEAREST`.
   If the image mode specifies a number of bits, such as "I;16", then the
   default filter is :py:data:`PIL.Image.NEAREST`.
   Otherwise, the default filter is :py:data:`PIL.Image.BICUBIC`.
   See: :ref:`concept-filters`.
:param box: An optional 4-tuple of floats providing
   the source image region to be scaled.
   The values must be within (0, 0, width, height) rectangle.
   If omitted or None, the entire source is used.
:param reducing_gap: Apply optimization by resizing the image
   in two steps. First, reducing the image by integer times
   using :py:meth:`~PIL.Image.Image.reduce`.
   Second, resizing using regular resampling. The last step
   changes size no less than by ``reducing_gap`` times.
   ``reducing_gap`` may be None (no first step is performed)
   or should be greater than 1.0. The bigger ``reducing_gap``,
   the closer the result to the fair resampling.
   The smaller ``reducing_gap``, the faster resizing.
   With ``reducing_gap`` greater or equal to 3.0, the result is
   indistinguishable from fair resampling in most cases.
   The default value is None (no optimization).
:returns: An :py:class:`~PIL.Image.Image` object.
"""
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
    img_file_path = 'car.jpg'