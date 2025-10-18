import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


ex = tk.Tk()
ex.title('BMI CALCULATOR')
ex.geometry('400x550+50+50')
ex.resizable(False, False)
ex.configure(bg= 'grey')

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text='UNDERWEIGHT!')
        label3.config(text='please eat more \n your weight is below average')


    elif bmi<=25:
        label2.config(text='NORMAL WEIGHT')
        label3.config(text='your body is in good health keep it up')
    
    
    elif bmi<=35:
        label2.config(text='OVERWEIGHT!')
        label3.config(text='please regulate your food intake \n let it be more balanced diet \n exercise more to loose weight')
    
    
    else:
        label2.config(text='DANGER!!!')
        label3.config(text='your health is at risk \n please lose some weight asap')



ex.iconbitmap("C:/Users/miste/OneDrive/Immagini/Copy of icon.ico")

img= tk.PhotoImage(file=r"G:\My Drive\Copy of top.png")
top_image=ttk.Label(ex, image=img, background='green')
top_image.place(x=-10, y=-10)


Label(ex, height=18, width=72, bg='pink').pack(side=BOTTOM)


box = tk.PhotoImage(file=r"G:\My Drive\Copy of box.png")
ttk.Label(ex, image=box).place(x=-10, y=90)
ttk.Label(ex, image=box).place(x=190, y=90)

scale= tk.PhotoImage(file=r"G:\My Drive\Copy of scale.png")
Label(ex, image=scale, bg='pink').place(x=0, y=285)


current_value=tk.DoubleVar()

def get_current_value():
    return '{: 2f}'.format(current_value.get())


def slider1_change(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))

    img=(Image.open(r"G:\My Drive\Copy of man.png"))         
    resized_man=img.resize((50, 10+size))
    photo2=ImageTk.PhotoImage(resized_man)         
    secondimage.config(image=photo2)
    secondimage.place(x=55,y=530-size)
    secondimage.image=photo2   

ttk.Style().configure('TScale', background='purple')
slider1=ttk.Scale(ex,from_=0, to=240,orient='horizontal',style='TScale',command= slider1_change, variable=current_value)
slider1.place(x=80,y=245)



current_value2=tk.DoubleVar()

def get_current_value2():
    return '{: 2f}'.format(current_value2.get())


def slider2_change(event):
    Weight.set(get_current_value2())


    #size=int(float(get_current_value()))

    #img=(Image.open(r"G:\My Drive\Copy of man.png"))         
    #resized_man=img.resize((50, 10+size))
    #photo2=ImageTk.PhotoImage(resized_man)         
    #secondimage.config(image=photo2)
    #secondimage.place(x=55,y=490-size)
    #secondimage.image=photo2         
         
ttk.Style().configure('TScale', background='purple')
slider2=ttk.Scale(ex,from_=0, to=200,orient='horizontal',style='TScale',command= slider2_change, variable=current_value2)
slider2.place(x=290,y=245)




Height=StringVar()
Weight=StringVar()

height=Entry(ex, textvariable=Height,width=5, font='arial 50',bg='white', fg='black',bd=0, justify=CENTER)
height.place(x=-5, y=150)
Height.set(get_current_value())

weight=Entry(ex, textvariable=Weight,width=5,font='arial 50',bg='white',fg='black',bd=0, justify=CENTER)
weight.place(x=210, y=150)
Weight.set(get_current_value2())

man=PhotoImage(file=r"G:\My Drive\Copy of man.png")
secondimage=tk.Label(ex,image=man,bg='pink',)
secondimage.place(x=55,y=550)

Button(ex, text='View Report',width=15,height=2, font='arial 10 bold',bg='lightblue',fg='red', command=BMI).place(x=240,y=285)


label1=Label(ex,font='arial 30 bold', bg='pink',fg='green')
label1.place(x=100,y=285)

label2=Label(ex,font='arial 20 bold', bg='pink',fg='yellow')
label2.place(x=140,y=390)

label3=Label(ex,font='arial 10 bold', bg='pink',fg='red')
label3.place(x=150,y=430)

Button(ex, text='exit', width=10, height=1, font='arial 10 bold', bg='white', fg='black', command=quit).place(x=290,y=510)

ex.mainloop()