from tkinter import *
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
from tkinter import filedialog, messagebox
from pathlib import Path
import cv2 
import numpy as np

# definindo propriedades do front-end
root = Tk()
root.title("Sistema de Manipulação de Imagens")
root.geometry("900x700+250+5")
root.configure(bg="#404040")
root.resizable(width=True, height=True)
img_no = 0
filename = ["" for x in range(150)]
filename[0] = "noFile"
panel = Label(root, image=None)

def openfilename():
    file = filedialog.askopenfilename(title='abrir')
    return file

def openimage():
    x = openfilename()
    img = Image.open(x)
    fileNameWithoutExtension = Path(x).stem
    width, height = img.size
    ratio = round(width/height, 3)
    fra = round(ratio, 3)
    if width > height:
        newHeight = round(650/fra)
        img.resize((650, newHeight)).save('img.png')
    else:
        newWidth = round(650*fra)
        img.resize((newWidth, 650)).save('img.png')
    global filename, img_no
    img_no = img_no + 1
    filename[img_no] = "img.png"
    img = Image.open(filename[img_no])
    img = ImageTk.PhotoImage(img)
    #front-end
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=150, y=40)

def updateimage():
    global filename, img_no
    img_enhance = Image.open(filename[img_no])
    img_enhance = ImageTk.PhotoImage(img_enhance)
    panel = Label(root, image=img_enhance)
    panel.configure(image=img_enhance)  # Atualiza a imagem no Label existente
    panel.image = img_enhance

def grayscaleimage():
    global filename, img_no
    img_grayscale = Image.open(filename[img_no])
    color = ImageEnhance.Color(img_grayscale)
    img_no = img_no + 1
    color.enhance(0).save(str(img_no)+'.png')
    filename[img_no] = str(img_no)+'.png'
    updateimage()

def rotateimage():
    global filename, img_no
    img_rotate = Image.open(filename[img_no])
    img_rotated = img_rotate.rotate(90, expand=True, resample=Image.BILINEAR)
    img_no = img_no +1
    img_rotated.save(str(img_no) + '.png')
    filename[img_no] = str(img_no) + '.png'
    updateimage()

def MinImage():
    global filename, img_no
    img = Image.open(filename[img_no])
    width, height = img.size
    newHeight = int (height*0.5)
    newWidth = int (width*0.5)
    imageMin = img.resize((newWidth,newHeight), Image.BILINEAR)
    imageMin.save("imagemmin.png")
    img_no = img_no + 1
    filename[img_no] = ("imagemin.png")
    updateimage()

def MaxImage():
    global filename, img_no
    img = Image.open(filename[img_no])
    width, height = img.size
    newHeight = int (height*2)
    newWidth = int (width*2)
    imageMin = img.resize((newWidth,newHeight), Image.BILINEAR)
    imageMin.save("imagemmax.png")
    img_no = img_no + 1
    filename[img_no] = ("imagemax.png")
    updateimage()

def translationImage():
    global filename,img_no
    imagem = cv2.imread(filename[img_no])

    # Define o deslocamento desejado (25 pixels para direita e 50 pixels para baixo)
    deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])

    # Aplica a translação usando o método warpAffine
    imagem_transladada = cv2.warpAffine(imagem, deslocamento, (imagem.shape[1]+25, imagem.shape[0]+50),cv2.INTER_LINEAR)

    # salva a imagem e exiba ela na interface
    cv2.imwrite("imagem_transladada.png", imagem_transladada)
    img_no = img_no +1
    filename[img_no] = ("imagem_transladada.png")
    updateimage()

Button(root, text='Abrir Imagem', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=openimage).place(x=2, y=2)
Button(root, text='Escala de Cinza', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=grayscaleimage).place(x=2, y=350)
Button(root, text='rotacionar', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=rotateimage).place(x=2, y=400)
Button(root, text='minimizar', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=MinImage).place(x=2, y=450)
Button(root, text='maximizar', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=MaxImage).place(x=2, y=500)
Button(root, text='transladar', height="1", width="15", bg="#04BF68", fg="#ffffff", bd="0", cursor="hand2", font="Montserrat", command=translationImage).place(x=2, y=550)

root.mainloop()