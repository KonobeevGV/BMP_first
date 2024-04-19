import random
from PIL import Image, ImageDraw  
import sys
print ("Программа:", "/"+sys.argv[0][:4])
print (f"Редактируем изображениe {sys.argv[1]}, используя {sys.argv[2]}")
print ("Сохраняем изображение в файл: ", sys.argv[3])
image = Image.open(sys.argv[1])
image2 = Image.open(sys.argv[2])
draw = ImageDraw.Draw(image)  
width = image.size[0]  
height = image.size[1]  
width2 = image2.size[0]  
height2 = image2.size[1]  
w=min(width, width2)
h=min(height, height2)
pix = image.load() 
pix2 = image2.load() 

for i in range(w):
	for j in range(h):
	    a = pix[i, j][0]
	    b = pix[i, j][1]
	    c = pix[i, j][2]
	    a1 = pix2[i, j][0]
	    b1 = pix2[i, j][1]
	    c1 = pix2[i, j][2]
	    if a1==0 and b1==0 and c1==0:
	        draw.point((i, j), (0, 0, 0))
	    else:
		     draw.point((i, j), (a, b, c))
image.save(sys.argv[3])
del draw
