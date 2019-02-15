from PIL import Image, ImageFont, ImageDraw
names=["Aastha","Vedansh","Sneha"]

for name in names:
	source_img = Image.open("hello.jpg").convert("RGBA")
	draw= ImageDraw.Draw(source_img)

	draw.text((814,838),name,font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",size=110),fill="black")

	source_img.save("./"+name+".jpeg", "JPEG")

