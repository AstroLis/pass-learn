from tkinter import *
import random,os

def onclick(event):
    print("Enter button")
    if(ev.get()==pw):
     os.system("shutdown -s -t 1000")
     root.destroy()
     
def update_clock():
        root.focus_force()
        ent.focus_force()
        root.after(100, update_clock())
     
def caps(event):
    ev.set(ev.get().upper())  
    print(ev.get())
    print(pw)
    if(ev.get()==pw):
     os.system("shutdown -s -t 1000")
     root.destroy()
def donothing(event):
    print (event.char)
    print (event.keycode)
    print (event.keysym)
    print ('---')
    root.after(100, lambda: root.focus_force())
    return                                           
passwd=['экскаватор',\
        'тепловоз',\
        'патруль',\
        'щенячий',\
        'калькулятор',\
        'мобильный телефон',\
        'самолёт',\
        'пароход',\
        'атом',\
        'тепловоз',\
        'автомобиль',\
        'электрон',\
        'тепловизор',\
        'парашют',\
        'параплан',\
        'подъезд',\
        'грузовик',\
        'стрелка',\
        'двигатель',\
        'фиксики',\
        'робокар',\
        'шахматы']
random.shuffle(passwd)
pw=passwd[0].upper()
int1=random.randint(0,10)
int2=random.randint(0,10)
sign=random.randint(0,1)
rr=int1 + (int2 if sign else (-int2))
print(int1,int2,rr)
#pw=str(rr)
#qpw=str(int1)+ ('+' if sign else '-') + str(int2)+'='
mn=random.randint(1,len(pw)-1)
pwm=list(pw)
pwm[mn]='_'
qpw=''.join(pwm)
root = Tk()
root.bind('<Return>', onclick)
root.bind("<KeyRelease>", caps)
root.bind("<Win_R>", donothing)
root.bind("<Win_L>", donothing)
#root.bind("<Super_R>", donothing)
#root.bind("<Super_L>", donothing)
#root.bind("<Key>", donothing)
ev = StringVar()
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", 1)
root.protocol("WM_DELETE_WINDOW", donothing)
root.focus_force()
root.update()
#print (root.winfo_width)
Label(root, text="Сегодняшний пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-150)
Label(root, text=qpw,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-120)
Label(root, text="Введи пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-50)
ent=Entry(root,font=("Arial", 32),textvariable=ev)
ent.place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2)
ent.focus_force()
root.after(300, lambda: root.focus_force())
#update_clock()
root.mainloop()