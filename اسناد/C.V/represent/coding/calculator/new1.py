import tkinter as tk
from math import *

convas=tk.Tk()
convas.title('simple Calculator')

convas=tk.Canvas(convas, bg='gray')

#functions

def hhh():
    return

def clear():
    numbox.delete(0,tk.END)
    
def back():
    length=len(str(numbox.get()))
    numbox.delete(length-1)
    
def write(integer):
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    numbox.insert(0,FirstNum+str(integer))
    
def add():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='add'
    
def sub():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='sub'
    
def mult():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='mult'
    
def div():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='div'
    
def power():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    if FirstNum.count('.')==1:
        numbox.insert(0, float(FirstNum)*float(FirstNum))
    else:
        numbox.insert(0, int(FirstNum)*int(FirstNum))

def root():
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    if FirstNum.count('.')==1:
        numbox.insert(0, sqrt(float(FirstNum)))
    else:
        numbox.insert(0, sqrt(int(FirstNum)))
    
def equal():
    SecondNum=str(numbox.get())
    numbox.delete(0,tk.END)
    if math=='add':
        if F_num.count('.')==1 and SecondNum.count('.')==1:
            numbox.insert(0, float(F_num)+float(SecondNum))
        elif F_num.count('.')==1:
            numbox.insert(0, float(F_num)+int(SecondNum))
        elif SecondNum.count('.')==1:
            numbox.insert(0, int(F_num)+float(SecondNum))
        else:
            numbox.insert(0, int(F_num)+int(SecondNum))
    elif math=='sub':
        if F_num.count('.')==1 and SecondNum.count('.')==1:
            numbox.insert(0, float(F_num)-float(SecondNum))
        elif F_num.count('.')==1:
            numbox.insert(0, float(F_num)-int(SecondNum))
        elif SecondNum.count('.')==1:
            numbox.insert(0, int(F_num)-float(SecondNum))
        else:
            numbox.insert(0, int(F_num)-int(SecondNum))
    elif math=='mult':
        if F_num.count('.')==1 and SecondNum.count('.')==1:
            numbox.insert(0, float(F_num)*float(SecondNum))
        elif F_num.count('.')==1:
            numbox.insert(0, float(F_num)*int(SecondNum))
        elif SecondNum.count('.')==1:
            numbox.insert(0, int(F_num)*float(SecondNum))
        else:
            numbox.insert(0, int(F_num)*int(SecondNum))
    elif math=='div':
        if F_num.count('.')==1 and SecondNum.count('.')==1:
            numbox.insert(0, float(F_num)/float(SecondNum))
        elif F_num.count('.')==1:
            numbox.insert(0, float(F_num)/int(SecondNum))
        elif SecondNum.count('.')==1:
            numbox.insert(0, int(F_num)/float(SecondNum))
        else:
            numbox.insert(0, int(F_num)/int(SecondNum))
    
#buttons

convas.grid(row=0, column=0)
numbox=tk.Entry(convas, width=35, font=('Times New Roman',12,'bold'))
num1=tk.Button(convas, text='1', padx=20, pady=15, command=lambda: write(1))
num2=tk.Button(convas, text='2', padx=20, pady=15, command=lambda: write(2))
num3=tk.Button(convas, text='3', padx=20, pady=15, command=lambda: write(3))
num4=tk.Button(convas, text='4', padx=20, pady=15, command=lambda: write(4))
num5=tk.Button(convas, text='5', padx=20, pady=15, command=lambda: write(5))
num6=tk.Button(convas, text='6', padx=20, pady=15, command=lambda: write(6))
num7=tk.Button(convas, text='7', padx=20, pady=15, command=lambda: write(7))
num8=tk.Button(convas, text='8', padx=20, pady=15, command=lambda: write(8))
num9=tk.Button(convas, text='9', padx=20, pady=15, command=lambda: write(9))
num0=tk.Button(convas, text='0', padx=20, pady=15, command=lambda: write(0))
dot=tk.Button(convas, text='.', padx=20, pady=15, command=lambda: write('.'))
clear=tk.Button(convas, text='C', padx=20, pady=15, command=clear)
back=tk.Button(convas, text='<-', padx=20, pady=15, command=back)
power=tk.Button(convas, text='^2', padx=20, pady=15, command=power)
root=tk.Button(convas, text='√', padx=20, pady=15, command=root)
add=tk.Button(convas, text='+', padx=20, pady=15, command=add)
div=tk.Button(convas, text='÷', padx=20, pady=15, command=div)
mult=tk.Button(convas, text='×', padx=20, pady=15, command=mult)
sub=tk.Button(convas, text='-', padx=20, pady=15, command=sub)
equal=tk.Button(convas, text='=', padx=20, pady=15, command=equal)


#positions

numbox.grid(row=0, column=0, padx=15, pady=15, columnspan=4)
num1.grid(row=4, column=0, padx=5, pady=5)
num2.grid(row=4, column=1, padx=5, pady=5)
num3.grid(row=4, column=2, padx=5, pady=5)  
num4.grid(row=3, column=0, padx=5, pady=5)
num5.grid(row=3, column=1, padx=5, pady=5)
num6.grid(row=3, column=2, padx=5, pady=5)
num7.grid(row=2, column=0, padx=5, pady=5)
num8.grid(row=2, column=1, padx=5, pady=5)
num9.grid(row=2, column=2, padx=5, pady=5)
num0.grid(row=5, column=0, padx=5, pady=5)
dot.grid(row=5, column=1, padx=5, pady=5)
clear.grid(row=1, column=2, padx=5, pady=5)
back.grid(row=1, column=3, padx=5, pady=5)
power.grid(row=1, column=0, padx=5, pady=5)
root.grid(row=1, column=1, padx=5, pady=5)
add.grid(row=5, column=3, padx=5, pady=5)
div.grid(row=2, column=3, padx=5, pady=5)
mult.grid(row=3, column=3, padx=5, pady=5)
sub.grid(row=4, column=3, padx=5, pady=5)
equal.grid(row=5, column=2, padx=5, pady=5)

convas.mainloop()
