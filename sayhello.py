'''python code to add text in the image by using PIL(Python Image Library module)
	The program adds name in the image hello.jpg
'''

from PIL import Image, ImageFont, ImageDraw
#assigning array for generating multiple files with different text
names=["Aastha","Vedansh","Sneha"]

for name in names:
	#opening an image file
	source_img = Image.open("hello.jpg").convert("RGBA")
	draw= ImageDraw.Draw(source_img)
	#specifying cordinates,value, font and color of the text 
	draw.text((814,838),name,font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",size=110),fill="black")
	#saving the image
	source_img.save("./"+name+".jpeg", "JPEG")

