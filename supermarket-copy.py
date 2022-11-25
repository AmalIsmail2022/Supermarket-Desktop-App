from tkinter import *
from tkinter import messagebox
import math
import os
import random
#************************************
#انشاء كلاس
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('supermarket : سوبر ماركيت')
        self.root.resizable(False,False)
        self.root.iconbitmap('D:\\python\\pythonproject\\supermarket\\ic.ico')
        title=Label(self.root,text='supermarket system',fg='white',bg='#074463',font=('tajawal',16,'bold'),pady=2).pack(fill=X)
#************************variables cos**************************
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
#************************variables gros**************************
        self.oil=IntVar()
        self.rice=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.macaroni=IntVar()
#*************************variables cold drinks**************************
        self.juice = IntVar()
        self.cock = IntVar()
        self.seven = IntVar()
        self.souda = IntVar()
        self.icetea = IntVar()
        self.fruits = IntVar()
#*************************variables cold drinks**************************
        self.cosmetic_price= StringVar()
        self.grocery_price=StringVar()
        self.colddrink_price=StringVar()

        self.cosmetic_tx= StringVar()
        self.grocery_tx=StringVar()
        self.colddrink_tx=StringVar()
#*************************variables CUSTOMER**************************
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()
#************************customer details**************************
        f1=LabelFrame(self.root,bd=5,relief=GROOVE,text='customer details',font=('tajawal',10,'bold'),fg='gold',bg='#074463')
        f1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(f1,text='customer name',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(f1,width=15,textvariable=self.c_name,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=1,padx=10,pady=5)
        cphone_lbl=Label(f1,text='customer phone',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=2,padx=20,pady=5)
        cphone_text=Entry(f1,width=15,textvariable=self.c_phone,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=3,padx=10,pady=5)
        cbill_lbl=Label(f1,text='bill no.',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=4,padx=20,pady=5)
        cbill_text=Entry(f1,width=15,textvariable=self.bill_no,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(f1,text='search',command=self.find_bill,width=6,bd=5,font=('tajawal',16,'bold')).grid(row=0,column=6,padx=10,pady=5)
#***********************cosmetics frame***************************
        f2=LabelFrame(self.root,bd=5,relief=GROOVE,text='cosmetics',font=('tajawal',10,'bold'),fg='gold',bg='#074463')
        f2.place(x=0,y=162,width=325,height=380)

        bath_lbl=Label(f2,text='bath soap',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(f2,width=10,textvariable=self.soap,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=1,padx=10,pady=10)

        facecream_lbl=Label(f2,text='face cream',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        facecream_txt=Entry(f2,width=10,textvariable=self.facecream,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=1,column=1,padx=10,pady=10)

        facew_lbl=Label(f2,text='face wash',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        facew_txt=Entry(f2,width=10,textvariable=self.facewash,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=2,column=1,padx=10,pady=10)

        hairs_lbl=Label(f2,text='hair spry',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        hairs_txt=Entry(f2,width=10,textvariable=self.spray,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=3,column=1,padx=10,pady=10)

        hairg_lbl=Label(f2,text='hair gel',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        hairg_txt=Entry(f2,width=10,textvariable=self.gell,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(f2,text='body lotion',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        body_txt=Entry(f2,width=10,textvariable=self.lotion,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=5,column=1,padx=10,pady=10)

#***********************grocery frame***************************
        f3=LabelFrame(self.root,bd=5,relief=GROOVE,text='grocery',font=('tajawal',10,'bold'),fg='gold',bg='#074463')
        f3.place(x=320,y=162,width=325,height=380)

        g1_lbl=Label(f3,text='oil',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g1_lbl=Entry(f3,width=10,textvariable=self.oil,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(f3,text='rice',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_lbl=Entry(f3,width=10,textvariable=self.rice,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(f3,text='wheat',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3_lbl=Entry(f3,width=10,textvariable=self.wheat,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(f3,text='sugar',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4_lbl=Entry(f3,width=10,textvariable=self.sugar,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(f3,text='tea',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5_lbl=Entry(f3,width=10,textvariable=self.tea,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(f3,text='macaroni',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6_lbl=Entry(f3,width=10,textvariable=self.macaroni,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=5,column=1,padx=10,pady=10)


#***********************cold drink frame***************************
        f4=LabelFrame(self.root,bd=5,relief=GROOVE,text='cold drinks',font=('tajawal',10,'bold'),fg='gold',bg='#074463')
        f4.place(x=640,y=162,width=325,height=380)

        c1_lbl=Label(f4,text='juice',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        c1_lbl=Entry(f4,width=10,textvariable=self.juice,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(f4,text='cock',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        c2_lbl=Entry(f4,width=10,textvariable=self.cock,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(f4,text='seven',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        c3_lbl=Entry(f4,width=10,textvariable=self.seven,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(f4,text='souda',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        c4_lbl=Entry(f4,width=10,textvariable=self.souda,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(f4,text='ice tea',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        c5_lbl=Entry(f4,width=10,textvariable=self.icetea,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(f4,text='fruits',bg='#074463',fg='white',font=('tajawal',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        c6_lbl=Entry(f4,width=10,textvariable=self.fruits,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=5,column=1,padx=10,pady=10)

#***********************bill area***************************
        f5=Frame(self.root,bd=5,relief=GROOVE)
        f5.place(x=968,y=162,width=332,height=382)
        bill_title=Label(f5,text='bill area',font='tajawal 16 bold',bd=5,relief=GROOVE,justify='center').pack(fill=X)
        scroll_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)



#***********************button frame**************************
        f6=LabelFrame(self.root,bd=5,relief=GROOVE,text='bill menu',font=('tajawal',10,'bold'),fg='gold',bg='#074463')
        f6.place(x=0,y=542,relwidth=1,height=158)
        m1_lbl=Label(f6,text='total cosmetics price',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=0,column=0,padx=10,pady=1,sticky='w')
        m1_text=Entry(f6,width=18,textvariable=self.cosmetic_price,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(f6,text='total grocery price',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        m2_text=Entry(f6,width=18,textvariable=self.grocery_price,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=1,column=1,padx=10,pady=10)

        m3_lbl=Label(f6,text='total cold drinks price',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=2,column=0,padx=10,pady=1,sticky='w')
        m3_text=Entry(f6,width=18,textvariable=self.colddrink_price,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(f6,text='cosmetics tax',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=0,column=2,padx=10,pady=1,sticky='w')
        c1_text=Entry(f6,width=18,textvariable=self.cosmetic_tx,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(f6,text='grocery tax',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=1,column=2,padx=10,pady=10,sticky='w')
        c2_text=Entry(f6,width=18,textvariable=self.grocery_tx,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=1,column=3,padx=10,pady=10)

        c3_lbl=Label(f6,text='cold drinks tax',bg='#074463',fg='lightgreen',font=('tajawal',10,'bold')).grid(row=2,column=2,padx=10,pady=1,sticky='w')
        c3_text=Entry(f6,width=18,textvariable=self.colddrink_tx,font=('tajawal',16,'bold'),bd=5,relief=SUNKEN,justify='center').grid(row=2,column=3,padx=10,pady=1)



        btn_frame=Frame(f6,bd=5,relief=GROOVE)
        btn_frame.place(x=780,width=500,height=132)

        total_btn=Button(btn_frame,command=self.total,text='total',bg='cadetblue',fg='white',bd=5,pady=15,width=9,font=('tajawal',12,'bold')).grid(row=0,column=0,padx=8,pady=25)
        gbill_btn=Button(btn_frame,command=self.bill_area,text='genrate bill',bg='cadetblue',fg='white',bd=5,pady=15,width=9,font=('tajawal',12,'bold')).grid(row=0,column=1,padx=8,pady=5)
        clear_btn=Button(btn_frame,command=self.clear,text='clear',bg='cadetblue',fg='white',bd=5,pady=15,width=9,font=('tajawal',12,'bold')).grid(row=0,column=2,padx=8,pady=5)
        exit_btn=Button(btn_frame,command=self.exit,text='exit',bg='cadetblue',fg='white',bd=5,pady=15,width=9,font=('tajawal',12,'bold')).grid(row=0,column=3,padx=8,pady=5)
        self.welcome_bill()

    def total (self):
        self.total_cosmetic_price=float((self.soap.get()*40)+
                                        (self.facecream.get()*120)+
                                        (self.facewash.get()*60)+
                                        (self.spray.get()*180)+
                                        (self.gell.get()*140)+
                                        (self.lotion.get()*180))
        self.cosmetic_price.set(' E£. '+ str(self.total_cosmetic_price))
        self.cosmetic_tx.set(' E£. '+ str(round((self.total_cosmetic_price*0.05),2)))

        self.total_grocery_price=float((self.oil.get()*80)+
                                       (self.rice.get()*180)+
                                       (self.wheat.get()*60)+
                                       (self.sugar.get()*240)+
                                       (self.tea.get()*45)+
                                       (self.macaroni.get()*150))
        self.grocery_price.set(' E£. '+ str(self.total_grocery_price))
        self.grocery_tx.set(' E£. '+ str(round((self.total_grocery_price*0.1),2)))


        self.total_colddrink_price = float((self.juice.get() * 60) +
                                         (self.cock.get() * 60) +
                                         (self.seven.get() * 50) +
                                         (self.souda.get() * 45) +
                                         (self.icetea.get() * 40) +
                                         (self.fruits.get() * 60))
        self.colddrink_price.set(' E£. '+ str(self.total_colddrink_price))
        self.colddrink_tx.set(' E£. '+ str(round((self.total_colddrink_price*0.05),2)))

        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_colddrink_price+
                              (self.total_cosmetic_price*0.05)+
                              (self.total_grocery_price*0.1)+
                              (self.total_colddrink_price*0.05))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t welcome webcode retail\n")
        self.txtarea.insert(END,f"\n bill number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n customer name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n customer phone:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n ====================================")
        self.txtarea.insert(END,f"\n products\t\tqty\t\tprice")
        self.txtarea.insert(END,f"\n ====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("error","you should enter customer details")
        elif self.cosmetic_price.get() == "" and \
             self.grocery_price.get() == "" and \
             self.colddrink_price.get() == "":
            messagebox.showerror("error", "you did not choose any products")
        else:
            self.welcome_bill()
            if self.soap.get() != 0:
                self.txtarea.insert(END, f'\n bath soap\t\t{self.soap.get()}\t\t{self.soap.get() * 40}')
            if self.facecream.get() != 0:
                self.txtarea.insert(END, f'\n face cream\t\t{self.facecream.get()}\t\t{self.facecream.get() * 120}')
            if self.facewash.get() != 0:
                self.txtarea.insert(END, f'\n face wash\t\t{self.facewash.get()}\t\t{self.facewash.get() * 60}')
            if self.spray.get() != 0:
                self.txtarea.insert(END, f'\n hair spray\t\t{self.spray.get()}\t\t{self.spray.get() * 180}')
            if self.gell.get() != 0:
                self.txtarea.insert(END, f'\n hair gel\t\t{self.gell.get()}\t\t{self.gell.get() * 140}')
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f'\n body lotion\t\t{self.lotion.get()}\t\t{self.lotion.get() * 180}')
            # ============================================================================================================
            if self.oil.get() != 0:
                self.txtarea.insert(END, f'\n oil\t\t{self.oil.get()}\t\t{self.oil.get() * 80}')
            if self.rice.get() != 0:
                self.txtarea.insert(END, f'\n rice\t\t{self.rice.get()}\t\t{self.rice.get() * 180}')
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f'\n wheat\t\t{self.wheat.get()}\t\t{self.wheat.get() * 60}')
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f'\n sugar\t\t{self.sugar.get()}\t\t{self.sugar.get() * 240}')
            if self.tea.get() != 0:
                self.txtarea.insert(END, f'\n tea\t\t{self.tea.get()}\t\t{self.tea.get() * 45}')
            if self.macaroni.get() != 0:
                self.txtarea.insert(END, f'\n macaroni\t\t{self.macaroni.get()}\t\t{self.macaroni.get() * 150}')
            # ============================================================================================================
            if self.juice.get() != 0:
                self.txtarea.insert(END, f'\n juice\t\t{self.juice.get()}\t\t{self.juice.get() * 60}')
            if self.cock.get() != 0:
                self.txtarea.insert(END, f'\n cock\t\t{self.cock.get()}\t\t{self.cock.get() * 60}')
            if self.seven.get() != 0:
                self.txtarea.insert(END, f'\n seven\t\t{self.seven.get()}\t\t{self.seven.get() * 50}')
            if self.souda.get() != 0:
                self.txtarea.insert(END, f'\n souda\t\t{self.souda.get()}\t\t{self.souda.get() * 45}')
            if self.icetea.get() != 0:
                self.txtarea.insert(END, f'\n ice tea\t\t{self.icetea.get()}\t\t{self.icetea.get() * 40}')
            if self.fruits.get() != 0:
                self.txtarea.insert(END, f'\n fruits\t\t{self.fruits.get()}\t\t{self.fruits.get() * 60}')

            # ========================================================================================
            self.txtarea.insert(END, f"\n ====================================")
            if self.cosmetic_tx.get() != 0:
                self.txtarea.insert(END, f"\n cosmetics tax\t\t{self.cosmetic_tx.get()}")
            if self.grocery_tx.get() != 0:
                self.txtarea.insert(END, f"\n grocery tax\t\t{self.grocery_tx.get()}")
            if self.colddrink_tx.get() != 0:
                self.txtarea.insert(END, f"\n drinks tax\t\t{self.colddrink_tx.get()}")
            self.txtarea.insert(END, f"\n total bill\t\t E£. {self.total_bill}")
            self.txtarea.insert(END, f"\n ====================================")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("save bill","do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1=open ("customers/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"bill no.  {self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("customers/"):
              if i.split('.')[0]==self.bill_no.get():
                    f1=open(f'customers/{i}','r')
                    self.txtarea.delete(1.0,END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
        if present=='no':
              messagebox.showerror("error","invalid bill no.")

    def clear(self):
        self.soap.set(0)
        self.facecream.set(0)
        self.facewash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.lotion.set(0)
        # ************************variables gros**************************
        self.oil.set(0)
        self.rice.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        self.macaroni.set(0)
        # *************************variables cold drinks**************************
        self.juice.set(0)
        self.cock.set(0)
        self.seven.set(0)
        self.souda.set(0)
        self.icetea.set(0)
        self.fruits.set(0)
        # *************************variables cold drinks**************************
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.colddrink_price.set("")

        self.cosmetic_tx.set("")
        self.grocery_tx.set("")
        self.colddrink_tx.set("")
        # *************************variables CUSTOMER**************************
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("exit","do you really want to exit the program?")
        if op>0:
            self.root.destroy()




root=Tk()
ob = bill_app(root)
root.mainloop()