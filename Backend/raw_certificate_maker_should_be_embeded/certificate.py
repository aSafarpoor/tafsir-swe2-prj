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

def make_certificate(first_name,last_name,passed_day,course_name,teacher_name):
    
    fontFile = "raw_certificate_maker_should_be_embeded/TAHOMAB0.TTF"
   
    # this was a 400x400 jpg file
    # imageFile = "tmp.png"

    imageFile="raw_certificate_maker_should_be_embeded/images.jpeg"

    # load the font and image
    font = ImageFont.truetype(fontFile, 18)

    image = Image.open(imageFile)

    # firts you must prepare your text (you dont need this for english text)
    #text =  "\n\n"+"        "+first_name+" "+last_name+"\n      "+passed_day+"\n        "+course_name+"\n       "+teacher_name

    text="\n"*11+first_name+ " "+last_name+" "*(140-2*(len(first_name)+len(last_name)))

    text+="\n"*3+course_name+" "*(200-2*(len(course_name)))
    text+="\n"*3+teacher_name+" "*(180-2*(len(teacher_name)))
    print("lol")
    text+="\n"*3+str(passed_day)+" "*(160)
   
    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)           # correct its direction

    

    # start drawing on image
    draw = ImageDraw.Draw(image)
    draw.text((0,0), bidi_text, (255,0,255), font=font)
    draw = ImageDraw.Draw(image)

    name=str(randint(1,99999999999))+".pdf"
    adrs="media/folanja/certificate/"+name
    # save it
    # image.save("raw_certificate_maker_should_be_embeded/media/output.png",resolution=100.0)
    image.save(adrs,resolution=100.0)
    return adrs
    # imageFile="raw_certificate_maker_should_be_embeded/media/output.pdf"
    
    # return imageFile

# print(make_certificate("علی" ,"صفرپور","1392/01/14" , " تاریخ صدر اسلام", "حجت الاسلام مجتهدی"))


