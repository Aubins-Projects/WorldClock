from tkinter import *
import time
root = Tk()
root.geometry('600x200+350+300')
root.wm_attributes('-type', 'splash')

 
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
        clock.config(text= timenow)
    clock.after(200, timer)
timer()
 
 
root.mainloop()