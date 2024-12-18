from tkinter import *
root = Tk()
root.title('Fish-Tank Water Capacity')
root.minsize(width=760,height=500)
root.maxsize(width=760,height=500)

#TITEL
L1 = Label(root, text="Fish-Tank ")
L1.config(font=('Ink Free',32)) #change font
L1.config(bg='#111111') #background
L1.config(fg='#00FF00') #foreground
L1.config(width=12) #width displayed in characters
L1.grid(row=0,column=0)

L1 = Label(root, text="Water")
L1.config(font=('Ink Free',32)) #change font
L1.config(bg='#111111') #background
L1.config(fg='#00FF00') #foreground
L1.config(width=10) #width displayed in characters
L1.grid(row=0,column=1)

L1 = Label(root, text="Capacity")
L1.config(font=('Ink Free',32)) #change font
L1.config(bg='#111111') #background
L1.config(fg='#00FF00') #foreground
L1.config(width=10) #width displayed in characters
L1.grid(row=0,column=2)

#NOTE
L1 = Label(root, text="Note:- Include cost with glue and labor cost")
L1.config(fg='#FF0000')
L1.grid(row=1,column=0)

L1 = Label(root, text="Note:- press Tab key to start")
L1.config(fg='#FF0000')
L1.grid(row=1,column=1)

L1 = Label(root, text="Note:- Use Tab key to select&move")
L1.config(fg='#FF0000')
L1.grid(row=1,column=2)

#convert to string
m1 = StringVar()
m2 = StringVar()
m3 = StringVar()
m4 = StringVar()
m5 = StringVar()
m6 = StringVar()
m7 = StringVar()
m8 = StringVar()
m9 = StringVar()
m10 = StringVar()
m11 = StringVar()

wc = StringVar()
tp = StringVar()



#GALSS COST
L1 = Label(root, text="Enter Glass 1 Square meter Cost Here LKR")
L1.config(font=('Arial',8)) #change font
L1.grid(row=2,column=0)
E1 = Entry(root, bd =5, textvariable=m1)
E1.config(width=25)
E1.config(show='$')
E1.insert(0,'0')
E1.grid(row=3,column=0)

#ALUMINIUM COST
L1 = Label(root, text="Enter Aluminium 1 Meter Cost Here LKR")
L1.config(font=('Arial',8)) #change font
L1.grid(row=2,column=1)
E2 = Entry(root, bd =5, textvariable=m2)
E2.config(width=25)
E2.config(show='$')
E2.insert(0,'0')
E2.grid(row=3,column=1)

#SPACE
L1 = Label(root, text="")
L1.grid(row=4,column=0)

#Length
L1 = Label(root, text="Enter Length (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=5,column=0)
E3 = Entry(root, bd =5, textvariable=m3)
E3.config(width=25)
E3.insert(0,'0')
E3.grid(row=6,column=0)

#Collection Length
L1 = Label(root, text="Enter Collection Length (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=5,column=1)
E4 = Entry(root, bd =5, textvariable=m4)
E4.config(width=25)
E4.insert(0,'0')
E4.grid(row=6,column=1)

#Reduced Length
L1 = Label(root, text="Enter Reduced Length (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=5,column=2)
E5 = Entry(root, bd =5, textvariable=m5)
E5.config(width=25)
E5.insert(0,'0')
E5.grid(row=6,column=2)

#SPACE
L1 = Label(root, text="")
L1.grid(row=7,column=0)

#Width
L1 = Label(root, text="Enter Width (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=8,column=0)
E6 = Entry(root, bd =5, textvariable=m6)
E6.config(width=25)
E6.insert(0,'0')
E6.grid(row=9,column=0)

#Collection Width
L1 = Label(root, text="Enter Collection Width (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=8,column=1)
E7 = Entry(root, bd =5, textvariable=m7)
E7.config(width=25)
E7.insert(0,'0')
E7.grid(row=9,column=1)

#Reduced Length
L1 = Label(root, text="Enter Reduced Width (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=8,column=2)
E8 = Entry(root, bd =5, textvariable=m8)
E8.config(width=25)
E8.insert(0,'0')
E8.grid(row=9,column=2)

#SPACE
L1 = Label(root, text="")
L1.grid(row=10,column=0)

#Height
L1 = Label(root, text="Enter Height (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=11,column=0)
E9 = Entry(root, bd =5, textvariable=m9)
E9.config(width=25)
E9.insert(0,'0')
E9.grid(row=12,column=0)

#Collection Height
L1 = Label(root, text="Enter Collection Height (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=11,column=1)
E10 = Entry(root, bd =5, textvariable=m10)
E10.config(width=25)
E10.insert(0,'0')
E10.grid(row=12,column=1)

#Reduced Height
L1 = Label(root, text="Enter Reduced Height (cm)")
L1.config(font=('Arial',8)) #change font
L1.grid(row=11,column=2)
E11 = Entry(root, bd =5, textvariable=m11)
E11.config(width=25)
E11.insert(0,'0')
E11.grid(row=12,column=2)

#SPACE
L1 = Label(root, text="")
L1.grid(row=13,column=0)

#SUBMIT BTN
def button_command():
    E12.delete(0,END)
    E13.delete(0,END)
    n1 = float(m1.get())
    n2 = float(m2.get())
    n3 = float(m3.get())
    n4 = float(m4.get())
    n5 = float(m5.get())
    n6 = float(m6.get())
    n7 = float(m7.get())
    n8 = float(m8.get())
    n9 = float(m9.get())
    n10 = float(m10.get())
    n11 = float(m11.get())

    wc = ( n3 + n4 - n5 ) * ( n6 + n7 - n8 ) * ( n9 + n10 - n11 ) / 1000
    tp = ( ( n3 + n4 - n5 ) * 2 + ( n6 + n7 - n8 ) * 2 + ( n9 + n10 - n11 ) * 4 ) * n2 / 100 + ( ( n9 +  n10 - n11 ) * ( n6 + n7 - n8 ) * 2 + ( n3 + n4  - n5 ) * ( n9 + n10 - n11 ) * 2 + ( n6 + n7 - n8 ) * ( n3 + n4 - n5 ) ) * n1 / 10000
    
    E12.insert(0,wc)
    E13.insert(0,tp)
    return None
   

B1 = Button(root, text="Submit", command=button_command)
B1.config(fg='#FF0000') #foreground
B1.config(bg='#00FF00') #background
B1.grid(row=14,column=1)

#SPACE
L1 = Label(root, text="")
L1.grid(row=15,column=0)

#output
#Water Capacity
L1 = Label(root, text="Water Capacity (Liters)")
L1.config(font=('Arial',10)) #change font
L1.grid(row=16,column=0)
E12 = Entry(root, bd =5)
E12.config(width=25)
E12.config(font=('Arial',12))
E12.config(bg='#000000') #background
E12.config(fg='#00FF00') #foreground
E12.grid(row=17,column=0)

#price
L1 = Label(root, text="Price (LKR)")
L1.config(font=('Arial',10)) #change font
L1.grid(row=16,column=1)
E13 = Entry(root, bd =5)
E13.config(width=25)
E13.config(font=('Arial',12))
E13.config(bg='#000000') #background
E13.config(fg='#00FF00') #foreground
E13.grid(row=17,column=1)

#SPACE
L1 = Label(root, text="Powered by TechChanu.wordpress.com")
L1.config(fg='#0000FF')
L1.grid(row=18,column=2)

root.mainloop()

#entry = Entry()
#entry.config(font=('Ink Free',50)) #change font
#entry.config(bg='#111111') #background
#entry.config(fg='#00FF00') #foreground
#entry.config(width=10) #width displayed in characters
#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character
#entry.pack()
