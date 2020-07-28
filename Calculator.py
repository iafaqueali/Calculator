#Code to be paste

from tkinter import*

root = Tk()
root.title("Calculator")
root.minsize(width=364, height=523)
root.maxsize(width=364, height=523)
#Code For Icon (Paste Here)
icon = PhotoImage(file="Calculator.png") #Png , Jpg , Other.

root.tk.call('wm','iconphoto',root._w,icon) #Image Should Be With The Python File

def Calc(source, side):
    storeObj = Frame (source, borderwidth=4, bd=4, bg="Green")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, bg="Gold", fg="Red", text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame. __init__(self)
        self.option_add('*Font', 'Helvetica 22 bold', )
        self.pack(expand=YES, fill=BOTH)


        display = StringVar()
        Entry(self, relief=RIDGE,
                textvariable=display,justify='right',bd=26,fg="Black",bg="White").pack(side=TOP, expand=YES,
                        fill=BOTH)

        for clearBut in(["CLEAR"],):
            erase = Calc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = Calc(self, TOP)
            for char in NumBut:
                button(FunctionNum, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

        EqualsButton = Calc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                         lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,
                   lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))
       

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("::Error::")

if __name__ == '__main__':
    app().mainloop()   
