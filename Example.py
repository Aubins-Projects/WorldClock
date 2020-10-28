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
 
timenow=''
cframe =Frame(root, width=1920, height=500, bg='black', relief=GROOVE)
cframe.pack()
 
clock=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= timenow,bg='gray', relief= SUNKEN)
clock.pack()

clock1=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "",bg='gray', relief= SUNKEN)
clock1.pack()

clock2=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock2.pack()

clock3=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock3.pack()

clock4=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock4.pack()

clock5=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock5.pack()

clock6=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock6.pack()

clock7=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= "test",bg='gray', relief= SUNKEN)
clock7.pack()

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
        #clock3.config(text= timezoner(clock3_zone))
        #clock4.config(text= timezoner(clock4_zone))
        #clock5.config(text= timezoner(clock5_zone))
        #clock6.config(text= timezoner(clock6_zone))
        #clock7.config(text= timezoner(clock7_zone))
    clock.after(200, timer)
timer()
 
 
root.mainloop()