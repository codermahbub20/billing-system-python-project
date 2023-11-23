from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import random,os
from tkinter import  messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing System Software")

        # =========== Variable for price =====

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.c_bill_no = StringVar()
        z=random.randint(1000,9999)
        self.c_bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        # Product Categories List
        self.Category = ["Select Option","Clothing","LifeStyle","Mobiles"]

        self.SubCategoryClothing = ["Pant","T-Shirt","Shirt"]
        self.pant = ["Levis","Mufti","SpyKar"]
        self.price_levis=1200
        self.price_mufti=1700
        self.price_spyKar=2000
        
        self.T_Shirt = ["Polo","Roadster","Jack&Jones"]
        self.price_polo=1400
        self.price_roadster=1300
        self.price_jackJones=1800

        self.shirt = ["Peter England","Louis Phillipe","Park Avenue"]
        self.price_peter=1190
        self.price_louis=1390
        self.price_park=1690

        #  Sub Category life Style 
        self.SubCategoryLifeStyle  = ["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_Soap = ["Lux","Dove","LifeBuy","Pearl"]
        self.price_life= (20)
        self.price_lux=20
        self.price_dove=70
        self.price_pearl=30

        self.Hair_oil = ["Parasute","Jui","Coconut oil"]
        self.price_parasute=120
        self.price_jui=70
        self.price_coconut=130

        self.Face_Cream = ["Fair&Lovely","Ponds","Grainer"]
        self.price_fair = 60
        self.price_ponds = 80
        self.price_grainer = 100

        self.SubCategoryMobiles  = ["Iphone","SamSung","mi"]

        self.Iphone = ["Iphone_x","Iphone_11","Iphone_14"]
        self.price_ix = 40000
        self.price_11 = 150000
        self.price_14 = 180000

        self.Samsung= ["Samsung M16","Samsung M12","Samsung M21"]
        self.price_m16 = 16000
        self.price_m12 = 11000
        self.price_m21 = 18000

        self.mi = ["Red11","Red12","Red13"]
        self.price_red11 = 12000
        self.price_red12 = 14000
        self.price_red13 = 15000



#-------------------- image part  start----------------------------

    # image number 1
        img = Image.open("./image/banner.png")
        img = img.resize((500, 130)) 
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=500, height=130)

    # image number 2
        img1 = Image.open("./image/banner1.png")
        img1 = img1.resize((500, 130)) 
        self.photoimg_1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg_1)
        lbl_img1.place(x=500, y=0, width=500, height=130)

    # image number 3
        img2 = Image.open("./image/banner2.jpg")
        img2 = img2.resize((500, 130)) 
        self.photoimg_2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg_2)
        lbl_img2.place(x=1000, y=0, width=500, height=130)

# --------------------Header section image part end here-----------------------------------

# -------------------------Header Title code here ----------------------

        lbl_title = Label(self.root,text=" Billing System Software",font=("times new roman",30,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=50)

    # def time():
    #     string=strftime('%H:%M:%S:%p')
    #     lbl.config(text = string)
    #     lbl.after(1000, time)
    #     lbl = Label(title, font = ('times new roman',16,'bold'),background = 'white',fg='red')

    #     lbl.place(x=0,y=0,width=120,height=50)
    #     time()


#---------Header  Title code end here -----------------------------

#---------------Main Frame code start Here ----------------------
        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0,y=180,width=1530,height=620)


#---------------- customer LabelFrame -----------------------
        
        Cust_Frame = LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.label_mob = Label(Cust_Frame, text="Mobile No:", font=("times new roman", 16, "bold"), bg="white")
        self.label_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_Mob = ttk.Entry(Cust_Frame, font=("times new roman", 12, "bold"), width=20)
        self.entry_Mob.grid(row=0, column=1)


        self.lablCustName = Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name: ",bd=4)
        self.lablCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame,textvariable = self.c_name, font=('arial', 10, 'bold'), width=24)

        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lablEmail = Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email: ",bd=4)
        self.lablEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable = self.c_email,font=('arial', 10, 'bold'), width=24)

        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        
#-------------- Product LabelFrame -----------------------
        
        Product_Frame = LabelFrame(Main_Frame,text="Product ",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=740,height=140)

        # Category
        self.lablCategory = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text=" Select Categories: ",bd=4)
        self.lablCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)



        # SubCategory
        self.lablSubCategory = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text=" Select SubCategories: ",bd=4)
        self.lablSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory = ttk.Combobox(Product_Frame,value=[" "],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lablProduct = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name:",bd=4)
        self.lablProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable = self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Product Price
        self.lablPrice = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Price:",bd=4)
        self.lablPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # Product Quantity
        self.lablQty = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Qty:",bd=4)
        self.lablQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty = ttk.Entry(Product_Frame,textvariable = self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        # Middle Frame Photo gallery
        MiddleFrame = Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=1120,height=340)

        # image number 1
        img12 = Image.open("./image/banner.png")
        img12 = img12.resize((490, 340)) 
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lbl_img12 = Label(MiddleFrame, image=self.photoimg12)
        lbl_img12.place(x=0, y=0, width=550, height=340)

    # image number 2
        img13 = Image.open("./image/banner1.png")
        img13 = img1.resize((510, 340)) 
        self.photoimg_13 = ImageTk.PhotoImage(img13)

        lbl_img13 = Label(MiddleFrame, image=self.photoimg_13)
        lbl_img13.place(x=500, y=0, width=570, height=340)


         # Search Frame
        Search_Frame = Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1120,y=10,height=60,width=500)

        self.lablSearch = Label(Search_Frame,font=('arial',12,'bold'),fg="White",bg="red",text="Bill Number")
        self.lablSearch.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame,textvariable = self.search_bill,font=('arial',10,'bold'),width=15)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)




        # Right side Bii area Code Here -----------------
        RightLabelFrame = LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1110, y=45,width=400,height=440)

        scroll_y =Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame,yscrollcommand =scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))

        scroll_y.pack(side=RIGHT,fill =Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        # Bill Counter LabelFrame -----------------------
        
        Bottom_Frame = LabelFrame(Main_Frame,text="Bill Counter ",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        # Product SubTotal
        self.lablSubTotal = Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Product SubTotal:",bd=4)
        self.lablSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal = ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        # Product Tax
        self.labl_tax = Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov Tax:",bd=4)
        self.labl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # Product TotalAmount
        self.lablAmountTotal = Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total:",bd=4)
        self.lablAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal= ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Btn Frame
        Btn_Frame = Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=370,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill=Button(Btn_Frame,command=self.generate_bill,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)

        

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)


        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

    # welcome related code

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Code With Mahbub  Mini Mall ")
        self.textarea.insert(END,f"\n Bill Number : {self.c_bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email: {self.c_email.get()}")


        self.textarea.insert(END,"\n=====================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n=====================================\n")


        self.l=[]
        # Function declaretion
    def AddItem(self):
        Tax = 1
        self.n=self.prices.get()
        self.m = self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()== "":
            messagebox.showerror("Error","Please Select The Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Tk.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Tk.%.2f'%((((sum(self.l)) - self.prices.get())*Tax)/100)))
            self.total.set(str('Tk.%.2f'%(((sum(self.l))+((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def generate_bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Select at least one Product")
        else:
            text = self.textarea.get(10.0,(10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n=====================================")
            self.textarea.insert(END, f"\n Sub Amount: \t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount: \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount: \t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n=====================================")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1 = open('bills/' + self.c_bill_no.get() + ".txt", "w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no:{self.c_bill_no.get() }saved sucesfully")
            f1.close()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]== self.search_bill.get(): 
                f1=open(f"bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                      self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found == "no":
            messagebox.showerror("Invalid Bill No.")   

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set('')        
        self.c_phon.set('')
        self.c_bill_no.set('')
        z=random.randint(1000,9999)
        self.c_bill_no.set(str(x))
        self.c_email.set('')
        self.search_bill.set('')
        self.product.set('')
        self.prices.set(0)
        self.qty.set(0)
        self.sub_total.set('')
        self.tax_input.set('')
        self.total.set('')
        self.welcome()




    def Categories(self,event=""):
         if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCategoryClothing)
            self.ComboSubCategory.current(0)

         if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCategoryLifeStyle)
            self.ComboSubCategory.current(0)

         if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCategoryMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.shirt)
            self.ComboProduct.current(0)

            # LifeStyle Related code
        if self.ComboSubCategory.get() == "Bath Soap":
            self.ComboProduct.config(value = self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Face Cream":
            self.ComboProduct.config(value = self.Face_Cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(value = self.Hair_oil)
            self.ComboProduct.current(0)

            # Mobiles Related code
        if self.ComboSubCategory.get() == "Iphone":
            self.ComboProduct.config(value = self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Samsung":
            self.ComboProduct.config(value = self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "mi":
            self.ComboProduct.config(value = self.mi)
            self.ComboProduct.current(0)

    def price(self,event=""):
        # pant price
        if self.ComboProduct.get() == "Levis":
            self.ComboPrice.config(value = self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Mufti":
            self.ComboPrice.config(value = self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "SpyKar":
            self.ComboPrice.config(value = self.price_spyKar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-Shirt
        if self.ComboProduct.get() == "Polo":
            self.ComboPrice.config(value = self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Roadster":
            self.ComboPrice.config(value = self.price_roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jack&Jones":
            self.ComboPrice.config(value = self.price_jackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Shirt
        if self.ComboProduct.get() == "Peter England":
            self.ComboPrice.config(value = self.price_peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Louis Phillipe":
            self.ComboPrice.config(value = self.price_louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Park Avenue":
            self.ComboPrice.config(value = self.price_park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # LifeStyle  ["Lux","Dove","LifeBuy","Pearl"]
        if self.ComboProduct.get() == "LifeBuy":
            self.ComboPrice.config(value = self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(value = self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Dove":
            self.ComboPrice.config(value = self.price_dove)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Pearl":
            self.ComboPrice.config(value = self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Oil ["Parasute","Jui","Coconut oil"]
        
        if self.ComboProduct.get() == "Parasute":
            self.ComboPrice.config(value = self.price_parasute)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jui":
            self.ComboPrice.config(value = self.price_jui)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Coconut oil":
            self.ComboPrice.config(value = self.price_coconut)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Face Cream ["Fair&Lovely","Ponds","Grainer"]

        if self.ComboProduct.get() == "Fair&Lovely":
            self.ComboPrice.config(value = self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(value = self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Grainer":
            self.ComboPrice.config(value = self.price_grainer)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        # I Phone ["Iphone_x","Iphone_11","Iphone_14"]

        if self.ComboProduct.get() == "Iphone_x":
            self.ComboPrice.config(value = self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_11":
            self.ComboPrice.config(value = self.price_11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_14":
            self.ComboPrice.config(value = self.price_14)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Samsung ["Samsung M16","Samsung M12","Samsung M21"]

        if self.ComboProduct.get() == "Samsung M16":
            self.ComboPrice.config(value = self.price_m16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M12":
            self.ComboPrice.config(value = self.price_m12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M21":
            self.ComboPrice.config(value = self.price_m21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #  Xiomi ["Red11","Red12","Red13"]

        if self.ComboProduct.get() == "Red11":
            self.ComboPrice.config(value = self.price_red11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Red12":
            self.ComboPrice.config(value = self.price_red12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Red13":
            self.ComboPrice.config(value = self.price_red13)
            self.ComboPrice.current(0)
            self.qty.set(1)





if __name__ == '__main__':
    root = Tk()  
    obj = Bill_App(root)
    root.mainloop()
