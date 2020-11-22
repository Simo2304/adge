from PIL import Image,ImageDraw,ImageFont


image = Image.open('idk.png')
font_type = ImageFont.truetype("arial.ttf", 15)
draw = ImageDraw.Draw(image)
draw.text(xy=(100,20),fill=(0,0,0), text= "confused screaming", font = font_type)


image.show()
