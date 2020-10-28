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
clock1_zone = 1
clock2_zone = 2
clock3_zone = 3
clock4_zone = -1
clock5_zone = -2
clock6_zone = -3
clock7_zone = 10


##########################################################
# STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP
##########################################################
# STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP
##########################################################

from tkinter import *
import time
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

canvas = Canvas(root, width = 150, height = 150)      
canvas.grid(row=1, column=1)      
img = PhotoImage(file="logo.JPG")      
canvas.create_image(20,20, anchor=NW, image=img)

clock=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= timenow,bg='#292929', relief= SUNKEN)
clock.grid(row=2,column=1)

clock1=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "",bg='#292929', relief= SUNKEN)
clock1.grid(row=2,column=2)

clock2=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock2.grid(row=2,column=3)

clock3=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock3.grid(row=2,column=4)

clock4=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "both",bg='#292929', relief= SUNKEN)
clock4.grid(row=3,column=1)

clock5=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock5.grid(row=3,column=2)

clock6=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock6.grid(row=3,column=3)

clock7=Label(root, padx=25, pady=40, bd=3, fg= '#FFCA08',font=('arial',48,'bold'),text= "test",bg='#292929', relief= SUNKEN)
clock7.grid(row=3,column=4)

def timezoner(hours):
    global timenow
    oldtime=time.time()
    newtime=oldtime+(hours*3600)
    return time.strftime('%H: %M: %S',time.localtime(newtime))

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
 
 
root.mainloop()