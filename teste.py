from tkinter import *
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
from tkinter import filedialog, messagebox
from pathlib import Path

root = Tk()
root.title("Image Editor")
root.geometry("800x700+250+5")
root.configure(bg="#212121")
root.resizable(width=True, height=True)
img_no = 0
filename = ["" for x in range(150)]
filename[0] = "noFile"


def openfn():
    file = filedialog.askopenfilename(title='open')
    return file


def open_img():
    x = openfn()
    img = Image.open(x)
    firstName = Path(x).stem
    width, height = img.size
    ratio = round(width/height, 3)
    fra = round(ratio, 3)
    if width > height:
        newHeight = round(650/fra)
        img.resize((650, newHeight), Image.ANTIALIAS).save('img.png')
    else:
        newWidth = round(650*fra)
        img.resize((newWidth, 650), Image.ANTIALIAS).save('img.png')
    global filename, img_no
    img_no = img_no + 1
    filename[img_no] = "img.png"
    img = Image.open(filename[img_no])
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=150, y=40)

    def update_img():
        global filename, img_no
        img_enhance = Image.open(filename[img_no])
        img_enhance = ImageTk.PhotoImage(img_enhance)
        panel = Label(root, image=img_enhance)
        panel.configure(image=img_enhance)
        panel.image = img_enhance

    def undo_change():
        global filename, img_no
        img_no = img_no - 1
        if img_no < 1:
            img_no = 1
        img_enhance = Image.open(filename[img_no])
        img_enhance = ImageTk.PhotoImage(img_enhance)
        panel.configure(image=img_enhance)
        panel.image = img_enhance

    def save_img():
        global filename, img_no
        img = Image.open(filename[img_no])
        path = "C:\\Users\\kushm\\Downloads\\" #change your path here
        img.save(path + firstName + "_edited.png")
        messagebox.showinfo("information", "Your Image is Saved in your desired location", )

    def sharpness_img():
        global filename, img_no
        img_enhance = Image.open(filename[img_no])
        enhancer = ImageEnhance.Sharpness(img_enhance)
        img_no = img_no + 1
        enhancer.enhance(2).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def blur_img():
        global filename, img_no
        img_enhance = Image.open(filename[img_no])
        enhancer = ImageEnhance.Sharpness(img_enhance)
        img_no = img_no + 1
        enhancer.enhance(0).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def flip_horizontal_img():
        global filename, img_no
        img_flipH = Image.open(filename[img_no])
        img_no = img_no + 1
        img_flipH.transpose(Image.FLIP_LEFT_RIGHT).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def flip_vertical_img():
        global filename, img_no
        img_flipV = Image.open(filename[img_no])
        img_no = img_no + 1
        img_flipV.transpose(Image.FLIP_TOP_BOTTOM).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def grayscale_img():
        global filename, img_no
        img_grayscale = Image.open(filename[img_no])
        color = ImageEnhance.Color(img_grayscale)
        img_no = img_no + 1
        color.enhance(0).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def brighten_img():
        global filename, img_no
        img_brighten = Image.open(filename[img_no])
        img_brighten = ImageEnhance.Brightness(img_brighten)
        img_no = img_no + 1
        img_brighten.enhance(1.1).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def contrast_img():
        global filename, img_no
        img_contrast = Image.open(filename[img_no])
        img_contrast = ImageEnhance.Contrast(img_contrast)
        img_no = img_no + 1
        img_contrast.enhance(1.1).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def smooth_img():
        global filename, img_no
        img_smooth = Image.open(filename[img_no])
        img_no = img_no + 1
        img_smooth.filter(ImageFilter.SMOOTH).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def contour_img():
        global filename, img_no
        img_contour = Image.open(filename[img_no])
        img_no = img_no + 1
        img_contour.filter(ImageFilter.CONTOUR).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def emboss_img():
        global filename, img_no
        img_emboss = Image.open(filename[img_no])
        img_no = img_no + 1
        img_emboss.filter(ImageFilter.EMBOSS).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()

    def edge_img():
        global filename, img_no
        img_edge = Image.open(filename[img_no])
        img_no = img_no + 1
        img_edge.filter(ImageFilter.FIND_EDGES).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        update_img()


    Button(root, text='save image', height="1", width="15", bg="#424242", fg="#ffffff", bd="0", command=save_img).place(x=115, y=2)
    Button(root, text='undo', height="1", width="15", bg="#424242", fg="#ffffff", bd="0", command=undo_change).place(x=228, y=2)

    Button(root, text='sharpen', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=sharpness_img).place(x=2, y=250)
    Button(root, text='blur', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=blur_img).place(x=2, y=275)
    Button(root, text='flip hori', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=flip_horizontal_img).place(x=2, y=300)
    Button(root, text='flip vert', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=flip_vertical_img).place(x=2, y=325)
    Button(root, text='grayscale', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=grayscale_img).place(x=2, y=350)
    Button(root, text='brighten', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=brighten_img).place(x=2, y=375)
    Button(root, text='contrast', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=contrast_img).place(x=2, y=400)
    Button(root, text='smooth', height="1", width="10", bg="#424242", fg="#ffffff", bd="0",command=smooth_img).place(x=2, y=425)
    Button(root, text='contour', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=contour_img).place(x=2, y=450)
    Button(root, text='emboss', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=emboss_img).place(x=2, y=475)
    Button(root, text='edge', height="1", width="10", bg="#424242", fg="#ffffff", bd="0", command=edge_img).place(x=2, y=500)


Button(root, text='open image', height="1", width="15", bg="#424242", fg="#ffffff", bd="0", command=open_img).place(x=2, y=2)


root.mainloop()