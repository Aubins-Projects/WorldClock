from tkinter import *
import time
root = Tk()
root.geometry('2000x500+1500+00')
#root.wm_attributes('-fullscreen', 'true')
root.wm_state('zoomed')
root.overrideredirect(1)
root.bind('<Escape>',lambda e: root.destroy())
 
timenow=''
cframe =Frame(root, width=200, height=100, bg='green', relief=GROOVE)
cframe.pack()
 
clock=Label(cframe, padx=25, pady=40, bd=3, fg= 'dark green',font=('arial',48,'bold'),text= timenow,bg='light green', relief= SUNKEN)
clock.pack()
 
def timer():
    global timenow
    newtime = time.strftime('%H: %M: %S %p')
    if newtime != timenow:
        timenow= newtime
        clock.config(text= "Can I Get a Team Now?")
    clock.after(200, timer)
timer()
 
 
root.mainloop()