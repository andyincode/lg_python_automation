from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import os
from icecream import ic

# Get File Information
from pygments.formatters import img


def get_info(img_file_path):
    img = Image.open(img_file_path)
    ic(img)
    return ({'FileName':img.filename,
             'Format':img.format,
             'Format Desc':img.format_description,
             'Width':img.width,
             'Height':img.height,
             'Mode':img.mode})

# Convert Image Format
def convert_format(img_file_path, format):
    img = Image.open(img_file_path)
    path = img_file_path[:-3] # images/car.jpg -> images/car
    path += format
    img.save(path)

# Make Thumbnail Image
# 주어진 길이값을 기준으로 이미지의 가로/세로 중 큰값을 기준으로 작은 값을 비율에 맞게 조절
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
def rotate_image(img_file_path, degree, is_keep_size=True):
    img = Image.open(img_file_path)
    # img = img.rotate(degree)
    img = img.rotate(degree, expand=is_keep_size)
    dir = os.path.dirname(img_file_path)  # images/car.jpg -> imgaes/
    file_name = os.path.basename(img_file_path)  # car.jpg
    file_name = 'rotate_%s_' % degree + file_name
    img.save(os.path.join(dir, file_name))  # images/thumb_car.jpg

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

# Merge Image
class MergeImage:
    # W x H 사이즈 설정
    def set_matrix(self, rows, columns):
        self.rows = rows
        self.columns = columns

    # 기본 사이즈 설정
    def set_default_image_size(self, width, height):
        self.width = width
        self.height = height

    # Merge 할 빈 이미지 생성
    def create_merged_image(self):
        self.new_image = Image.new('RGB', (self.width * self.columns, self.height * self.rows))

    # 특정 row, column에 이미지 붙여넣기
    def paste_image(self, row, column, img_file_path):
        img = Image.open(img_file_path)
        self.new_image.paste(img, (self.width * column, self.height * row))

    # 이미지 저장
    def save(self, img_file_path):
        self.new_image.save(img_file_path)

if __name__ == '__main__':
    img_file_path = 'car.jpg'

    ########################################################################################
    # 이미지 정보 출력
    ic(get_info(img_file_path))

    ########################################################################################
    # 이미지 포맷 변경
    convert_format(img_file_path, 'png')
    ic(get_info('car.png'))
    convert_format(img_file_path, 'bmp')
    ic(get_info('car.bmp'))

    ########################################################################################
    # 썸네일 이미지 만들기
    make_thumbnail(img_file_path, width=100, height=100)

    ########################################################################################
    # 이미지 잘라내기
    crop_image(img_file_path, 100, 100, 200, 200)

    ########################################################################################
    # 이미지 크기변경
    resize_image(img_file_path, 100, 100)

    ########################################################################################
    # 이미지 회전
    rotate_image(img_file_path, 90)
    rotate_image(img_file_path, 180)
    rotate_image(img_file_path, 270)
    rotate_image(img_file_path, 90, False)
    rotate_image(img_file_path, 180, False)
    rotate_image(img_file_path, 270, False)

    ########################################################################################
    # 이미지에 글쓰기
    draw_text_on_image(img_file_path, 500, 500, 'Hello World', 20, 'red')

    ########################################################################################
    # 필터적용
    filter_list = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL,
                   ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.FIND_EDGES,
                   ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]
    for filter in filter_list:
        apply_filter(img_file_path, filter)

    ########################################################################################
    # 이미지 합치기
    img_file_path = 'resize_car.jpg'

    row = 2
    column = 3
    merge = MergeImage()
    merge.set_matrix(row, column)
    merge.set_default_image_size(100, 100)
    merge.create_merged_image()
    count = 0
    for _row in range(row):
        for _column in range(column):
            merge.paste_image(_row, _column, img_file_path)
    merge.save('merge_car.jpg')
