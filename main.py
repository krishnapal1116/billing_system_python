from tkinter import *
from tkinter import  ttk 
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x800+0+0")
       self.root.title("Billing System")

       self.c_name=StringVar()
       self.c_phone=StringVar()
       self.c_email=StringVar()
       self.bill_no=StringVar()
       z=random.randint(1000,99999)
       self.bill_no.set(z)
       self.search_bill=StringVar()
       self.product=StringVar()
       self.sub_total=StringVar()
       self.tax_input=StringVar()
       self.total=StringVar()
       self.qty=IntVar()
       self.prices=IntVar()



       #product category list
       self.category=["Select Option","Mobile","Clothing","Laptop"]

       #subcat mobile
       self.subcatmobile=["Oppo","Vivo","Poco"]

       self.Oppo=["A59_5G","A78_5G","A3_Pro_5G"]
       self.priceA59_5G=15499
       self.priceA78_5G=17499
       self.priceA3_Pro_5G=17999
       
       self.Vivo=["T3x","T2x","Y18e"]
       self.price_T3x=14999
       self.price_T2x=13950
       self.price_Y18e=8865

       self.Poco=["C65","X6","F6"]
       self.price_C65=7499
       self.price_X6=21999
       self.price_F6=29999

       #subcat cloth 
       self.subcatClothing=["Pent","Shirt","T_Shirt"]

       self.Pent=["Killer","Raymond","Floreos"]
       self.price_Killer=927
       self.price_Raymond=879
       self.price_Floreos=497

       self.Shirt=["Surhi","Arham","Febq"]
       self.price_Surhi=299
       self.price_Arham=242
       self.price_Febq=299

       self.T_Shirt=["Rodzen","Fasla"]
       self.price_Rodzen=459
       self.price_Fasla=279

       #subcat laptop
       self.subcatlaptop=["Asus","Hp"]

       self.Asus=["Vivobook14","ExpertbookB15","TufF15"]
       self.price_Vivobook14=34990
       self.price_ExpertbookB15=33999
       self.price_TufF15=47990

       self.Hp=["Amd5","Chromebook"]
       self.price_Amd5=39990
       self.price_Chromebook=10990


       #heading
       lbl_title=Label(self.root,text="BILLING SOFTWARE FOR A SHOP",font=("times new roman",40,"bold"),bg="white",bd=5,fg="purple")
       lbl_title.place(x=0,y=50,width=1530,height=45)

       def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)

        lbl = Label(lbl_title,font=("times new roman",40,"bold"),bg="red",fg="blue")
        lbl.place(x=0,y=50,width=100,height=45)
        time()
         

       Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
       Main_Frame.place(x=0,y=100,width=1280,height=548)

       #customer fream
       Cust_Frame=LabelFrame(Main_Frame,text="CUSTOMER",font=("times new roman",12,"bold"),bg="white",fg="red")
       Cust_Frame.place(x=10,y=5,width=295,height=140)

       #mob no
       self.lbl_mob=Label(Cust_Frame,text="Mobile No:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

       self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
       self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

       #name
       self.lblCustName=Label(Cust_Frame,text="Name:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

       self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=24)
       self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

       #email
       self.lblEmail=Label(Cust_Frame,text="Email:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

       self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=24)
       self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

       #product fream
       product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
       product_Frame.place(x=310,y=5,width=540,height=140)
       
       #catagory
       self.lblCategory=Label(product_Frame,text="Catagory:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

       self.Combo_category=ttk.Combobox(product_Frame,value=self.category,font=("times new roman",10,"bold"),width=20,state="readonly")
       self.Combo_category.current(0)
       self.Combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
       self.Combo_category.bind("<<ComboboxSelected>>",self.Categories)
       
       #subccatagory
       self.lblsubCategory=Label(product_Frame,text="Sub Catagory:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblsubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

       self.Combosubcategory=ttk.Combobox(product_Frame,value=[""],font=("times new roman",10,"bold"),width=20,state="readonly")
       self.Combosubcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
       self.Combosubcategory.bind("<<ComboboxSelected>>",self.Product_add)

       #product
       self.lblproduct=Label(product_Frame,text="Product:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

       self.Comboproduct=ttk.Combobox(product_Frame,textvariable=self.product,font=("times new roman",10,"bold"),width=20,state="readonly")
       self.Comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
       self.Comboproduct.bind("<<ComboboxSelected>>",self.price)

       #price
       self.lblprice=Label(product_Frame,text="Price:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

       self.Comboprice=ttk.Combobox(product_Frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=18,state="readonly")
       self.Comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

       #qty
       self.lblqty=Label(product_Frame,text="Quntity:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

       self.Comboqty=ttk.Entry(product_Frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=21)
       self.Comboqty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

      
       #middle photo fream
       Mphoto_Frame=LabelFrame(Main_Frame,bg="white")
       Mphoto_Frame.place(x=10,y=150,width=840,height=260)

       #search fream
       Search_Frame=LabelFrame(Mphoto_Frame,text="Searching Area",font=("times new roman",12,"bold"),bg="white",fg="red")
       Search_Frame.place(x=450,y=0,width=385,height=65)


       #billno
       self.lblBillNo=Label(Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),bg="royalblue3",bd=4,fg="white")
       self.lblBillNo.grid(row=0,column=0,sticky=W,padx=5,pady=2)

       self.txtBillNo=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",10,"bold"),width=28)
       self.txtBillNo.grid(row=0,column=1,sticky=W,padx=5,pady=2)

       #search
       self.lblSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",12,"bold"),bg="royalblue",fg="white",cursor="hand2")
       self.lblSearch.grid(row=0,column=2,sticky=W,padx=2,pady=2)



       #billarea
       RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
       RightLabelFrame.place(x=870,y=10,width=380,height=401)

       #scrollbar
       scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
       self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",11,"bold"))
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_y.config(command=self.textarea.yview)
       self.textarea.pack(fill=BOTH,expand=1)

       #bill counter fream
       Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
       Bottom_Frame.place(x=0,y=410,width=1265,height=125)

       #sub total
       self.lblsubtotal=Label(Bottom_Frame,text="Sub Total:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

       self.Entrysubtotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=21)
       self.Entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

       #tax
       self.lbltax=Label(Bottom_Frame,text="Tax:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

       self.Entrytax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",10,"bold"),width=21)
       self.Entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

       #total
       self.lbltotal=Label(Bottom_Frame,text="Total:",font=("times new roman",12,"bold"),bg="white",bd=4)
       self.lbltotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

       self.Entrytotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",10,"bold"),width=21)
       self.Entrytotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

       #key
       Key_Frame=Frame(Bottom_Frame,bd=2,bg="white")
       Key_Frame.place(x=270,y=0)

       #add
       self.KeyAddToCart=Button(Key_Frame,command=self.AddItem,text="Add To Cart",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeyAddToCart.grid(row=0,column=0)

       #generate
       self.KeyGenerate=Button(Key_Frame,command=self.gen_bill,text="Generate Bill",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeyGenerate.grid(row=0,column=1)

       #save
       self.KeySave=Button(Key_Frame,command=self.save_bill,text="Save Bill",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeySave.grid(row=0,column=2)

       #print
       self.KeyPrint=Button(Key_Frame,command=self.iprint,text="Print Bill",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeyPrint.grid(row=0,column=3)

       #clear
       self.KeyClear=Button(Key_Frame,command=self.clear_bill,text="Clear",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeyClear.grid(row=0,column=4) 
       
       #exit
       self.KeyExit=Button(Key_Frame,command=self.root.destroy,text="Exit",font=("times new roman",15,"bold"),bg="green",fg="white",width=12,cursor="hand2",height=2)
       self.KeyExit.grid(row=0,column=5)
       self.welcome()

       self.l=[]

      #++++++++++++++++++++++++ All Function +++++++++++++++++++++++ 

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t WELCOME TO OUR SHOP")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Email Id:{self.c_email.get()}")

        self.textarea.insert(END,"\n =======================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrices")
        self.textarea.insert(END,"\n =======================================\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select The Product Name")
        else:
            self.textarea.insert(END,f"\n  {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100))))) 


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n =======================================")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=======================================")    


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Done")
            f1.close()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found='no'
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("ERROR","Enter Valid Bill No")


    def clear_bill(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        z=random.randint(1000,99999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.product.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.qty.set("0")
        self.prices.set("0")
        self.l=[0]
        self.welcome()

    
    
    
    def Categories(self,event=""):
        if self.Combo_category.get()=="Mobile":
            self.Combosubcategory.config(value=self.subcatmobile)
            self.Combosubcategory.current(0)

        if self.Combo_category.get()=="Clothing":
            self.Combosubcategory.config(value=self.subcatClothing)
            self.Combosubcategory.current(0)

        if self.Combo_category.get()=="Laptop":
            self.Combosubcategory.config(value=self.subcatlaptop)
            self.Combosubcategory.current(0)

    def Product_add(self,event=""):
        if self.Combosubcategory.get()=="Oppo":
            self.Comboproduct.config(value=self.Oppo)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="Vivo":
            self.Comboproduct.config(value=self.Vivo)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="Poco":
            self.Comboproduct.config(value=self.Poco)
            self.Comboproduct.current(0)

        #cloth
        if self.Combosubcategory.get()=="Pent":
            self.Comboproduct.config(value=self.Pent)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="Shirt":
            self.Comboproduct.config(value=self.Shirt)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="T_Shirt":
            self.Comboproduct.config(value=self.T_Shirt)
            self.Comboproduct.current(0)
       
        #laptop
        if self.Combosubcategory.get()=="Asus":
            self.Comboproduct.config(value=self.Asus)
            self.Comboproduct.current(0)
        
        if self.Combosubcategory.get()=="Hp":
            self.Comboproduct.config(value=self.Hp)
            self.Comboproduct.current(0)

         #oppo
    def price(self,event=""):
        if self.Comboproduct.get()=="A59_5G":
            self.Comboprice.config(value=self.priceA59_5G)
            self.Comboprice.current(0)
            self.qty.set(1)
        
        if self.Comboproduct.get()=="A78_5G":
            self.Comboprice.config(value=self.priceA78_5G)
            self.Comboprice.current(0)
            self.qty.set(1)
        
        if self.Comboproduct.get()=="A59_5G":
            self.Comboprice.config(value=self.priceA59_5G)
            self.Comboprice.current(0)
            self.qty.set(1)

        #vivo
        if self.Comboproduct.get()=="T3x":
            self.Comboprice.config(value=self.price_T3x)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="T2x":
            self.Comboprice.config(value=self.price_T2x)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Y18e":
            self.Comboprice.config(value=self.price_Y18e)
            self.Comboprice.current(0)
            self.qty.set(1)

        #poco
        if self.Comboproduct.get()=="C65":
            self.Comboprice.config(value=self.price_C65)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="X6":
            self.Comboprice.config(value=self.price_X6)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="F6":
            self.Comboprice.config(value=self.price_F6)
            self.Comboprice.current(0)
            self.qty.set(1)
        
        #Pent
        if self.Comboproduct.get()=="Killer":
            self.Comboprice.config(value=self.price_Killer)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Raymond":
            self.Comboprice.config(value=self.price_Raymond)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Floreos":
            self.Comboprice.config(value=self.price_Floreos)
            self.Comboprice.current(0)
            self.qty.set(1)
        #Shirt
        if self.Comboproduct.get()=="Surhi":
            self.Comboprice.config(value=self.price_Surhi)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Arham":
            self.Comboprice.config(value=self.price_Arham)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Febq":
            self.Comboprice.config(value=self.price_Febq)
            self.Comboprice.current(0)
            self.qty.set(1)
        #T_Shirt=["Rodzen","Fasla"]
        if self.Comboproduct.get()=="Rodzen":
            self.Comboprice.config(value=self.price_Rodzen)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Fasla":
            self.Comboprice.config(value=self.price_Fasla)
            self.Comboprice.current(0)
            self.qty.set(1)
        #Asus=["Vivobook14","ExpertbookB15","TufF15"]
        if self.Comboproduct.get()=="Vivobook14":
            self.Comboprice.config(value=self.price_Vivobook14)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="ExpertbookB15":
            self.Comboprice.config(value=self.price_ExpertbookB15)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="TufF15":
            self.Comboprice.config(value=self.price_TufF15)
            self.Comboprice.current(0)
            self.qty.set(1)

        #Hp=["Amd5","Chromebook"]
        if self.Comboproduct.get()=="Amd5":
            self.Comboprice.config(value=self.price_Amd5)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Chromebook":
            self.Comboprice.config(value=self.price_Chromebook)
            self.Comboprice.current(0)
            self.qty.set(1)

       


if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()