from tkinter import *
from PIL import Image, ImageTk
import time
root = Tk()
root.geometry('1000x1000+1500+00')
#root.wm_attributes('-fullscreen', 'true')
root.wm_state('zoomed')
root.overrideredirect(1)
root.bind('<Escape>',lambda e: root.destroy())
root.configure(bg='black')

full_logo = Image.open("logo.JPG").convert("RGBA")
full_logo = full_logo.resize((400, 360), Image.ANTIALIAS) 
starsonly = Image.open("stars.JPG").convert("RGBA")
starsonly = starsonly.resize((400, 360), Image.ANTIALIAS) 
starsmotto = Image.open("stars_motto.JPG").convert("RGBA")
starsmotto = starsmotto.resize((400, 360), Image.ANTIALIAS) 


def fadelogos(full_logo,starsonly,starsmotto):
    alpha = 0
    while True:
        if 1.0 > alpha:
            new_img = Image.blend(full_logo,starsonly,alpha)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (500), bg= 'black')
            canvas2.create_image(250, 250, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.1
            time.sleep(.1)
            root.update()
        elif 2.0 > alpha:
            beta=alpha-1
            new_img = Image.blend(starsonly,starsmotto,beta)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (500), bg= 'black')
            canvas2.create_image(250, 250, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.1
            time.sleep(.1)
            root.update()
            pass
        elif 3.0 > alpha:
            beta=alpha-2
            new_img = Image.blend(starsmotto,full_logo,beta)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (500), bg= 'black')
            canvas2.create_image(250, 250, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.1
            time.sleep(.1)
            root.update()
            pass
        else:
            time.sleep(.1)
            root.update()
            alpha = 0 
            pass


fadelogos(full_logo,starsonly,starsmotto)

root.mainloop()