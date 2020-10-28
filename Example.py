################################################
#     PYTHON SCRIPT FOR SETTING THE DISPLAY CLOCKS
#
#     By: AUBIN HEFFERNAN
#
#     Using TKINTER you can set multiple clock instances based off your choosen offset
#     
##################################################
#
# Example: clock1_zone = 1    #this gives a 1 hour time difference
# Example: clock2_zone = -3   #this gives a -3 hour time difference
#
###################################################
#Change clock#_zones below
###################################################

clock_name = "LOCAL"
clock1_zone = 1
clock1_name = "NOT-LOCAL"
clock2_zone = 2
clock2_name = "NOT-LOCAL"
clock3_zone = 3
clock3_name = "NOT-LOCAL"
clock4_zone = -1
clock4_name = "NOT-LOCAL"
clock5_zone = -2
clock5_name = "NOT-LOCAL"
clock6_zone = -3
clock6_name = "NOT-LOCAL"
clock7_zone = 10
clock7_name = "NOT-LOCAL"


##########################################################
# STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP
##########################################################
# STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP
##########################################################

from tkinter import *
import time
from PIL import Image, ImageTk
import datetime as dt
import random


root = Tk()
root.geometry('2000x500+1500+00')
#root.wm_attributes('-fullscreen', 'true')
root.wm_state('zoomed')
root.overrideredirect(1)
root.bind('<Escape>',lambda e: root.destroy())
root.configure(bg='black')
 
timenow=''
#cframe =Frame(root, width=1920, height=500, bg='black', relief=GROOVE)
#cframe.pack()

##########################################################
#sizex=250
#sizey=180

#canvas = Canvas(root, width = (2*sizex), height = (2*sizey),bg = "black", bd= 0 , highlightthickness = 0)  
#img = Image.open("logo.JPG")
#img = img.resize((400, 360), Image.ANTIALIAS)   
#img = ImageTk.PhotoImage(img)
#canvas.create_image(sizex, sizey, image=img)
#canvas.grid(row=1,column=1,rowspan=5)

###########################################################
sizex=700
sizey=40

canvas2 = Canvas(root, width = (2*sizex), height = (2*sizey), bg= 'black')  
img2 = Image.open("hunter_ops.JPG")
img2 = img2.resize((800, 80), Image.ANTIALIAS)   
img2 = ImageTk.PhotoImage(img2)
canvas2.create_image(sizex, 50, image=img2)
canvas2.grid(row=1,column=2,columnspan=4)

############################################################
full_logo = Image.open("logo.JPG").convert("RGBA")
full_logo = full_logo.resize((400, 360), Image.ANTIALIAS) 
starsonly = Image.open("stars.JPG").convert("RGBA")
starsonly = starsonly.resize((400, 360), Image.ANTIALIAS) 
starsmotto = Image.open("stars_motto.JPG").convert("RGBA")
starsmotto = starsmotto.resize((400, 360), Image.ANTIALIAS) 
############################################################
class SimpleApp(object):
    def __init__(self, master, filename, width, height, xcoord, ycoord, rspan, cspan, resizeX, resizeY, **kwargs):
        self.master = master
        self.filename = filename
        self.width = width
        self.height = height
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.rspan = rspan
        self.cspan = cspan
        self.resizeX = resizeX
        self.resizeY = resizeY
        self.canvas = Canvas(master, width=self.width, height=self.height, bd= 0 , highlightthickness = 0, bg = 'black')
        self.canvas.grid(row=self.xcoord,column=self.ycoord, rowspan=self.rspan, columnspan=self.cspan)
        self.process_next_frame = self.draw().__next__  # Using "next(self.draw())" doesn't work
        master.after(1, self.process_next_frame)


    def draw(self):
        image = Image.open(self.filename)
        image = image.resize((self.resizeX, self.resizeY), Image.ANTIALIAS)
        angle = 0
        print(self.process_next_frame)
        oldtime=time.time()
        while True:
            if angle==0:
                if (int(time.time())%60 < 2):
                    angle+=1
                tkimage = ImageTk.PhotoImage(image.rotate(angle))
                canvas_obj = self.canvas.create_image(self.width/2, self.height/2, image=tkimage)
                self.master.after_idle(self.process_next_frame)
                yield
                self.canvas.delete(canvas_obj)
                #time.sleep(0.002)
            else:
                tkimage = ImageTk.PhotoImage(image.rotate(angle))
                canvas_obj = self.canvas.create_image(self.width/2, self.height/2, image=tkimage)
                self.master.after_idle(self.process_next_frame)
                yield
                self.canvas.delete(canvas_obj)
                angle += 1
                angle %= 360
                time.sleep(0.002)
                oldtime=time.time()
############################################################
def fadelogos(full_logo,starsonly,starsmotto):
    alpha = 0
    counter=0
    stimulation=random.randint(300,1500)
    while True:
        counter+=1
        if (counter==stimulation):
            alpha = 0
            counter=0
            stimulation=random.randint(300,1500)
        else:
            pass
        if 1.0 > alpha:
            new_img = Image.blend(full_logo,starsonly,alpha)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (360), bg= 'black')
            canvas2.create_image(250, 180, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.05
            time.sleep(.1)
            root.update()
        elif 2.0 > alpha:
            beta=alpha-1
            new_img = Image.blend(starsonly,starsmotto,beta)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (360), bg= 'black')
            canvas2.create_image(250, 180, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.05
            time.sleep(.1)
            root.update()
            pass
        elif 3.0 > alpha:
            beta=alpha-2
            new_img = Image.blend(starsmotto,full_logo,beta)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (360), bg= 'white')
            canvas2.create_image(250, 180, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            alpha = alpha + 0.05
            time.sleep(.1)
            root.update()
            pass
        else:
            time.sleep(.1)
            beta=1
            new_img = Image.blend(starsmotto,full_logo,beta)
            modifying_image = ImageTk.PhotoImage(new_img)
            canvas2 = Canvas(root, width = (500), height = (360), bg= 'white')
            canvas2.create_image(250, 180, image=modifying_image)
            canvas2.grid(row=1,column=1, rowspan=5)
            root.update()
            pass


###############################################################

clock=Label(root, padx=25, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= timenow,bg='#292929', relief= SUNKEN)
clock.grid(row=3,column=2)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock_name, bg ="black", relief= FLAT)
zone.grid(row=2,column=2)

clock1=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "",bg='#292929', relief= SUNKEN)
clock1.grid(row=3,column=3)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock1_name, bg ="black", relief= FLAT)
zone.grid(row=2,column=3)

clock2=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock2.grid(row=3,column=4)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock2_name, bg ="black", relief= FLAT)
zone.grid(row=2,column=4)

clock3=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock3.grid(row=3,column=5)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock3_name, bg ="black", relief= FLAT)
zone.grid(row=2,column=5)

clock4=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "both",bg='#292929', relief= SUNKEN)
clock4.grid(row=5,column=2)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock4_name, bg ="black", relief= FLAT)
zone.grid(row=4,column=2)

clock5=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock5.grid(row=5,column=3)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock5_name, bg ="black", relief= FLAT)
zone.grid(row=4,column=3)

clock6=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock6.grid(row=5,column=4)
zone=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock6_name, bg ="black", relief= FLAT)
zone.grid(row=4,column=4)

clock7=Label(root, padx=80, pady=10, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock7.grid(row=5,column=5)
zone7=Label(root, padx=2, pady=2, bd=3, fg= '#FFCA08',font=('arial',20,'bold'),text= clock7_name, bg ="black", relief= FLAT)
zone7.grid(row=4,column=5)

def timezoner(hours):
    global timenow
    oldtime=time.time()
    newtime=oldtime+(hours*3600)
    return time.strftime('%H: %M',time.localtime(newtime))

def timer():
    global timenow
    newtime = time.strftime('%H: %M: %S')
    if newtime != timenow:
        timenow= newtime
        clock.config(text= timenow)
        clock1.config(text= timezoner(clock1_zone))
        clock2.config(text= timezoner(clock2_zone))
        clock3.config(text= timezoner(clock3_zone))
        clock4.config(text= timezoner(clock4_zone))
        clock5.config(text= timezoner(clock5_zone))
        clock6.config(text= timezoner(clock6_zone))
        clock7.config(text= timezoner(clock7_zone))
    clock.after(200, timer)
timer()
fadelogos(full_logo,starsonly,starsmotto)
#app = SimpleApp(root, 'logo.JPG',500,360,1,1,5,1,350,350)
root.mainloop()
