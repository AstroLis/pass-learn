from tkinter import *
import random,os
import datetime
import ctypes
import PIL.Image
import PIL.ImageTk
import chess
import chess.svg
import cairosvg
import io

#   store some stuff for win api interaction
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event

alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002

(fcdate, fccount) = (int(x) for x in open('var_counter.dat').read().split())

def steal_focus():
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(root.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

    #ent1.focus_set()
    root.after(1000, steal_focus)

         
def caps(event):
    global fccount
    global fcdate
    print(ev1.get(),ev2.get(),ev3.get())
    print(pw1,pw2,pw3)
    if(ev1.get()==pw1 and ev2.get()==pw2 and ev3.get()==pw3 and ev4.get()==pw4):
     os.system("shutdown -s -t 700")
     fccount=random.randint(0,4)
     open('var_counter.dat','w').write('{} {}'.format(fcdate, fccount))
     open('continue.dat','w').write('{}\n{}\n{}'.format(0,0,0))
     root.destroy()
     
def donothing(event):
    print (event.char)
    print (event.keycode)
    print (event.keysym)
    print ('---')
    return          
    
int1=random.randint(-15,15)
int2=random.randint(6,19)
sign=random.randint(0,1)
rr=int1 + (int2 if sign else (-int2))
print(int1,int2,rr)
pw1=str(rr)
qpw1=str(int1)+ ('+' if sign else '-') + str(int2)+'='

int1=random.randint(-10,10)
int2=random.randint(0,15)
sign=random.randint(0,1)
rr=int1 + (int2 if sign else (-int2))
print(int1,int2,rr)
pw2=str(rr)
qpw2=str(int1)+ ('+' if sign else '-') + str(int2)+'='

int1=random.randint(-10,10)
int2=random.randint(6,19)
sign=random.randint(0,1)
rr=int1 + (int2 if sign else (-int2))
print(int1,int2,rr)
pw3=str(rr)
qpw3=str(int1)+ ('+' if sign else '-') + str(int2)+'='

int1=random.randint(0,7)
int2=random.randint(0,7)
sign=random.randint(0,1)
rr=int1 * int2
print(int1,int2,rr)
pw4=str(rr)
qpw4=str(int1) +'*'+ str(int2)+'='



root = Tk()
root.bind('<Return>', caps)
root.bind("<KeyRelease>", caps)
root.bind("<Win_R>", donothing)
root.bind("<Win_L>", donothing)
ev1 = StringVar()
ev2 = StringVar()
ev3 = StringVar()
ev4 = StringVar()
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", 1)
root.protocol("WM_DELETE_WINDOW", donothing)
root.focus_force()
root.update()

Label(root, text="Сегодняшний пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-250)
Label(root, text=qpw1,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-190)
Label(root, text=qpw2,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-130)
Label(root, text=qpw3,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-70)
Label(root, text=qpw4,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-10)


#Label(root, text="Введи пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()*2/3-50)
ent1=Entry(root,font=("Arial", 32),textvariable=ev1)
ent1.place(x=(1*root.winfo_width())/2-50, y = root.winfo_height()/2-190)

ent2=Entry(root,font=("Arial", 32),textvariable=ev2)
ent2.place(x=(1*root.winfo_width())/2-50, y = root.winfo_height()/2-130)

ent3=Entry(root,font=("Arial", 32),textvariable=ev3)
ent3.place(x=(1*root.winfo_width())/2-50, y = root.winfo_height()/2-70)

ent4=Entry(root,font=("Arial", 32),textvariable=ev4)
ent4.place(x=(1*root.winfo_width())/2-50, y = root.winfo_height()/2-10)


root.after(500, steal_focus)
root.mainloop()