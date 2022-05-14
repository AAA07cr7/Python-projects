from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="c":
        pass
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
        
root=Tk()
root.geometry("644x970")
root.title("calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida,40,bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

a=[['9','8','7'],['6','5','4'],['3','2','1'],['*','0','/'],['+','-','%'],['c','=','.']]

for list in a:
    f=Frame(root,bg="grey")
    for number in list:
        b=Button(f,text=number,padx=26,pady=10,font="lucida 35 bold")
        b.pack(side=LEFT,padx=18,pady=5)
        b.bind("<Button-1>",click)
    f.pack()

root.mainloop()
