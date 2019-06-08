from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np


# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

# install: pip install Pillow
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import randint

def make_certificate(first_name,last_name,passed_day,course_name,teacher_name,pic):
   
    fontFile = "raw_certificate_maker_should_be_embeded/B Koodak Bold.ttf"
   
    # this was a 400x400 jpg file
    # imageFile = "tmp.png"
    print("hello")
    # imageFile="raw_certificate_maker_should_be_embeded/images2.jpeg"
    imageFile="raw_certificate_maker_should_be_embeded/images.jpg"
    # load the font and image
    
    font = ImageFont.truetype(fontFile, 66)
    
    image = Image.open(imageFile)
    
    text="\n"*32+" گواهی میشود آقا/خانم "+first_name+" "+last_name+" "*(178-(23+len(first_name)+len(last_name)))
    text+="\n\n"+" دوره "+course_name+" "+" "*(193-len(course_name)-6)
    text+="\n\n"+" ارائه شده توسط "+teacher_name+ " "*(155-len(teacher_name))
    text+="\n"*2+" را در تاریخ "+str(passed_day[1:-1])+" "*(162)
    text+="\n\n"+"با موفقیت گذرانده است"+"."+" "*165

    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)           # correct its direction

    

    # start drawing on image
    draw = ImageDraw.Draw(image)
    draw.text((0,0), bidi_text, (255,0,255), font=font)
    draw = ImageDraw.Draw(image)
    
    image2 = Image.open(pic)
    
    image2 = image2.resize( (380,500), Image.ANTIALIAS) 
    # img = Image.open('/path/to/file'?, 'r')
    img_w, img_h = image2.size
    background = image#Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 9, (bg_h - img_h) // 3)
    background.paste(image2, offset)
    # background.save('outttt.png')

    name=str(randint(1,99999999999))+".pdf"
    adrs="media/folanja/certificate/"+name
    # save it
    print(pic)

    # image.save("raw_certificate_maker_should_be_embeded/media/output.png",resolution=100.0)
    image.save(adrs,resolution=100.0)
    
    return adrs
    # imageFile="raw_certificate_maker_should_be_embeded/media/output.pdf"
    
    # return imageFile

# print(make_certificate("علی" ,"صفرپور","1392/01/14" , " تاریخ صدر اسلام", "حجت الاسلام مجتهدی"))


