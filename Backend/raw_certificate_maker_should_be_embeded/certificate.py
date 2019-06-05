from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

# img = Image.open("certificate.png")
# draw = ImageDraw.Draw(img)


# selectFont = ImageFont.truetype("TAHOMAB0.TTF", size = 60)


# text="passed greate"
# x=10
# y=10
# r,g,b=0,0,250

# draw.text( (x,y), text, (r,g,b), font=selectFont)
# # (x,y) is the starting position for the draw object
# # text is the text to be entered
# # (r,g,b) represents the color eg (255,0,0) is Red
# # font is used to specify the Font object


# x = np.array(img)
# r, g, b, a = np.rollaxis(x, axis=-1)
# r[a == 0] = 0#color[0]
# g[a == 0] = 100#color[1]
# b[a == 0] = 1000#color[2] 
# x = np.dstack([r, g, b, a])
# img=Image.fromarray(x, 'RGB')

# img.save( 'kir.PNG', "PNG", resolution=100.0)


# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

# install: pip install Pillow
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
def make_certificate(first_name,last_name,passed_day,course_name,teacher_name):
    # use a good font!
    fontFile = "TAHOMAB0.TTF"

    # this was a 400x400 jpg file
    # imageFile = "tmp.png"
    imageFile="images.jpeg"

    # load the font and image
    font = ImageFont.truetype(fontFile, 18)
    image = Image.open(imageFile)

    # firts you must prepare your text (you dont need this for english text)
    #text =  "\n\n"+"        "+first_name+" "+last_name+"\n      "+passed_day+"\n        "+course_name+"\n       "+teacher_name
    
    text="\n"*11+first_name+ " "+last_name+" "*(140-2*(len(first_name)+len(last_name)))
    text+="\n"*3+course_name+" "*(200-2*(len(course_name)))
    text+="\n"*3+teacher_name+" "*(180-2*(len(teacher_name)))
    text+="\n"*3+passed_day+" "*(160)

    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)           # correct its direction


    

    # start drawing on image
    draw = ImageDraw.Draw(image)
    draw.text((0,0), bidi_text, (255,0,255), font=font)
    draw = ImageDraw.Draw(image)

    # save it
    image.save("output.png",resolution=100.0)
    image.save("output.pdf",resolution=100.0)
make_certificate("علی" ,"صفرپور","1392/01/14" , " تاریخ صدر اسلام", "حجت الاسلام مجتهدی")