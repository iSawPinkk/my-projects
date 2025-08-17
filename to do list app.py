#main code
class Task():
    def __init__(self,task,imp,id):
        self.task=task
        self.imp=imp #prority
        self.id=id
class taskList():
    def __init__(self):
        self.list=[]
        self.size=0
    def add(self,task):
        if task.imp==1:
            self.list.insert(0,(task.id, task))
        else:
            self.list.append((task.id,task))
        self.size+=1
    def delete(self,key):
        rev=None
        for elem in self.list:
            if elem[0]==key:
                rev=elem
                break
        if rev:
            self.list.remove(rev)
    def print_all(self):
        prin = ""
        if self.list:
            for i in self.list:
                prin += f"{i[1].task}(id: {i[0]} )" + "\n"
            return prin
        else:
            return "null"



    def search(self,key):
        for i in self.list:
            if i[0]==key:
                return True
        return False
tdlist=taskList()

#change page
def pageClear():
    btn_get.place_forget()
    ent_apd.place_forget()
    btn_apd.place_forget()
    btn_del.place_forget()
    btn_getD.place_forget()
    ent_del.place_forget()
    btn_pr.place_forget()
    btn_bk.place_forget()
    btn_left.place_forget()
    btn_right.place_forget()
    chk_apd.place_forget()
    var_chkA.set(0)


def pageOne():
    pageClear()
    btn_apd.place(anchor="center", x=100, y=60)
    btn_del.place(anchor="center", x=100, y=135)
    btn_left.place(anchor="center", x=80, y=200)
    btn_right.place(anchor="center", x=120, y=200)
    btn_right.config(state="normal")
    btn_left.config(state="disabled")


def pageTwo():
    pageClear()
    btn_get.place(anchor="center", x=125, y=200)
    ent_apd.place(anchor="center", x=100, y=70)
    btn_bk.place(anchor="center", x=55, y=200)
    chk_apd.place(anchor="center", x=100, y=120)
    ent_apd.delete(0,END)


def pageThree():
    pageClear()
    btn_getD.place(anchor="center", x=100, y=200)
    ent_del.place(anchor="center", x=100, y=70)
    btn_bk.place(anchor="center", x=100, y=160)
    ent_del.delete(0, END)

def pageFour():
    pageClear()
    btn_pr.place(anchor="center",x=100,y=60)
    btn_left.place(anchor="center", x=80, y=200)
    btn_right.place(anchor="center", x=120, y=200)
    btn_right.config(state="disabled")
    btn_left.config(state="normal")

#main screen
from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("ToDo")
win.geometry("200x250")
# win.minsize(width=200,height=250)
# win.maxsize(width=200,height=250)
win.resizable(False,False) # T/F = 0/1
win.config(background="grey")

#add task
btn_bk=Button(win)
btn_bk.config(width=5,height=1,text="back")
btn_bk.config(command=pageOne)
def btnApd():
    pageTwo()
btn_apd=Button(win)
btn_apd.config(width=10,height=3,text="ADD")
btn_apd.config(command=btnApd)

def getApd_hideText():
    lab_get.place_forget()
    pageOne()
def getApd():
    global value
    value=ent_apd.get()
    if not value == "":
        new_task = Task(value, var_chkA.get(), tdlist.size)
        tdlist.add(new_task)
        lab_get.place(anchor="center", x=100, y=100)
        pageClear()
        win.after(1000, getApd_hideText)


btn_get=Button(win,command=getApd,width=9,height=1,text="enter task")
ent_apd=Entry(win)
lab_get=Label(win,bg="white",width=12,height=2,text="task added")
var_chkA=IntVar(value=0)
chk_apd=Checkbutton(win,text="high priority",variable=var_chkA, onvalue=1, offvalue=0)



#delete elem
def btnDel():
    pageThree()
btn_del=Button(win)
btn_del.config(width=10,height=3,text="DELETE")
btn_del.config(command=btnDel)
def getDel_hideText():
    lab_getD.place_forget()
    lab_nf.place_forget()
    lab_error.place_forget()
    pageOne()
def getDel():
    global value
    try :
        value=int(ent_del.get())
    except ValueError:
        lab_error.place(anchor="center", x=100, y=100)
        pageClear()
        win.after(1000, getDel_hideText)

    if tdlist.search(value) :
        tdlist.delete(value)
        pageClear()
        lab_getD.place(anchor="center", x=100, y=100)
        win.after(1000,getDel_hideText)
    else:
        pageClear()
        lab_nf.place(anchor="center", x=100, y=100)
        win.after(1000, getDel_hideText)


btn_getD=Button(win,command=getDel,width=9,height=1,text="enter key")
ent_del=Entry(win)
lab_getD=Label(win,bg="white",width=12,height=2,text="task deleted")
lab_getD.place_forget()
lab_nf=Label(win,bg="white",width=12,height=2,text="key not found")
lab_nf.place_forget()
lab_error=Label(win,bg="white",width=12,height=2,text="invalid value")
lab_error.place_forget()

#show list
def btnPr():
    messagebox.showinfo("toDo",tdlist.print_all())
btn_pr=Button(win)
btn_pr.config(width=10,height=1,text="show list")
btn_pr.config(command=btnPr)


def btnLeft():
    btn_left.config(state="disabled")
    btn_right.config(state="normal")
    pageClear()
    pageOne()
def btnRight():
    btn_right.config(state="disabled")
    btn_left.config(state="normal")
    pageClear()
    pageFour()
btn_left=Button(win,bg="white",width=2,height=1,text="<",command=btnLeft)
btn_right = Button(win, bg="white", width=2, height=1, text=">",command=btnRight)





pageOne()

win.mainloop()
