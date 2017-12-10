from tkinter import *
import random,os
import datetime
import ctypes

#   store some stuff for win api interaction
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event

alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002


def steal_focus():
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(root.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

    ent.focus_set()
    root.after(1000, steal_focus)

def parse_quiz(qf_name):
    qa=[]
    q=''
    flines=open(qf_name).read().splitlines()
    for line in flines:
        if len(line)>2:
            if '(' in line:
                a=line.strip(' ()\n\t').upper()
                qa.append((q, a))
                q=''
            else:
                q+=line+'\n'
    return qa

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


(fcdate, fccount) = (int(x) for x in open('var_counter.dat').read().split())
print((fcdate, fccount))
cdate=datetime.datetime.now().day
print(cdate)
if(cdate == fcdate):
    fccount+=1
else:
    fcdate=cdate
    fccount = 0
open('var_counter.dat','w').write('{} {}'.format(fcdate, fccount))
qstyle='quiz'
if fccount==0:
    qstyle='word'
elif fccount==1:
    qstyle='math'

random.shuffle(passwd)
pw=passwd[0].upper()
int1=random.randint(0,10)
int2=random.randint(0,10)
sign=random.randint(0,1)
rr=int1 + (int2 if sign else (-int2))
print(int1,int2,rr)

qpw=''

if qstyle=='math':
    pw=str(rr)
    qpw=str(int1)+ ('+' if sign else '-') + str(int2)+'='
if qstyle=='word':
    mn=random.randint(1,len(pw)-1)
    pwm=list(pw)
    pwm[mn]='_'
    qpw=''.join(pwm)
if qstyle=='quiz':
    quizs=parse_quiz('q2_det.txt')
    mn=random.randint(0,len(quizs)-1)
    pw=quizs[mn][1]
    qpw=quizs[mn][0]



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
if qstyle=='quiz':
    T=Text(root, height=6, width=50,font=("Tahoma", 16))
    T.place(x=(1*root.winfo_width())/4, y = root.winfo_height()/4)
    T.insert(END, qpw)
if qstyle=='word' or qstyle=='math':
    Label(root, text="Сегодняшний пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-150)
    Label(root, text=qpw,font=("Arial", 32)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-120)
Label(root, text="Введи пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2-50)
ent=Entry(root,font=("Arial", 32),textvariable=ev)
ent.place(x=(1*root.winfo_width())/3, y = root.winfo_height()/2)
#ent.focus_force()
#root.after(300, lambda: root.focus_force())
#update_clock()
root.after(500, steal_focus)
root.mainloop()