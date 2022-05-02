from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import pymysql
import re
import pyttsx3
import base64
class signup:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.maxsize(0,0)
        self.root.title("Registrarion Page")
        self.root.config(bg="#52595D")
        self.root.bg= Image.open("regpic.jpg")
        self.photo =ImageTk.PhotoImage(self.root.bg)
        lable2= Label(image=self.photo)
        lable2.pack()
        my_text1= Label(self.root,text="Register Here", font=("time new roman", 30,"bold"),bg="white",fg="#FFA500").place(x=750,y=50)

        frame1 = Frame(self.root,borderwidth=20,bg="#2B547E")
        frame1.place(x=655,y=170, width=540, height=460)

        my_text2= Label(self.root,text="Text Base 1st level of security", font=("time new roman", 15,"bold"),bg="white",fg="red").place(x=770,y=150)

        #-----------Text-to-speech-----------------
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)

    #---------------First name--------------------
        self.val_fname=StringVar()
        f_name=Label(self.root, text="First Name",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=700, y=230)
        self.text_fname=Entry(self.root,font=("time new roman",13), bg="#36454F",fg="white", textvariable=self.val_fname)
        self.text_fname.place(x=700,y=265,width=200, height=30)

        # callback and validation register
        validate_name=self.root.register(self.checkname)
        self.text_fname.config(validate='key',validatecommand=(validate_name,'%P'))

     #-----------Last name--------------------------
        self.val_lname=StringVar()
        l_name=Label(self.root, text="Last Name",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=970, y=230)
        self.text_lname=Entry(self.root,font=("time new roman",13), bg="#36454F",fg="white", textvariable=self.val_lname)
        self.text_lname.place(x=970,y=265,width=200,height=30)

     #-------------------Email---------------------
        self.val_email=StringVar()
        email=Label(self.root, text="Email",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=700, y=315)
        self.text_email=Entry(self.root,font=("time new roman",13), bg="#36454F",fg="white", textvariable=self.val_email)
        self.text_email.place(x=700,y=350,width=200, height=30)

      #-----------------Phone no----------------------
        self.val_contact=StringVar()
        contact=Label(self.root, text="Phone No",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=970, y=315)
        self.text_contact=Entry(self.root,font=("time new roman",13), bg="#36454F",fg="white", textvariable=self.val_contact)
        self.text_contact.place(x=970,y=350,width=200, height=30)

        # callback and validation register
        validate_contact = self.root.register(self.checkcontact)
        self.text_contact.config(validate='key', validatecommand=(validate_contact, '%P'))

      #-----------------password-----------------------
        self.val_password=StringVar()
        password =Label(self.root, text="Password",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=700, y=400)
        self.text_password=Entry(self.root,font=("time new roman",13), bg="#36454F",fg="white", textvariable=self.val_password, show='*')
        self.text_password.place(x=700,y=435,width=200, height=30)

     #----------------conform password--------------------
        self.val_cpassword=StringVar()
        conform_password=Label(self.root, text="Conform Password",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=970, y=400)
        self.text_conform_password=Entry(self.root,font=("time new roman",13),bg="#36454F",fg="white", textvariable=self.val_cpassword, show='*')
        self.text_conform_password.place(x=970,y=435,width=200, height=30)

         #-------------------Security Quistions-----------------

        Security_Questions =Label(self.root, text="Security Questions",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=700, y=485)

         #-----------------Answer-------------
        self.val_answer=StringVar()
        answer=Label(self.root, text="Answer",font=("time new roman", 15),bg="#2B547E",fg="#FFFFFF").place(x=970, y=485)
        self.text_answer=Entry(self.root,font=("time new roman",13),bg="#36454F",fg="white", textvariable=self.val_answer)
        self.text_answer.place(x=970,y=520,width=200, height=30)

        self.cmb_question=StringVar()
        self.cmb_question=ttk.Combobox(self.root,font=("time new roman",13),state='readonly')
        self.cmb_question['values']=("Select", "Your first school name","your birth place", "your best friend name")
        self.cmb_question.place(x=700,y=520, width=200)
        self.cmb_question.current(0)

        # ---------------Sign Up--------------------
        Submit_up = Button(self.root, text="SUBMIT", font=("time new roman", 13, "bold"), border=5, bg="#006400",
                           fg="white", command=self.signup).place(x=830, y=630, width=180, height=40)
        Back = Button(self.root, command=self.back,text="BACK", font=("time new roman", 13, "bold"), border=5, bg="#FD1C03",
                      fg="white").place(x=850, y=670, width=150, height=40)
        #------------------confomation------------------
        self.val_chk=IntVar()
        chk=Checkbutton(self.root,text="I agree the term and conditions",onvalue=1,offvalue=0,font=("time new roman", 13),fg="red",bg="#F5FFFA", variable=self.val_chk).place(x=800,y=570)

        self.check_lbl=Label(self.root,text='',font=("time new roman", 13),bg='#2B547E',fg='red')
        self.check_lbl.place(x=800,y=605)
    #call back Function
    def checkname(self,name):
        if name.isalnum():
            return  True
        if name=='':
            return True
        else:
            self.engine.say('space dos not allow ')
            self.engine.runAndWait()
            messagebox.showerror('Invalid',"Not Allowed"+name[-1])
            return False

    #checkcontact
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return  True
        else:
            self.engine.say('character dos not exit in phone number ')
            self.engine.runAndWait()
            messagebox.showerror('Invalid',"Invalid Entry")
            return False

    #checkpassword
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))", password):
                return True
            else:
                self.engine.say('Please Enter Strong Password')
                self.engine.runAndWait()
                messagebox.showinfo('Invalid', "Please Enter Strong Password")
                return False
        else:
            self.engine.say(' length try to exceed')
            self.engine.runAndWait()
            messagebox.showerror("invalid","length try to exceed")
            return False

    #checkemail
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                self.engine.say('invalid email, Enter valid email ')
                self.engine.runAndWait()
                messagebox.showwarning("Alert","invalid email, Enter valid email (example:codewith11@gmail.com)")
                return False
        else:
            self.engine.say('Email length is too small ')
            self.engine.runAndWait()
            messagebox.showinfo("Invalid","Email length is too small")


    def clear1_text(self):
        self.text_answer.delete(0,END)
        self.text_fname.delete(0,END)
        self.text_lname.delete(0,END)
        self.text_email.delete(0,END)
        self.text_password.delete(0,END)
        self.text_conform_password.delete(0,END)

    def signup(self):
        if self.val_fname.get()=="":
            self.engine.say('please Enter your First Name')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your First Name", parent=self.root)
        elif self.val_lname.get()=="":
            self.engine.say('please Enter your Last Name')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your Last Name", parent=self.root)
        elif self.val_email.get()=="":
            self.engine.say('please Enter your Email')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your Email", parent=self.root)
        elif self.val_contact.get()=="" :
            self.engine.say('please Enter your contact number')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your contact number", parent=self.root)
        elif len(self.val_contact.get())!=10:
            self.engine.say('please Enter your valid contact number')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your valid contact number", parent=self.root)
        elif self.val_password.get()=="":
            self.engine.say('please Enter your password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your password", parent=self.root)
        elif self.val_cpassword.get()=="":
            self.engine.say('please Enter your conform Password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your conform Password", parent=self.root)
        elif self.val_password.get()!= self.val_cpassword.get():
            self.engine.say('Password & Conform password should be same')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Password & Conform password should be same!", parent=self.root)
        elif self.val_answer.get()=="":
            self.engine.say('please Enter your Answer')
            self.engine.runAndWait()
            messagebox.showerror("Error", "please Enter your Answer", parent=self.root)
        elif self.val_email.get()!=None and self.val_password.get()!=None:
            self.x=self.checkemail(self.val_email.get())
            self.y=self.checkpassword(self.val_password.get())
            password = self.val_password.get()
            self.encrypted_password = base64.b85encode(password.encode(str("utf-8")))
        if (self.x==True) and (self.y==True):
            if self.val_chk.get()==0:
                self.engine.say('Please Agree our terms & Conditions')
                self.engine.runAndWait()
                self.check_lbl.config(text='Please Agree our terms & Conditions', fg='red')

            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="employee3")
                    cur=con.cursor()
                    cur.execute("select * from student where email=%s",self.val_email.get())
                    row=cur.fetchone()
                    #print(row)
                    if row!=None:
                        self.engine.say('User already exist,Please try with another email ')
                        self.engine.runAndWait()
                        messagebox.showinfo("Error", "User already exist,Please try with another email", parent=self.root)
                    else:
                        cur.execute("insert into student(f_name,l_name,email,contact,password,question,answer) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.val_fname.get(),
                                     self.val_lname.get(),
                                     self.val_email.get(),
                                     self.val_contact.get(),
                                     self.encrypted_password,
                                     self.cmb_question.get(),
                                     self.val_answer.get()

                                     ))
                        con.commit()
                        con.close()
                        self.engine.say('Congratulation you are successfully register ')
                        self.engine.runAndWait()
                        messagebox.showinfo("Success", "Text base password Successfully register", parent=self.root)
                        self.clear1_text()
                        self.next()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)



    def back(self):
        self.root.destroy()
        import Home_page


    #*****************************************Secod Label of colour base  Security_Page*****************************

    def colour_signup(self):
        if self.scvalue.get()=="":
            self.engine.say('Please select your password ')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please select your password", parent=self.window)

        else:
            try:
                if self.scvalue.get()!=None:
                    color_password=self.scvalue.get()
                    self.color_encrypted_password = base64.b85encode(color_password.encode(str("utf-8")))
                con=pymysql.connect(host="localhost",user="root",password="",database="employee3")
                cur = con.cursor()
                cur.execute("update student set ga_password=%s where email=%s",(self.color_encrypted_password,self.val_email.get()))

                con.commit()
                con.close()
                self.engine.say('Congratulation colour base password Successfully register ')
                self.engine.runAndWait()
                messagebox.showinfo("Success", "colour base password Successfully register", parent=self.window)
                self.next_page()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.window)


    def next(self):
        self.window = Toplevel()
        self.window.title("Second Level of security")
        self.window.geometry('550x540+650+170')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        my_text4 = Label(self.window, text="Graphical Password", font=("time new roman", 25, "bold"), bg="white",fg="blue").place(x=120, y=20)
        my_text3 = Label(self.window, text="Colour Base 2nd lavel of security", font=("time new roman", 15, "bold"), bg= "white", fg="red").place(x=150, y=80)

        def click(event):
            text = event.widget.cget("text")
            if text == "=":
                pass
            elif text == "C":
                pass
            else:
                self.scvalue.set(self.scvalue.get() + text)

        red = Button(self.window, text="red10", font=("time new roman", 13), border=5, bg="red", fg="red",activebackground='red', activeforeground='red')
        red.place(x=50, y=180, width=150, height=40)
        red.bind("<Button-1>", click)

        red = Button(self.window, text="blue20", font=("time new roman", 13), border=5, bg="blue", fg="blue",activebackground='blue', activeforeground='blue', width=15)
        red.place(x=200, y=150, width=150, height=40)
        red.bind("<Button-1>", click)

        red = Button(self.window, text="green30", font=("time new roman", 13), border=5, bg="green", fg="green", activebackground='green', activeforeground='green',width=15)
        red.place(x=350, y=180, width=150, height=40)
        red.bind("<Button-1>", click)

        red = Button(self.window, text="yellow40", font=("time new roman", 13), border=5, bg="yellow", fg="yellow",activebackground='yellow', activeforeground='yellow', width=15)
        red.place(x=200, y=220, width=150, height=40)
        red.bind("<Button-1>", click)

        self.scvalue = StringVar()
        self.screen= Entry(self.window, textvariable=self.scvalue, font="lucida 20 bold",bg="#36454F",fg="white", show='*').place(x=120, y=300)

        Submit = Button(self.window, text="SAVE", font=("time new roman", 13,"bold"), border=5, bg="#006400", fg="white",command=self.colour_signup).place(x=200, y=400, width=150, height=40)

     #********************************Third level of image base Security Page*************************************

    def back1(self):
        self.window1.destroy()
        self.window.destroy()
        self.root.destroy()
        import Home_page
    def clear3_text(self):
        self.screen1.delete(0,END)

    def image_signup(self):
        if self.screen.get()=="":
            self.engine.say('Please select your password ')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please select your password", parent=self.window1)

        else:
            try:
                if self.screen.get()!=None:
                    Image_password=self.screen.get()
                    self.image_encrypted_password = base64.b85encode(Image_password.encode(str("utf-8")))
                con=pymysql.connect(host="localhost",user="root",password="",database="employee3")
                cur = con.cursor()
                cur.execute("update student set gb_password=%s where email=%s",(self.image_encrypted_password,self.val_email.get()))
                con.commit()
                con.close()
                self.engine.say('Congratulation Image base password Successfully register ')
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Image base password Successfully register", parent=self.window1)
                self.clear3_text()
                self.back1()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.window1)

#-----------------------------Main page of image base password-------------------
    def next_page(self):
        self.window1 = Toplevel()
        self.window1.title("Third Level of security")
        self.window1.geometry('550x540+650+170')
        self.window1.config(bg='white')
        self.window1.resizable(False, False)
        my_text4 = Label(self.window1, text="Graphical Password", font=("time new roman", 25, "bold"), bg="white",fg="#B422E6").place(x=20, y=20, relwidth=1)
        my_text3 = Label(self.window1, text="Image Base 3nd lavel of security", font=("time new roman", 15, "bold"), bg="white", fg="red").place(x=120, y=80)

        self.var1 = StringVar()
        self.bg1 = Image.open("image11111.jpg")
        self.resizeA = self.bg1.resize((100, 100), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.resizeA)

        self.bg2 = Image.open("image22222.jpg")
        self.resizeB = self.bg2.resize((100, 100), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.resizeB)

        self.bg3 = Image.open("image33333.jpg")
        self.resizeC = self.bg3.resize((100, 100), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.resizeC)

        self.bg4 = Image.open("image44444.jpg")
        self.resizeD = self.bg4.resize((100, 100), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(self.resizeD)

        self.bg5 = Image.open("image1111.jpg")
        self.resizeE = self.bg5.resize((100, 100), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(self.resizeE)

        self.bg6 = Image.open("image2222.jpg")
        self.resizeF = self.bg6.resize((100, 100), Image.ANTIALIAS)
        self.photo6 = ImageTk.PhotoImage(self.resizeF)

        self.bg7 = Image.open("image3333.jpg")
        self.resizeG = self.bg7.resize((100, 100), Image.ANTIALIAS)
        self.photo7 = ImageTk.PhotoImage(self.resizeG)

        self.bg8 = Image.open("image4444.jpg")
        self.resizeH = self.bg8.resize((100, 100), Image.ANTIALIAS)
        self.photo8 = ImageTk.PhotoImage(self.resizeH)

        self.bg9 = Image.open("image111.jpg")
        self.resizeI = self.bg9.resize((100, 100), Image.ANTIALIAS)
        self.photo9 = ImageTk.PhotoImage(self.resizeI)

        self.bg10 = Image.open("image222.jpg")
        self.resizeJ = self.bg10.resize((100, 100), Image.ANTIALIAS)
        self.photo10 = ImageTk.PhotoImage(self.resizeJ)

        self.bg11 = Image.open("image333.jpg")
        self.resizeK = self.bg11.resize((100, 100), Image.ANTIALIAS)
        self.photo11 = ImageTk.PhotoImage(self.resizeK)

        self.bg12 = Image.open("image444.jpg")
        self.resizeL = self.bg12.resize((100, 100), Image.ANTIALIAS)
        self.photo12 = ImageTk.PhotoImage(self.resizeL)

        self.screen = StringVar()
        self.screen1 = Entry(self.window1, textvariable=self.screen, font="lucida 20 bold", bg="white", fg="white",bd=0,show='*')
        self.screen1.place(x=120, y=150, width=200, height=30)

        def onclick(event):
            text = event.widget.cget("text")
            if text == "=":
                pass
            elif text == "C":
                pass
            else:
                self.screen.set(self.screen.get() + text)

        Next = Button(self.window1, image=self.photo1, font=("time new roman", 13, "bold"),text='1',border=2)
        Next.place(x=70, y=150,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo2, font=("time new roman", 13, "bold"),text='2', border=2)
        Next.place(x=170,y=150,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo3, font=("time new roman", 13, "bold"),text='3', border=2)
        Next.place(x=270,y=150,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo4, font=("time new roman", 13, "bold"),text='4', border=2)
        Next.place(x=370,y=150,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo5, font=("time new roman", 13, "bold"),text='5', border=2)
        Next.place(x=70, y=250,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo6, font=("time new roman", 13, "bold"),text='6', border=2)
        Next.place(x=170,y=250,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo7, font=("time new roman", 13, "bold"),text='7', border=2)
        Next.place(x=270,y=250,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo8, font=("time new roman", 13, "bold"),text='8', border=2)
        Next.place(x=370,y=250,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo9, font=("time new roman", 13, "bold"),text='9', border=2)
        Next.place(x=70, y=350,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo10, font=("time new roman", 13, "bold"),text='10', border=2)
        Next.place(x=170,y=350,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo11, font=("time new roman", 13, "bold"),text='11', border=2)
        Next.place(x=270,y=350,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo12, font=("time new roman", 13, "bold"),text='12', border=2)
        Next.place(x=370,y=350,width=100,height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1,command=self.image_signup, text="Save", font=("time new roman", 13, "bold"), border=5, bg="#006400", fg="white")
        Next.place(x=200, y=480, width=150, height=40)

        def back(self):
            self.root.destroy()

root=Tk()
obj=signup(root)
root.mainloop()