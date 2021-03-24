# metric unit converter
# importing libraries/packages

from tkinter import Tk,ttk
from tkinter import *
# window dimension,colour and format setting
window=Tk()
window.title(" METRIC UNIT CONVERTER")
window.geometry("700x300")
window.configure(background="black")
#for creating frame we use 3 frame here top, right and left
Tops=Frame(window, width=1000, height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
leftframe=Frame(window,width=300,height=300,bd=8,relief="raise")
leftframe.pack(side=LEFT)
rightframe=Frame(window,width=300,height=300,bd=8,relief="raise")
rightframe.pack(side=RIGHT)

#variable 

v=StringVar()
convert=DoubleVar()
unit=DoubleVar()

# function for conversion

def conunit():
    if v.get()=='milimeter to centimeter':
        c1=float(convert.get()/10)
        c2=str('%f'%(c1)),'centimeter'
        unit.set(c2)
    elif v.get()=='centimeter to milimeter':
        c1=float(convert.get()*10)
        c2=str('%f'%(c1)),'miliimeter'
        unit.set(c2)
    elif v.get()=='milimeter to meter':
        c1=float(convert.get()/1000)
        c2=str('%f'%(c1)),'meter'
        unit.set(c2)
    elif v.get()=='meter to milimeter':
        c1=float(convert.get()*1000)
        c2=str('%f'%(c1)),'milimeter'
        unit.set(c2)
    elif v.get()=='milimeter to kilometer':
        c1=float(convert.get()/10**6)
        c2=str('%f'%(c1)),'kilometer'
        unit.set(c2)
    elif v.get()=='centimeter to metere':
        c1=float(convert.get()/100)
        c2=str('%f'%(c1)),'meter'
        unit.set(c2)
    elif v.get()=='meter to centimeter':
        c1=float(convert.get()*100)
        c2=str('%f'%(c1)),'centimeter'
        unit.set(c2)
    elif v.get()=='centimeter to kilometer':
        c1=float(convert.get()/10**5)
        c2=str('%f'%(c1)),'kilometer'
        unit.set(c2)
    elif v.get()=='meter to kilometer':
        c1=float(convert.get()/1000)
        c2=str('%f'%(c1)),'kilometer'
        unit.set(c2)
    elif v.get()=='kilometer to centimeter':
        c1=float(convert.get()*(10**5))
        c2=str('%f'%(c1)),'centimeter'
        unit.set(c2)
    elif v.get()=='kilometer to milimeter':
        c1=float(convert.get()*(10**6))
        c2=str('%f'%(c1)),'miliimeter'
        unit.set(c2)
    elif v.get()=='kilometer to meter':
        c1=float(convert.get()*1000)
        c2=str('%f'%(c1)),'meter'
        unit.set(c2)
    elif v.get()=='miligram to centigram':
        c1=float(convert.get()/10)
        c2=str('%f'%(c1)),'centigram'
        unit.set(c2)
    elif v.get()=='centigram to miligram':
        c1=float(convert.get()*10)
        c2=str('%f'%(c1)),'miligram'
        unit.set(c2)
    elif v.get()=='miligram to gram':
        c1=float(convert.get()/1000)
        c2=str('%f'%(c1)),'gram'
        unit.set(c2)
    elif v.get()=='gram to miligram':
        c1=float(convert.get()*1000)
        c2=str('%f'%(c1)),'miligram'
        unit.set(c2)
    elif v.get()=='miligram to kilogram':
        c1=float(convert.get()/10**6)
        c2=str('%f'%(c1)),'kilogram'
        unit.set(c2)
    elif v.get()=='centigram to gram':
        c1=float(convert.get()/100)
        c2=str('%f'%(c1)),'gram'
        unit.set(c2)
    elif v.get()=='gram to centigram':
        c1=float(convert.get()*100)
        c2=str('%f'%(c1)),'centigram'
        unit.set(c2)
    elif v.get()=='centigram to kilogram':
        c1=float(convert.get()/10**5)
        c2=str('%f'%(c1)),'kilogram'
        unit.set(c2)
    elif v.get()=='gram to kilogram':
        c1=float(convert.get()/1000)
        c2=str('%f'%(c1)),'kilogram'
        unit.set(c2)
    elif v.get()=='kilogram to centigram':
        c1=float(convert.get()*(10**5))
        c2=str('%f'%(c1)),'centigram'
        unit.set(c2)
    elif v.get()=='kilogram to miligram':
        c1=float(convert.get()*(10**6))
        c2=str('%f'%(c1)),'miligram'
        unit.set(c2)
    elif v.get()=='kilogram to gram':
        c1=float(convert.get()*1000)
        c2=str('%f'%(c1)),'gram'
        unit.set(c2)
    else :
        v.get() ==" "
        unit.set('error')

   


#function for exit and reset window

def Quit():
        window.destroy()
        return 
def Reset():
    v.set(" ")
    unit.set("::")
    convert.set("0")


#for adding title

title=Label(Tops,font=('arial',50,'bold'),text="UNIT CONVERTER"
        ,bd=2,fg="dark violet",relief="sunken")
title.grid(row=0,column=2)


#for combo box means dropdown list

box=ttk.Combobox(leftframe,textvariable=v, font=('arial',20,'bold'),width=29)
box['value']=('','milimeter to centimeter', 'centimeter to milimeter' , 'milimeter to meter' , 'meter to milimeter','centimeter to kilometer',
              'kilometer to centimeter','meter to kilometer','kilometer to milimeter','kilometer to meter''milemeter to kilometer',
              'centimeter to metere','meter to centimeter','centigram to miligram','miligram to gram','gram to miligram',
              'miligram to kilogram','kilogram to centigram','kilogram to miligram','kilogram to gram','centigram to gram','gram to centigram',
              'centigram to kilogram','gram to kilogram','miligram to centigram',)
box.current(0)
box.grid(row=0,column=0)



#for creating labels

ent=Entry(leftframe,font=('arial',20,'bold'),textvariable=convert,bd=14,width=30,justify='center',relief="sunken")
ent.grid(row=1,column=0)
letconvert=Label(leftframe,font=('arial',20,'bold'),textvariable=unit,bd=14,width=26,
                 bg="white",relief="sunken")
letconvert.grid(row=2,column=0)




#for adding buttons(b)

b1=Button(rightframe,text="convert",bd=4,fg="green",
          font=('arial',18,'bold'),width=10,height=0,command=conunit).grid(row=1,column=0)
b2=Button(rightframe,text="Erase",bd=4,fg="green",
          font=('arial',18,'bold'),width=10,height=0,command=Reset).grid(row=2,column=0)
b3=Button(rightframe,text="Exit",bd=4,fg="green",
          font=('arial',18,'bold'),width=10,height=0,command=Quit).grid(row=3,column=0)
window.mainloop()

