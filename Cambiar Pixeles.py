from PIL import Image, ImageDraw
import random

file='Paisaje.jpg'
img = Image.open(file)
C1 = (240,120)
C2 = (430,750)

draw = ImageDraw.Draw(img)


if (C1[0] > C2[0]) or (C1[1] > C2[1]):
    print("Las primeras coordenadas deben ser de la esquina superior izquierda")
elif ((C1[0] or C2[0]) > img.width) or ((C1[1] or C2[1]) > img.height):
    print("Las coordenadas deben ser menor al tamaño de la imagen")
else:
    for x in range(C1[0], C2[0]):
        for y in range(C1[1], C2[1]):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            
            draw.point((x, y), (red, green, blue))
    img.show()
    
    

        
