from skin import *
from tkinter import *
from time import *

app=Tk()
app.title('Skin Analysis')
app.configure(bg='dimgray')
app.geometry('490x680')
app.iconbitmap("./statics/logo.ico")

#variables

s=BooleanVar()
style= (('bg','dimgray'), ('fg','black'), ('padx',5), ('pady',5))

#functions

def next():
    pass
    
def back():
    pass

def per_prop(value):
    global e1, e2, e3, e4, e5, e6, e7, e8, e9
    if value==1:
        label1=Label(frame0, text='Perforation Length= ', bg='dimgray', fg='white', anchor='e')
        e1=Entry(frame0, highlightthickness = 2, width=8)
        label1.grid(row=4, column=0, padx=10, pady=10)
        e1.grid(row=4, column=1, padx=10, pady=10)
        label2=Label(frame0, text='Phasing Angle= ', bg='dimgray', fg='white')
        e2=Entry(frame0, highlightthickness = 2, width=8)
        label2.grid(row=5, column=0, padx=10, pady=10)
        e2.grid(row=5, column=1, padx=10, pady=10)
        label3=Label(frame0, text='SPF= ', bg='dimgray', fg='white')
        e3=Entry(frame0, highlightthickness = 2, width=8)
        label3.grid(row=6, column=0, padx=10, pady=10)
        e3.grid(row=6, column=1, padx=10, pady=10)
        label4=Label(frame0, text='Anisotropy (Iani)= ', bg='dimgray', fg='white')
        e4=Entry(frame0, highlightthickness = 2, width=8)
        label4.grid(row=7, column=0, padx=10, pady=10)
        e4.grid(row=7, column=1, padx=10, pady=10)
        label5=Label(frame0, text='Kd/K= ', bg='dimgray', fg='white')
        e5=Entry(frame0, highlightthickness = 2, width=8)
        label5.grid(row=8, column=0, padx=10, pady=10)
        e5.grid(row=8, column=1, padx=10, pady=10)
        label6=Label(frame0, text='Kc/K= ', bg='dimgray', fg='white')
        e6=Entry(frame0, highlightthickness = 2, width=8)
        label6.grid(row=9, column=0, padx=10, pady=10)
        e6.grid(row=9, column=1, padx=10, pady=10)
        label7=Label(frame0, text='Damage zone radius (in.)= ', bg='dimgray', fg='white')
        e7=Entry(frame0, highlightthickness = 2, width=8)
        label7.grid(row=10, column=0, padx=10, pady=10)
        e7.grid(row=10, column=1, padx=10, pady=10)
        label8=Label(frame0, text='Crushed zone radius (in.)= ', bg='dimgray', fg='white')
        e8=Entry(frame0, highlightthickness = 2, width=8)
        label8.grid(row=11, column=0, padx=10, pady=10)
        e8.grid(row=11, column=1, padx=10, pady=10)
        label9=Label(frame0, text='Perforation tunnel radius (in.)= ', bg='dimgray', fg='white')
        e9=Entry(frame0, highlightthickness = 2, width=8)
        label9.grid(row=12, column=0, padx=10, pady=10)
        e9.grid(row=12, column=1, padx=10, pady=10)
        s.set(0)


        
def well_prop(value):
    global e0
    s.set(0)
    label0=Label(frame0, text='Well radius (in.)= ', bg='dimgray', fg='white')
    e0=Entry(frame0, highlightthickness = 2, width=8)
    label0.grid(row=2, column=0, padx=10, pady=10)
    e0.grid(row=2, column=1, padx=10, pady=10)
    
    
def calculate():
    global label11
    label11.grid_forget()
    a = Skin(e0.get())
    try:
        b = a.perforation(e1.get(), e2.get(), e3.get(), e7.get(), e8.get(), e9.get(), e4.get(), e5.get(), e6.get())
    except:
        b = 'Not Defined Angel'
    label11=Label(frame0, text=str(b), font=('Helvetica', 12, 'bold'), bg='dimgray', fg='white',  relief='raised')
    label11.grid(row=13, column=1, padx=10, pady=10)
    


#objects

frame0=LabelFrame(app, text='Perforation Skin', width=500, height=1900, bg='dimgray', font=('Helvetica', 16,), fg='white')
next_btn=Button(frame0, bg='gray17', text='Next', fg='white', padx=5, pady=5, anchor='se', command=next)
back_btn=Button(frame0, bg='gray17', text='Back', fg='white', padx=5, pady=5, anchor='sw')
Cal_btn=Button(frame0, bg='gray17', text='Calculate', fg='white', padx=5, pady=5, anchor='s', command=calculate)
radio0=Radiobutton(frame0, text='Well specifications', variable=s, value=1, command=lambda: well_prop(s.get()), bg='dimgray', highlightthickness = 0, fg='white')
radio1=Radiobutton(frame0, text='perforation specifications', variable=s, value=1, command=lambda: per_prop(s.get()), bg='dimgray', highlightthickness = 0, fg='white')
label10=Label(frame0, text='Total perforation skin= ', font=('Helvetica', 12,'bold',), bg='dimgray', fg='white')
label11=Label(frame0, text='', font=('Helvetica', 12, 'bold'), bg='dimgray', fg='white')


#positions

frame0.pack(padx=10, pady=10)
radio0.grid(row=1, column=0, padx=10, pady=10, sticky=W)
radio1.grid(row=3, column=0, padx=10, pady=10, sticky=W)
label10.grid(row=13, column=0, padx=10, pady=10)
next_btn.grid(row=14, column=2, padx=10, pady=10)
back_btn.grid(row=14, column=0, padx=10, pady=10)
Cal_btn.grid(row=14, column=1, padx=10, pady=10)
label11.grid(row=13, column=1, padx=10, pady=10)

app.mainloop()