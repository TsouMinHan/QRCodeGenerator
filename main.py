from datetime import datetime
from PIL import ImageDraw 
from PIL import ImageFont
from PIL import Image
from pprint import pprint
from pathlib import Path
import qrcode
import eel

@eel.expose
# def generator_picture(qrcode_text, up_text, down_text, left_text, right_text):
def generator_picture(qrcode_text, down_text):
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

    file = Path("web", "temp", f"{datetime.today().strftime('%Y%m%d%H%M%S')}.jpg")
    img.save(file)

    return f"{file.parts[1]}\\{file.parts[2]}"

@eel.expose
def set_data():
    dc = {}

    dc["title"] = "QRCodeGenerator"

    return dc

def delete_temp_flie():
    path = Path(Path.cwd(), "web", "temp")

    for p in path.iterdir():
        p.unlink()

if __name__ == "__main__":   
    eel.init("web")
    try:
        eel.start("index.html", size=(1100, 600))

    except (SystemExit, MemoryError, KeyboardInterrupt):
        # We can do something here if needed
        # But if we don't catch these safely, the script will crash
        pass 
    
    delete_temp_flie()
