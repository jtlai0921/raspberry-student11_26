#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *

def readText():
    with open('news.txt','rt',encoding="utf-8") as fileObject:
        content = ''
        while True:
            line = fileObject.readline()
            if not line:
                break
            content += line
    print(content)

def writeContent():
    print('您輸入的是:%s' % entryVariable.get())
    with open('news.txt', 'at',encoding='utf-8') as fileObject:
        print(entryVariable.get(),file=fileObject)
    entryVariable.set("")

def interface(w):
    """ 建立介面 """
    w.option_add("*font",('verdana',14))
    w.title("Pack - Example")
    #w.geometry("600x200")
    w.wm_resizable(height=False, width=False)

    menuFrame = Frame(w,bg='purple',width=200)
    lineFrame = Frame(menuFrame,borderwidth=2,relief=GROOVE,width=200,bg='purple')
    Button(lineFrame,text='讀出text', command=readText).pack(fill=BOTH,expand=TRUE)
    Button(lineFrame, text='寫入text', command=writeContent).pack(fill=BOTH,expand=TRUE,pady=5)
    Button(lineFrame, text='讀出CSV', command=readText).pack(fill=BOTH, expand=TRUE)
    Button(lineFrame, text='寫入CSV', command=writeContent).pack(fill=BOTH, expand=TRUE, pady=5)
    Button(lineFrame, text='讀出Json', command=readText).pack(fill=BOTH, expand=TRUE)
    Button(lineFrame, text='寫入Json', command=writeContent).pack(fill=BOTH, expand=TRUE, pady=5)
    Button(lineFrame, text='ok3').pack(fill=BOTH,expand=TRUE)
    lineFrame.pack(expand=YES, fill=BOTH,padx=10,pady=10)
    menuFrame.pack(side=LEFT, expand=YES,fill=BOTH)

    rightFrame = Frame(w, bg='gray',width=400)
    Label(rightFrame,text="輸入文字:").pack(side=LEFT, padx=5, pady=10)
    Entry(rightFrame,width=50,textvariable=entryVariable).pack(side=LEFT)
    rightFrame.pack(side=LEFT, expand=YES, fill=BOTH)
    entryVariable.set("Hello!World")



if __name__ == "__main__":
    window = Tk()
    entryVariable = StringVar()
    interface(w=window)
    window.mainloop()

