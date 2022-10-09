# import io
# from typing import List
# from PIL import Image, ImageDraw, ImageFont

# from fastapi.param_functions import File
# # from app.models.schemas.words import (
# #     WordOutWithIdDate
# # )
# from app.resources import strings
# # import datetime as dt
# # from O365 import calendar
# from app.core.config import settings

# import textwrap

# """ Return byte buffer if output=='__buffer', else export file 'output' @"""
# def create_bitmap_from_word(word: WordOutWithIdDate, output="temp.bmp"):

#     out = Image.new("1", (800, 480), 255)

#     fmb60 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
#                                "freemono/FreeMonoBold.ttf", 60)
#     fm30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER + "freemono/FreeMono.ttf", 30)
#     fmi30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
#                                "freemono/FreeMonoOblique.ttf", 30)
#     fmb30 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
#                                "freemono/FreeMonoBold.ttf", 30)
#     fmi15 = ImageFont.truetype(strings.PATH_FONTS_FOLDER +
#                                "freemono/FreeMonoOblique.ttf", 15)

#     # get a drawing context
#     d = ImageDraw.Draw(out)

#     d.text((5, 5), word.word, font=fmb60, fill=0)
#     d.text((5, 60), word.type, font=fmi30, fill=0)
#     d.line((0, 100, 800, 100), fill=0)
#     # ---------------------------------------------
#     d.text((5, 120), word.fullword, font=fm30, fill=0)
#     # d.multiline_text((5, 160), word.content, font=fmb30, fill=0)
#     offset = 0
#     count = 0
#     for line in textwrap.wrap(str(word.content), break_long_words=False, width=43):
#         # print(line)
#         d.text((5, 160 + offset), line, font=fm30, fill=0)
#         offset += fm30.getsize(line)[1]
#         count += 1
#         if count==9:
#             break
#     d.line((0, 435, 800, 435), fill=0)
#     # ---------------------------------------------
#     d.text((5, 445), "Last update: " +
#            word.updated_at.strftime("%m/%d/%Y, %H:%M:%S"),
#            font=fmi15, fill=0
#            )

#     if output == "__buffer":
#         img_byte_arr = io.BytesIO()
#         out.save(img_byte_arr, format='bmp')
#         img_byte_arr = img_byte_arr.getvalue()
#         return img_byte_arr
#     elif output == "__image_object":
#         return out
#     else:
#         out.save(settings.STATIC_DATA_DIR + output)

# # TODO: improve converting and resizing quality. Check "change" pictures in static folders
# # For now, stick with: convert to black-white before POST to server.
# # https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap


# def process_bitmap_from_file(file: File, output="temp.bmp"):

#     out = Image.open(io.BytesIO(file))
#     o2 = out.convert('1').resize((800, 480))

#     if output == "__buffer":
#         img_byte_arr = io.BytesIO()
#         o2.save(img_byte_arr, format='bmp')
#         img_byte_arr = img_byte_arr.getvalue()
#         return img_byte_arr
#     else:
#         o2.save(settings.STATIC_DATA_DIR + output, format='bmp')

