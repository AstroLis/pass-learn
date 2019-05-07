try:
    # python 3.x
    import tkinter as tk
except ImportError:
    # python 2.x
    import Tkinter as tk


class QuestWidget(tk.Frame):

    def change_coord(self,dx=0,dy=0,dz=0):
        ind=(self.x,self.y,self.z)
        self.rooms[ind]=self.term.get(1.0,tk.END)
        print(self.rooms[ind])
        self.term.delete(1.0,tk.END)
        self.x += dx
        self.y += dy
        self.z += dz
        ind=(self.x,self.y,self.z)
        if(ind in self.rooms):
            self.term.insert(tk.END,self.rooms[ind])

        self.entry.delete(0,tk.END)
        self.entry.insert(0,str(ind))

    def goNorth(self):
        self.change_coord(0,1,0)
    def goSouth(self):
        self.change_coord(0,-1,0)
    def goEast(self):
        self.change_coord(1,0,0)
    def goWest(self):
        self.change_coord(-1,0,0)

    def goUp(self):
        self.change_coord(0,0, 1)
    def goDown(self):
        self.change_coord(0,0,-1)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.x = 0
        self.y = 0
        self.z = 0

        self.rooms={(0,0,0):'Старт!'}

        self.term  = tk.Text(self)
        self.term.insert(tk.END,self.rooms[(0,0,0)])
        self.entry = tk.Entry(self)
        self.term.pack(side="left", fill="x", padx=4)
        self.entry.pack(side="bottom", fill="x", padx=4)

        self.bNorth=tk.Button(self,text='North',command=self.goNorth)
        self.bNorth.pack(side="right", fill="x", padx=4)

        self.bSouth=tk.Button(self,text='South',command=self.goSouth)
        self.bSouth.pack(side="right", fill="x", padx=4)

        self.bEast=tk.Button(self,text='East',command=self.goEast)
        self.bEast.pack(side="right", fill="x", padx=4)

        self.bWest=tk.Button(self,text='West',command=self.goWest)
        self.bWest.pack(side="right", fill="x", padx=4)


        self.bWest=tk.Button(self,text='Up',command=self.goUp)
        self.bWest.pack(side="top", fill="x", padx=4)

        self.bWest=tk.Button(self,text='Down',command=self.goDown)
        self.bWest.pack(side="bottom", fill="x", padx=4)


    def get(self):
        return self.entry.get()



if __name__ == "__main__":
    root = tk.Tk()
    QuestWidget(root).pack()
    root.mainloop()