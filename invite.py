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

def parse_chess_quiz(qf_name):
    tqa=[]
    q=''
    flines=open(qf_name).read().splitlines()
    for i in range (0,int(len(flines)/3)):
        tqa.append((flines[i*3],flines[i*3+1],flines[i*3+2]))
    return tqa


def onclick(event):
    print("Enter button")
    if(ev.get()==pw):
     os.system("shutdown -s -t 1000")
     root.destroy()
         
def caps(event):
    if(qstyle!='chess'):
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
    return          
    
def figname(ch):
    if (ch=='R'):
        return 'ладьёй'
    if (ch=='N'):
        return 'конём'
    if (ch=='B'):
        return 'слоном'
    if (ch=='Q'):
        return 'ферзём'
    return 'пешкой'
    
passwd=['экскаватор',\
        'тепловоз',\
        'патруль',\
        'щенячий',\
        'калькулятор',\
        'мобильный телефон',\
        'самолёт',\
        'пароход',\
        'вертолёт',\
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
qstyle='chess'
if fccount==0:
    qstyle='word'
elif fccount==1:
    qstyle='math'
elif fccount==2:
    qstyle='quiz'
    
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
if qstyle=='chess':
    quizs=parse_chess_quiz('m8n2.txt')
    pw='...'
    while '...' in pw:
        mn=random.randint(0,len(quizs)-1)
        pw=quizs[mn][2]
        qpw=quizs[mn][1]



root = Tk()
root.bind('<Return>', onclick)
root.bind("<KeyRelease>", caps)
root.bind("<Win_R>", donothing)
root.bind("<Win_L>", donothing)
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
if qstyle=='chess':
    #svg_board = chess.svg.board(chess.Board('r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0'))
    bb=chess.Board(qpw)
    iof = io.BytesIO()
    moves=pw.split()
#    T = Text(root, height=6, width=30, font=("Tahoma", 16))
#    T.place(x=(1 * root.winfo_width()) / 14, y=root.winfo_height() / 4)
#    T.insert(END, qpw)
    mv1=bb.parse_san(moves[1])
    bb.push(mv1)
    mv2=bb.parse_san(moves[2])
    bb.push(mv2)
    mv3=bb.parse_san(moves[4])
#    print(mv3)
#    print(bb.uci(mv3,True))
#    print(bb.uci(mv3))
    #print(bb.  san(mv1))
#    for mm in moves:
#        T.insert(END, mm+'\n')
#    T.insert(END, bb.uci(mv3)[2:]+'\n')
    q_text='На какое поле нужно пойти '+figname(moves[4][0]).upper()+', чтобы поставить мат чёрным?'
    Label(root, text=q_text,font=("Helvetica", 32),wraplength=root.winfo_width()/3,anchor=W, justify=LEFT, width=40).place(x=(1*root.winfo_width())/13, y = root.winfo_height()/2-150)
    pw=bb.uci(mv3)[2:]
    svg_board = chess.svg.board(bb)
    cairo_board = cairosvg.svg2png(svg_board, write_to=iof)
    iof.seek(0)
    im = PIL.Image.open(iof)
    photo = PIL.ImageTk.PhotoImage(im)
    Label(root, image=photo).place(x=(1*root.winfo_width())/2, y = root.winfo_height()/10)


Label(root, text="Введи пароль:",font=("Helvetica", 16)).place(x=(1*root.winfo_width())/3, y = root.winfo_height()*2/3-50)
ent=Entry(root,font=("Arial", 32),textvariable=ev)
ent.place(x=(1*root.winfo_width())/3, y = root.winfo_height()*2/3)
root.after(500, steal_focus)
root.mainloop()