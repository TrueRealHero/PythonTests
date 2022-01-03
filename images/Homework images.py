import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_PATH = sys.path[0] + '/'
FILE_PATH = BASE_PATH + '/source-images/'
SAVE_PATH = BASE_PATH + '/output-images/'
if not os.path.exists(SAVE_PATH):
    os.mkdir(BASE_PATH + "output-images")
FONT_SIZE = 28
FONT = ImageFont.truetype("segoesc", FONT_SIZE)
ALL_FILES = os.listdir(FILE_PATH)
EXTENTION = ('.jpg')

for files in ALL_FILES:
    if files.lower().endswith(EXTENTION):
        filename = files.split('.')[0]
        new_files = Image.open(FILE_PATH + files)
        width, height = new_files.size
        watermarked_files = ImageDraw.Draw(new_files)
        text_width, text_height = watermarked_files.textsize(filename, FONT)
        x = width - text_width - 10
        y = height - text_height - 10
        watermarked_files.text((x,y), filename, font=FONT)
        new_files.save(os.path.join(SAVE_PATH, files))