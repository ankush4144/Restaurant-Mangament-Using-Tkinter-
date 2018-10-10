from tkinter import *
from tkinter import messagebox
import datetime



class calculation:                      #class with all the functions

    def __init__(self):
        self.totalAmount=0
        
    def close_window(self):
        try:
            if(entry1.get()=='' and entry2.get()>='0'):
                raise ValueError
            elif(entry1.get()=='' and entry2.get()==''):
                messagebox.showinfo("THANKS","-----THANKS FOR USING OUR SERVICE----")
            else:
                messagebox.showinfo("TOTAL BILL ","-----THANKS FOR USING OUR SERVICE----\n\n"+"ORDER NO. "+str(entry1.get())+"\nTOTAL AMOUNT TO BE RECEIVED\nRs. "+str(self.totalAmount))
        except ValueError:
            messagebox.showinfo("ERROR","ORDER NUMBER IS EMPTY")
        else:
            root.destroy()
    def cost1(self):
        try:
            global totalAmount
            total=(int(entry2.get())*120)+(int(entry3.get())*80)+(int(entry4.get())*50)+(int(entry5.get())*150)+(int(entry6.get())*30)+(int(entry7.get())*35)
            cost.set("Rs. "+str(total))
            tax.set("Rs. "+str(0.18*total))
            serviceCharge.set("Rs. "+str(round(0.01*total,2)))
            Total.set("Rs. "+str(round((total+(0.18*total)+(0.01*total)),2)))
        except:
            messagebox.showinfo("ERROR","Please Enter Value In Every Field\nAnd Value Should Be Integer Only")
        else:
            self.totalAmount =  round((total+(0.18*total)+(0.01*total)),2)

    def reset_values(self):
        cost.set(0)
        Total.set(0)
        tax.set(0)
        serviceCharge.set(0)

    def price(self):
        messagebox.showinfo("Price List","French Meal-Rs.120 \n\nLunch Meal-Rs.80 \n\nBurger Meal-Rs.50 \n\nPizza Meal-Rs.150 \n\nCheese Burger-Rs.30 \n\nDrinks-Rs.35")



cal=calculation()

root = Tk()
root.title('RESTAURANT MANAGEMENT')
root.resizable(False, False)
root.geometry('800x500')
   
canvas = Canvas(root, bg='DarkOrchid4',height=500,width=800)   
canvas.grid()


canvas.create_text(400,15,fill="chocolate2",font="Times 20 italic bold",   #TEXT FOR THE TITLE
                       text="--Restaurant Management System--")

canvas.create_text(400,40,fill="chocolate2",font="Times 15 bold",          #TEXT FOR THE DATE
                       text=str(datetime.datetime.today().date()))

canvas.create_text(400,55,fill="chocolate2",font="Times 10 bold",          #TEXT FOR THE TIME
                       text=str(datetime.datetime.today().strftime("%H:%M:%S")))


canvas.create_text(50,80,fill="snow",font="Times 10 bold",text="Order No.")                     #ENTRY WIDGET FOR ORDER NO.
entry1=Entry(root,width=30)
entry1.place(x=100,y=70)


canvas.create_text(50,110,fill="snow",font="Times 10 bold",text="French Meal")                  #ENTRY WIDGET FOR FRENCH MEAL
entry2=Entry(root,width=30)
entry2.place(x=100,y=100)


canvas.create_text(50,140,fill="snow",font="Times 10 bold",text="Lunch Meal")                   #ENTRY WIDGET FOR LUNCH MEAL
entry3=Entry(root,width=30)
entry3.place(x=100,y=130)


canvas.create_text(50,170,fill="snow",font="Times 10 bold",text="Burger Meal")                  #ENTRY WIDGET FOR BURGER MEAL
entry4=Entry(root,width=30)
entry4.place(x=100,y=160)


canvas.create_text(50,200,fill="snow",font="Times 10 bold",text="Pizza Meal")                   #ENTRY WIDGET FOR PIZZA MEAL
entry5=Entry(root,width=30)
entry5.place(x=100,y=190)


canvas.create_text(50,230,fill="snow",font="Times 10 bold",text="Cheese Burger")                #ENTRY WIDGET FOR CHEESE BURGER
entry6=Entry(root,width=30)
entry6.place(x=100,y=220)


canvas.create_text(450,80,fill="snow",font="Times 10 bold",text="Drinks")                       #ENTRY WIDGET FOR DRINKS
entry7=Entry(root,width=30)
entry7.place(x=500,y=70)

cost=StringVar()
canvas.create_text(450,110,fill="snow",font="Times 10 bold",text="Cost")                        #ENTRY WIDGET FOR COST
entry8=Entry(root,width=30,textvariable=cost,state=DISABLED)
entry8.place(x=500,y=100)

serviceCharge=StringVar()
canvas.create_text(450,140,fill="snow",font="Times 10 bold",text="Service Charge")              #ENTRY WIDGET FOR SERVICE CHARGE
entry9=Entry(root,width=30,textvariable=serviceCharge,state=DISABLED)
entry9.place(x=500,y=130)

tax=StringVar()
canvas.create_text(450,170,fill="snow",font="Times 10 bold",text="Tax")                         #ENTRY WIDGET FOR TAX
entry10=Entry(root,width=30,textvariable=tax,state=DISABLED)
entry10.place(x=500,y=160)



canvas.create_text(450,200,fill="snow",font="Times 10 bold",text="Sub Total")                   #ENTRY WIDGET FOR SUB TOTAL
entry11=Entry(root,width=30,textvariable=cost,state=DISABLED)
entry11.place(x=500,y=190)


Total = StringVar()
canvas.create_text(450,230,fill="snow",font="Times 10 bold",text="Total")                       #ENTRY WIDGET FOR TOTAL
entry12=Entry(root,width=30,textvariable=Total,state=DISABLED)
entry12.place(x=500,y=220)

canvas.create_text(370,300,fill="snow",font="Times 10 bold",text="Service Tax - 1%                    Tax - 18%")  #TEXT FOR TAX APPLIED

price = Button(root, text="PRICE",command=cal.price)                                        #BUTTON FOR PRICE
canvas.create_window(100, 350, anchor=NW, height=25, width=90, window=price)


total = Button(root, text="TOTAL",command=cal.cost1)                                        #BUTTON FOR TOTAL
canvas.create_window(250, 350, anchor=NW, height=25, width=90, window=total)


reset = Button(root, text="RESET",command=cal.reset_values)                                 #BUTTON FOR RESET
canvas.create_window(450, 350, anchor=NW, height=25, width=90, window=reset)


exit1 = Button(root, text="EXIT",command=cal.close_window)                                  #BUTTON FOR EXIT
canvas.create_window(600, 350, anchor=NW, height=25, width=90, window=exit1)

root.mainloop()
