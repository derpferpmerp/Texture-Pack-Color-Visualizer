from PIL import Image,ImageDraw,ImageFont
from sty import fg, bg, ef, rs
from pprint import pprint
import sys


im = Image.open("image.jpg", "r")
width, height = im.size
pixel_values = list([list(x) for x in list(im.getdata())])
pixel_values_tup=list(im.getdata())
print(f"Pixels: {len(pixel_values)}")


fstr=""
count= 0
lstallwidths = []

WIDTH = 600
HEIGHT = 400
#img = Image.open("image.jpg")
img = Image.new('RGB', (600, 400), color = (255, 255, ))
d = ImageDraw.Draw(img)
img.save("pil_v1.jpg")

for g in range(1,HEIGHT):
	lstallwidths.append(WIDTH * g)


heightval = 0
WIDTHITER = 0
lstnotblack=[]
for bc in range(WIDTH):
	print(f"Doing Row {bc}")
	for hexvaliter in range(HEIGHT):
		hexval = pixel_values[bc*hexvaliter]
		character = "#"
		coloredchar = fg(int(hexval[0]),int(hexval[1]),int(hexval[2]))+character+fg.rs

		d.text((bc*5,5*hexvaliter), character, fill=pixel_values_tup[hexvaliter])
		if sum(hexval) > 0:
			lstnotblack.append(hexval)
		fstr += coloredchar

#print(fstr)
img.save('pil_text.jpg')
pprint(lstnotblack)