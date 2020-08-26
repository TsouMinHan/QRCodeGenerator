import qrcode

# img = qrcode.make('Some data here')

# print(type(img))
# print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

# img.save('qrcode_test.png')


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# img = Image.open("qrcode_test.png")
# x1,y1,x2,y2=img.getbbox() 
# draw = ImageDraw.Draw(img)
# msg = "Sample Text"
# w, h = draw.textsize(msg)
# print(w,h)
# # # draw.text((x, y),"Sample Text",(r,g,b))
# draw.text(((x2-w)/2, 0),msg)
# img.save('sample-out.jpg')

from pathlib import Path
from datetime import datetime
def generator_picture(qrcode_text, up_text, down_text, left_text, right_text):
    img = qrcode.make(qrcode_text)
    img_wide, img_height = img.size

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("msjhbd.ttc", 30)

    # up_w, up_h = draw.textsize(up_text)
    # draw.text(((img_wide-up_w)/2, 0), up_text)
    
    down_w, down_h = draw.textsize(down_text, font=font)
    draw.text(((img_wide-down_w)/2, img_height-down_h), down_text,font=font)

    # left_w, left_h = draw.textsize(left_text)
    # draw.text(((img_wide/2-left_w)/2, 0), left_text)

    # right_w, right_h = draw.textsize(right_text)
    # draw.text((img_wide-(img_wide/2-left_w)/2, 0), right_text)

    img.save(Path("temp", f"{datetime.today().strftime('%Y%m%d%H%M%S')}.jpg"))

if __name__ == '__main__':
    # generator_picture("A", "sdf", "sss", "yji3", "u4")
    path = Path("web", "temp", "filename")

    print(f"{path.parts[1]}\\{path.parts[2]}")
    
