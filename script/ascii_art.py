from PIL import Image

image = Image.open("image.jpg")

longueur = int(input('quelle longueure en px (entre 0 et 100) ? - '))
largeur = int(longueur * float(image.height/image.width))
image = image.resize((longueur, largeur))

liste = [' ','.',':','-','=','+','*','#','%','@']

print(len(liste))

content = ''

for y in range(image.height):
    for x in range(image.width):
        
        (r, g, b) = image.getpixel((x,y))
        gris = int((r+g+b)/3)
        #print(gris)
        
        if   gris <= 1*255/10 : caractere = liste[9]
        elif gris <= 2*255/10 : caractere = liste[8]
        elif gris <= 3*255/10 : caractere = liste[7]
        elif gris <= 4*255/10 : caractere = liste[6]
        elif gris <= 5*255/10 : caractere = liste[5]
        elif gris <= 6*255/10 : caractere = liste[4]
        elif gris <= 7*255/10 : caractere = liste[3]
        elif gris <= 8*255/10 : caractere = liste[2]
        elif gris <= 9*255/10 : caractere = liste[8]
        elif gris <= 10*255/10 : caractere = liste[9]
        
        
        content += str(caractere) + '_'
    
    content += '\n'

with open("image.txt",'a') : pass
with open("image.txt",'w') as fic:
    fic.write(content)

print(content)
input()