from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import pymysql
import time
import pyttsx3
import  base64
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.bg=Image.open("login.jpg")
        self.resizeA=self.bg.resize((1525,800), Image.ANTIALIAS)
        self.photo= ImageTk.PhotoImage(self.resizeA)
        self.bg_image=Label(self.root,image=self.photo).place(x=0,y=0)

        # -----------Text-to-speech-----------------
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        #-----------Login Frame------------------
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=600,y=120,height=500,width=500)


#****************************************First level of text base Security Page ***********************************

        #---------------------------Main Design of Text-based password-----------------------------------------

        title=Label(Frame_login,text="login Here",font=("time new roman",25,"bold"),fg="#d77337",bg="white").place(x=170,y=30)
        desc = Label(Frame_login, text=" Text Base Password Login", font=("time new roman", 12, "bold"), fg="#d25d17",
                      bg="white").place(x=100, y=90)
        lbl_user= Label(Frame_login, text="Email", font=("time new roman", 15, "bold"), fg="gray",
                      bg="white").place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("time new roman", 15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=300,height=35)

        lbl_password= Label(Frame_login, text="Password", font=("time new roman", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_password = Entry(Frame_login, font=("time new roman", 15), bg="lightgray", show='*')
        self.txt_password.place(x=90, y=240, width=300, height=35)

        forget=Button(Frame_login,command=self.forget_password,cursor="hand2",text="Forget Password?", bg="white",fg="#d77337",bd=0,
                      font=("time new roman",12)).place(x=130,y=280)
        Login = Button(Frame_login, command=self.login_function,text="Login", bg="#d77337", fg="white",
                        font=("time new roman", 12,"bold")).place(x=170, y=330,width=150,height=40)
        Back= Button(Frame_login, command=self.Back, text="Back", bg="#d77337", fg="white",
                       font=("time new roman", 12, "bold")).place(x=50, y=450, width=150, height=40)
        register_label = Label(Frame_login, text="If you not Registered go Back to Register!", font=("time new roman", 12),
                        fg="red",bg="white").place(x=50, y=400)


    #-----------------------------Forget and reset Password of text base security--------------------------
    def clear_reset_password(self):
        self.cmb_question.delete(0)
        # self.new_password.delete(0,END)
        # self.val_answer.delete(0,END)
        self.txt_user.delete(0,END)
    def reset_password(self):
        if self.cmb_question.get()=="" or self.new_password.get()=="" or self.val_answer.get()=="":
            self.engine.say('All fields are required')
            self.engine.runAndWait()
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                if self.new_password.get()!=None:
                    text_base_password = self.new_password.get()
                    self.reset_encrypted_text_password = base64.b85encode(text_base_password.encode(str("utf-8")))
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and question=%s and answer=%s", (self.txt_user.get(),self.cmb_question.get(),self.val_answer.get()))
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter the correct Security question and answer')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter the correct Security question and answer", parent=self.root2)
                else:
                    cur.execute("update student set password=%s where email=%s",(self.reset_encrypted_text_password,self.txt_user.get()))
                    con.commit()
                    con.close()
                    self.engine.say('Your password has been reset, Please login with new password!')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success","Your password has been reset, Please login with new password!",parent=self.root2)
                    self.clear_reset_password()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root2)

    #-------------------------Forget function of text_base Password-------------------------------
    def forget_password(self):
        if self.txt_user.get()=="":
            self.engine.say('Please Enter email address to reset your password')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter email address to reset your password",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s",self.txt_user.get())
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter The Valid Email Address')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter The Valid Email Address", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x420+650+190")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title = Label(self.root2, text="Forget Password", font=("time new roman", 15, "bold"), fg="red",
                                  bg="white").place(x=7, y=10, relwidth=1)

                    # -------------------Security Quistions-----------------
                    Security_Questions = Label(self.root2, text="Security Question",font=("time new roman", 15), bg="white", fg="gray").place(x=40, y=70)

                    # -----------------Answer-------------
                    self.val_answer = StringVar()
                    answer = Label(self.root2, text="Answer",font=("time new roman", 15), bg="white", fg="gray").place(x=40, y=150)
                    self.text_answer = Entry(self.root2, font=("time new roman", 13), bg="lightgray", fg="black",
                                        textvariable=self.val_answer).place(x=40, y=180, width=200, height=30)

                    self.cmb_question = StringVar()
                    self.cmb_question = ttk.Combobox(self.root2, textvariable=self.cmb_question,font=("time new roman", 13), state='readonly')
                    self.cmb_question['values'] = ("Select", "Your first school name", "your birth place", "your best friend name")
                    self.cmb_question.place(x=40, y=100, width=200)
                    self.cmb_question.current(0)

                    #______________________New Password________________________
                    self.new_password = StringVar()
                    new_password = Label(self.root2, text="New Password", font=("time new roman", 15), bg="white",fg="gray").place(x=40, y=230)
                    self.text_new_password = Entry(self.root2,textvariable=self.new_password,font=("time new roman", 13), bg="lightgray", fg="black",show='*').place(x=40, y=260, width=200, height=30)
                    reset_password = Button(self.root2, command=self.reset_password,text="Reset Password", bg="#d77337", fg="white",
                                            font=("time new roman", 12, "bold")).place(x=75, y=330, width=150,height=40)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)

    def Back(self):
        self.root.destroy()
        import Home_page
    #-------------------Clear text of text_base_password----------------------
    def clear1_text(self):
        #self.txt_user.delete(0,END)
        self.txt_password.delete(0,END)

    # ---------------------------Login Function of text base security---------------------
    def login_function(self):
        if  self.txt_user.get()=="":
            self.engine.say('Please Enter your Email address')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter your Email address",parent=self.root)
        elif self.txt_password.get()=="":
            self.engine.say('Please Enter your password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please Enter your Password", parent=self.root)
        else:
            try:
                if self.txt_password.get()!=None:
                    password = self.txt_password.get()
                    self.encrypted_password = base64.b85encode(password.encode(str("utf-8")))
                con=pymysql.connect(host="localhost",user="root",password="",database="employee3")
                cur=con.cursor()
                cur.execute("select * from student where email=%s and password=%s",(self.txt_user.get(),self.encrypted_password))
                row=cur.fetchone()
                if row==None:
                    self.engine.say('Invalid USERNAME & PASSWORD')
                    self.engine.runAndWait()
                    messagebox.showerror("Error","Invalid USERNAME &PASSWORD",parent=self.root)
                    self.clear1_text()
                else:
                    self.engine.say('Congratulation Succssfully login')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Succssfully login",parent=self.root)
                    self.clear1_text()
                    self.next()
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)


# ********************************Secend level of colour base Security Page*************************************


    #----------------Colour base rest_Password Function-----------------------
    def reset_colour_base_password(self):
        if self.cmb_color_question.get()=='' or self.val_color_answer.get()=='' or self.scvalue_color.get()=='':
            self.engine.say('All field are required')
            self.engine.runAndWait()
            messagebox.showerror("Error", "All field are required",parent=self.root3)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and question=%s and answer=%s",
                            (self.val_email.get(), self.cmb_color_question.get(), self.val_color_answer.get()))
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter the correct Security question and answer')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter the correct Security question and answer",parent=self.root3)
                else:
                    if self.scvalue_color.get()!=None:
                        color_base_reset_password = self.scvalue_color.get()
                        self.reset_encrypted_color_password = base64.b85encode(color_base_reset_password.encode(str("utf-8")))
                    cur.execute("update student set ga_password=%s where email=%s",(self.reset_encrypted_color_password, self.val_email.get()))
                    con.commit()
                    con.close()
                    self.engine.say('Your password has been reset, Please login with new password!')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Your password has been reset, Please login with new password!",parent=self.root3)
                    self.root3.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root3)

    # ----------------Colour base forget_Password Function-----------------------
    def colour_forget_password(self):
        if self.val_email.get() == "":
            self.engine.say('Please Enter email address to reset your password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please Enter email address to reset your password", parent=self.window)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.val_email.get())
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter The Valid Email Address')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter The Valid Email Address", parent=self.window)
                else:
                    con.close()
                    self.root3 = Toplevel()
                    self.root3.title("Forget Password")
                    self.root3.geometry("450x490+650+200")
                    self.root3.config(bg="white")
                    self.root3.resizable(False, False)
                    self.root3.focus_force()
                    self.root3.grab_set()

                    title = Label(self.root3, text="Forget Password", font=("time new roman", 15, "bold"), fg="red",bg="white").place(x=7, y=10, relwidth=1)
                    Security_Questions = Label(self.root3, text="Security Question",font=("time new roman", 15), bg="white", fg="gray").place(x=100, y=70)

                    # -----------------Answer-------------
                    self.val_color_answer = StringVar()
                    answer = Label(self.root3, text="Answer", font=("time new roman", 15), bg="white", fg="gray").place(x=100, y=140)
                    self.text_color_answer = Entry(self.root3, font=("time new roman", 13), bg="lightgray", fg="black",textvariable=self.val_color_answer).place(x=110, y=170, width=200, height=30)

                    self.cmb_color_question = StringVar()
                    self.cmb_color_question = ttk.Combobox(self.root3, textvariable=self.cmb_color_question, font=("time new roman", 13),state='readonly')
                    self.cmb_color_question['values'] = ("Select", "Your first school name", "your birth place", "your best friend name")
                    self.cmb_color_question.place(x=110, y=100, width=200)
                    self.cmb_color_question.current(0)

                    new_password = Label(self.root3, text="Enter New coloure base Password", font=("time new roman", 15), bg="white",fg="gray").place(x=50, y=220)

                    def click(event):
                        text = event.widget.cget("text")
                        if text == "=":
                            pass
                        elif text == "C":
                            pass
                        else:
                            self.scvalue_color.set(self.scvalue_color.get() + text)

                    red = Button(self.root3, text="red10", font=("time new roman", 13), border=5, bg="red", fg="red", activebackground='red', activeforeground='red')
                    red.place(x=60, y=270, width=70, height=40)
                    red.bind("<Button-1>", click)

                    red = Button(self.root3, text="blue20", font=("time new roman", 13), border=5, bg="blue", fg="blue", activebackground='blue', activeforeground='blue',width=15)
                    red.place(x=150, y=270, width=70, height=40)
                    red.bind("<Button-1>", click)

                    red = Button(self.root3, text="green30", font=("time new roman", 13), border=5, bg="green", fg="green", activebackground='green', activeforeground='green',width=15)
                    red.place(x=240, y=270, width=70, height=40)
                    red.bind("<Button-1>", click)

                    red = Button(self.root3, text="yellow40", font=("time new roman", 13), border=5, bg="yellow", fg="yellow", activebackground='yellow', activeforeground='yellow',width=15)
                    red.place(x=330, y=270, width=70, height=40)
                    red.bind("<Button-1>", click)

                    self.scvalue_color = StringVar()
                    self.scvalue_color.set("")
                    screen = Entry(self.root3, textvar=self.scvalue_color, font="lucida 20 bold",bg="lightgray", fg="black", show='*').place(x=80, y=350)

                    reset_password = Button(self.root3,command=self.reset_colour_base_password, text="Reset Password", bg="#d77337",fg="white",font=("time new roman", 12, "bold")).place(x=140, y=400, width=150, height=40)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)

    #-----------------------Clear text of colour base password------------------------------
    def clear2_text(self):
        self.screen2.delete(0,END)
        #self.text_email1.delete(0,END)
    #-----------------------Colour base password main login function--------------------------------
    def colour_login(self):
        if self.val_email.get()=="":
            self.engine.say('Please enter your email address')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter your email address", parent=self.window)
        elif self.text_email1.get()!=self.txt_user.get():
             self.engine.say('Please enter your valid email address')
             self.engine.runAndWait()
             messagebox.showerror("Error", "Your email address is not matching with text base email id", parent=self.window)
        elif self.scvalue.get()=="":
            self.engine.say('Please enter colour base password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter colour base password", parent=self.window)

        else:
            try:
                if self.scvalue.get()!=None:
                    color_base_password = self.scvalue.get()
                    self.encrypted_color_password = base64.b85encode(color_base_password.encode(str("utf-8")))
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.val_email.get())
                row=cur.fetchone()
                cur.execute("select * from student where email=%s and ga_password=%s",(self.val_email.get(), self.encrypted_color_password))
                row1 = cur.fetchone()
                if row==None:
                    self.engine.say('Please Enter The Valid Email Address')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter The Valid Email Address", parent=self.window)

                elif row1==None:
                    self.engine.say('Invalid Password!')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Password!", parent=self.window)
                    self.clear2_text()
                else:
                    self.engine.say('congratulation Colour base password Succssfuly login')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Colour base password Succssfuly login", parent=self.window)
                    self.clear2_text()
                    #self.window.destroy()
                    self.next_page()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.window)

    #--------------------colour base password main design-------------------------
    def next(self):
        #import random
        self.window = Toplevel(self.root)
        self.window.title("Second Level of security")
        self.window.geometry('550x600+600+150')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        self.window.focus_force()
        self.window.grab_set()

        my_text4 = Label(self.window, text="Graphical Password", font=("time new roman", 25, "bold"), bg="white",
                         fg="blue").place(x=120, y=20)
        my_text3 = Label(self.window, text="Colour Base 2nd level of security", font=("time new roman", 15, "bold"),
                         bg="white",fg="red").place(x=120, y=80)

        def click(event):
            text = event.widget.cget("text")
            if text == "=":
                pass
            elif text == "C":
                pass
            else:
                self.scvalue.set(self.scvalue.get() + text)
                # screen.update()

        self.val_email = StringVar()
        email = Label(self.window, text="Email",font=("time new roman", 15, "bold"), bg="white", fg="#36454F").place(x=120, y=140)
        self.text_email1 = Entry(self.window, font=("time new roman", 13), bg="lightgray", fg="black", textvariable=self.val_email)
        self.text_email1.place(x=190, y=140, width=200, height=30)

        red = Button(self.window, text="red10", font=("time new roman", 13), border=5, bg="red", fg="red",activebackground='red', activeforeground='red')
        red.place(x=50, y=240, width=150, height=40)
        red.bind("<Button-1>", click)

        red = Button(self.window, text="blue20", font=("time new roman", 13), border=5, bg="blue", fg="blue",activebackground='blue', activeforeground='blue', width=15)
        red.place(x=200, y=200, width=150, height=40)
        red.bind("<Button-1>", click)

        red = Button(self.window, text="green30", font=("time new roman", 13), border=5, bg="green", fg="green", activebackground='green', activeforeground='green',width=15)
        red.place(x=350, y=240, width=150, height=40)
        red.bind("<Button-1>", click)

        # bvalue= IntVar()
        # bvalue.set()
        red = Button(self.window, text="yellow40", font=("time new roman", 13), border=5, bg="yellow", fg="yellow", activebackground='yellow', activeforeground='yellow',width=15)
        red.place(x=200, y=280, width=150, height=40)
        red.bind("<Button-1>", click)

        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen2 = Entry(self.window, textvar=self.scvalue, font="lucida 20 bold", bg="#36454F", fg="white", show='*')
        self.screen2.place(x=120, y=360)

        forget = Button(self.window, command=self.colour_forget_password, cursor="hand2", text="Forget Password?", bg="white",
                        fg="#d77337", bd=0,font=("time new roman", 12)).place(x=200, y=410)
        Submit = Button(self.window, command=self.colour_login,text="SAVE", font=("time new roman", 13, "bold"), border=5, bg="#006400",fg="white").place(x=200, y=500, width=150, height=40)


# ********************************Third level of image base Security Page*************************************

    #-------------------------Image base reset password---------------------------
    def clear4_text(self):
        self.text_image_answer.delete(0,END)
        self.screen3.delete(0,END)
    def reset_image_base_password(self):
        if self.cmb3_image_question.get()=='' or self.val3_image_answer.get()=='':
            self.engine.say('All field are required')
            self.engine.runAndWait()
            messagebox.showerror("Error", "All field are required",parent=self.root4)
        elif self.image_screen.get()=='':
            self.engine.say('Please Enter password to reset')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please Enter password to reset", parent=self.root4)
        else:
            try:
                if self.image_screen.get()!=None:
                    reset_image_base_password = self.image_screen.get()
                    self.reset_encrypted_image_password = base64.b85encode(reset_image_base_password.encode(str("utf-8")))
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and question=%s and answer=%s",
                            (self.val3_email.get(), self.cmb3_image_question.get(), self.val3_image_answer.get()))
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter the correct Security question and answer')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter the correct Security question and answer",parent=self.root4)
                else:
                    cur.execute("update student set gb_password=%s where email=%s",(self.reset_encrypted_image_password, self.val3_email.get()))
                    con.commit()
                    con.close()
                    self.engine.say('Your password has been reset, Please login with new password')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Your password has been reset, Please login with new password!",parent=self.root4)
                    self.clear4_text()
                    self.root4.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root4)
    #------------------------image base Forget password----------------------------
    def image_forget_password(self):
        if self.val3_email.get() == "":
            self.engine.say('Please Enter email address to reset your password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please Enter email address to reset your password", parent=self.window1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.val3_email.get())
                row = cur.fetchone()
                if row == None:
                    self.engine.say('Please Enter The Valid Email Address')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter The Valid Email Address", parent=self.window1)
                else:
                    con.close()
                    self.root4 = Toplevel()
                    self.root4.title("Forget Password")
                    self.root4.geometry("450x505+650+200")
                    self.root4.config(bg="white")
                    self.root4.resizable(False, False)
                    self.root4.focus_force()
                    self.root4.grab_set()

                    title = Label(self.root4, text="Forget Password", font=("time new roman", 15, "bold"), fg="red",bg="white").place(x=7, y=10, relwidth=1)
                    Security_Questions = Label(self.root4, text="Security Question",font=("time new roman", 15), bg="white", fg="gray").place(x=105, y=60)

                    # -----------------Answer-------------
                    self.val3_image_answer = StringVar()
                    answer = Label(self.root4, text="Answer", font=("time new roman", 15), bg="white", fg="gray").place(x=105, y=120)
                    self.text_image_answer = Entry(self.root4, font=("time new roman", 13), bg="lightgray", fg="black",textvariable=self.val3_image_answer)
                    self.text_image_answer.place(x=110, y=150, width=200, height=30)

                    self.cmb3_image_question = StringVar()
                    self.cmb_image_question = ttk.Combobox(self.root4, textvariable=self.cmb3_image_question, font=("time new roman", 13),state='readonly')
                    self.cmb_image_question['values'] = ("Select", "Your first school name", "your birth place", "your best friend name")
                    self.cmb_image_question.place(x=110, y=90, width=200)
                    self.cmb_image_question.current(0)

                    new_password = Label(self.root4, text="Enter New Image base Password", font=("time new roman", 15), bg="white",fg="gray").place(x=70, y=180)
                    reset_password = Button(self.root4, command=self.reset_image_base_password, text="Reset Password",
                                    bg="#d77337", fg="white", font=("time new roman", 12, "bold")).place(x=140, y=450,width=150,height=40)

                    self.bg102 = Image.open("image11111.jpg")
                    self.resizeA = self.bg102.resize((70, 70), Image.ANTIALIAS)
                    self.photo102 = ImageTk.PhotoImage(self.resizeA)

                    self.bg22 = Image.open("image22222.jpg")
                    self.resizeB = self.bg22.resize((70, 70), Image.ANTIALIAS)
                    self.photo22 = ImageTk.PhotoImage(self.resizeB)

                    self.bg33 = Image.open("image33333.jpg")
                    self.resizeC = self.bg33.resize((70, 70), Image.ANTIALIAS)
                    self.photo33 = ImageTk.PhotoImage(self.resizeC)

                    self.bg44 = Image.open("image44444.jpg")
                    self.resizeD = self.bg44.resize((70, 70), Image.ANTIALIAS)
                    self.photo44 = ImageTk.PhotoImage(self.resizeD)

                    self.bg55 = Image.open("image111.jpg")
                    self.resizeE = self.bg55.resize((70, 70), Image.ANTIALIAS)
                    self.photo55 = ImageTk.PhotoImage(self.resizeE)

                    self.bg66 = Image.open("image222.jpg")
                    self.resizeF = self.bg66.resize((70, 70), Image.ANTIALIAS)
                    self.photo66 = ImageTk.PhotoImage(self.resizeF)

                    self.bg77 = Image.open("image333.jpg")
                    self.resizeG = self.bg77.resize((70, 70), Image.ANTIALIAS)
                    self.photo77 = ImageTk.PhotoImage(self.resizeG)

                    self.bg88 = Image.open("image444.jpg")
                    self.resizeH = self.bg88.resize((70, 70), Image.ANTIALIAS)
                    self.photo88 = ImageTk.PhotoImage(self.resizeH)

                    self.bg99 = Image.open("image1111.jpg")
                    self.resizeI = self.bg99.resize((70, 70), Image.ANTIALIAS)
                    self.photo99 = ImageTk.PhotoImage(self.resizeI)

                    self.bg101 = Image.open("image2222.jpg")
                    self.resizeJ = self.bg101.resize((70, 70), Image.ANTIALIAS)
                    self.photo101 = ImageTk.PhotoImage(self.resizeJ)

                    self.bg111 = Image.open("image3333.jpg")
                    self.resizeK = self.bg111.resize((70, 70), Image.ANTIALIAS)
                    self.photo111 = ImageTk.PhotoImage(self.resizeK)

                    self.bg122 = Image.open("image4444.jpg")
                    self.resizeL = self.bg122.resize((70, 70), Image.ANTIALIAS)
                    self.photo122 = ImageTk.PhotoImage(self.resizeL)

                    self.image_screen = StringVar()
                    self.screen3 = Entry(self.root4, textvariable=self.image_screen, font="lucida 20 bold", bg="white",fg="white", bd=0, show='*')
                    self.screen3.place(x=150, y=225, width=150, height=30)

                    def onclick2(event):
                        text = event.widget.cget("text")
                        if text == "=":
                            pass
                        elif text == "C":
                            pass
                        else:
                            self.image_screen.set(self.image_screen.get() + text)

                    Next = Button(self.root4, image=self.photo102, font=("time new roman", 13, "bold"), text='1',border=2)
                    Next.place(x=100, y=220, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo22, font=("time new roman", 13, "bold"), text='2',border=2)
                    Next.place(x=160, y=220, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo33, font=("time new roman", 13, "bold"), text='3',border=2)
                    Next.place(x=220, y=220, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo44, font=("time new roman", 13, "bold"), text='4',border=2)
                    Next.place(x=280, y=220, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo55, font=("time new roman", 13, "bold"), text='9',border=2)
                    Next.place(x=100, y=270, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo66, font=("time new roman", 13, "bold"), text='10',border=2)
                    Next.place(x=160, y=270, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo77, font=("time new roman", 13, "bold"), text='11',border=2)
                    Next.place(x=220, y=270, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo88, font=("time new roman", 13, "bold"), text='12',border=2)
                    Next.place(x=280, y=270, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo99, font=("time new roman", 13, "bold"), text='5',border=2)
                    Next.place(x=100, y=320, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo101, font=("time new roman", 13, "bold"), text='6',border=2)
                    Next.place(x=160, y=320, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo111, font=("time new roman", 13, "bold"), text='7',border=2)
                    Next.place(x=220, y=320, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)

                    Next = Button(self.root4, image=self.photo122, font=("time new roman", 13, "bold"), text='8',border=2)
                    Next.place(x=280, y=320, width=70, height=70)
                    Next.bind("<Button-1>", onclick2)


            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root4)

    #_____________________Clear text of Image_Base password--------------------------
    def clear3_text(self):
        self.text_email.delete(0,END)
        self.screen1.delete(0,END)
    #---------------------Main login function of Image_password-------------------------
    def image_login(self):
        if self.val3_email.get()=="":
            self.engine.say('Please enter your email address')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter your email address", parent=self.window1)
        elif self.text_email.get()!= self.text_email1.get():
            messagebox.showerror("Error", "Please enter your same email address", parent=self.window1)
        elif self.screen.get()=="":
            self.engine.say('Please enter Image base password')
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter Image base password", parent=self.window1)
        else:
            try:
                if self.screen.get()!=None:
                    image_base_password = self.screen.get()
                    self.encrypted_image_password = base64.b85encode(image_base_password.encode(str("utf-8")))
                con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.val3_email.get())
                row=cur.fetchone()
                cur.execute("select * from student where email=%s and gb_password=%s",(self.val3_email.get(), self.encrypted_image_password))
                row3 = cur.fetchone()
                if row==None:
                    self.engine.say('Please Enter The Valid Email Address')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please Enter The Valid Email Address", parent=self.window1)
                elif row3==None:
                    self.engine.say('Invalid Password!')
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Password!", parent=self.window1)
                    self.clear3_text()
                else:
                    self.engine.say('Congratulation Succssfuly login')
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Image base password Succssfuly login", parent=self.window1)
                    self.clear3_text()
                    self.window1.destroy()
                    self.window.destroy()
                    self.student_details()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.window1)

    # ----------------------------------Image Base Password Main Design-------------------------------------
    def next_page(self):
        from PIL import Image, ImageTk
        #window1 = Tk()
        self.window1 = Toplevel(self.root)
        self.window1.title("Third Level of security")
        self.window1.geometry('550x600+600+150')
        self.window1.config(bg='white')
        self.window1.resizable(False, False)
        self.window1.focus_force()
        self.window1.grab_set()
        my_text4 = Label(self.window1, text="Graphical Password", font=("time new roman", 25, "bold"), bg="white",
                         fg="#B422E6").place(x=100, y=20)
        my_text3 = Label(self.window1, text="Image Base 3rd level of security", font=("time new roman", 15, "bold"), bg="white",
                         fg="red").place(x=120, y=80)

        self.val3_email = StringVar()
        email = Label(self.window1, text="User Name",font=("time new roman", 15,"bold"), bg="white", fg="#36454F").place(x=100, y=125)
        self.text_email = Entry(self.window1, font=("time new roman", 13), bg="lightgray", fg="black", textvariable=self.val3_email)
        self.text_email.place(x=220, y=125, width=200, height=30)

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

        self.bg5 = Image.open("image111.jpg")
        self.resizeE = self.bg5.resize((100, 100), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(self.resizeE)

        self.bg6 = Image.open("image222.jpg")
        self.resizeF = self.bg6.resize((100, 100), Image.ANTIALIAS)
        self.photo6 = ImageTk.PhotoImage(self.resizeF)

        self.bg7 = Image.open("image333.jpg")
        self.resizeG = self.bg7.resize((100, 100), Image.ANTIALIAS)
        self.photo7 = ImageTk.PhotoImage(self.resizeG)

        self.bg8 = Image.open("image444.jpg")
        self.resizeH = self.bg8.resize((100, 100), Image.ANTIALIAS)
        self.photo8 = ImageTk.PhotoImage(self.resizeH)

        self.bg9 = Image.open("image1111.jpg")
        self.resizeI = self.bg9.resize((100, 100), Image.ANTIALIAS)
        self.photo9 = ImageTk.PhotoImage(self.resizeI)

        self.bg10 = Image.open("image2222.jpg")
        self.resizeJ = self.bg10.resize((100, 100), Image.ANTIALIAS)
        self.photo10 = ImageTk.PhotoImage(self.resizeJ)

        self.bg11 = Image.open("image3333.jpg")
        self.resizeK = self.bg11.resize((100, 100), Image.ANTIALIAS)
        self.photo11 = ImageTk.PhotoImage(self.resizeK)

        self.bg12 = Image.open("image4444.jpg")
        self.resizeL = self.bg12.resize((100, 100), Image.ANTIALIAS)
        self.photo12 = ImageTk.PhotoImage(self.resizeL)

        self.screen = StringVar()
        self.screen1 = Entry(self.window1, textvariable=self.screen, font="lucida 20 bold", bg="white", fg="white",bd=0, show='*')
        self.screen1.place(x=120, y=200, width=200, height=30)

        def onclick(event):
            text = event.widget.cget("text")
            if text == "=":
                pass
            elif text == "C":
                pass
            else:
                self.screen.set(self.screen.get() + text)

        Next = Button(self.window1, image=self.photo1, font=("time new roman", 13, "bold"), text='1', border=2)
        Next.place(x=70, y=170, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo2, font=("time new roman", 13, "bold"), text='2', border=2)
        Next.place(x=170, y=170, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo3, font=("time new roman", 13, "bold"), text='3', border=2)
        Next.place(x=270, y=170, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo4, font=("time new roman", 13, "bold"), text='4', border=2)
        Next.place(x=370, y=170, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo5, font=("time new roman", 13, "bold"), text='9', border=2)
        Next.place(x=70, y=270, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo6, font=("time new roman", 13, "bold"), text='10', border=2)
        Next.place(x=170, y=270, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo7, font=("time new roman", 13, "bold"), text='11', border=2)
        Next.place(x=270, y=270, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo8, font=("time new roman", 13, "bold"), text='12', border=2)
        Next.place(x=370, y=270, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo9, font=("time new roman", 13, "bold"), text='5', border=2)
        Next.place(x=70, y=370, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo10, font=("time new roman", 13, "bold"), text='6', border=2)
        Next.place(x=170, y=370, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo11, font=("time new roman", 13, "bold"), text='7', border=2)
        Next.place(x=270, y=370, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        Next = Button(self.window1, image=self.photo12, font=("time new roman", 13, "bold"), text='8', border=2)
        Next.place(x=370, y=370, width=100, height=100)
        Next.bind("<Button-1>", onclick)

        forget = Button(self.window1, command=self.image_forget_password, cursor="hand2", text="Forget Password?",bg="white",
                        fg="#d77337", bd=0, font=("time new roman", 12)).place(x=200, y=475)
        Save = Button(self.window1, text="Save", font=("time new roman", 13, "bold"), border=5, bg="#d77337", fg="white",command=self.image_login).place(x=200, y=510, width=150, height=40)

    def student_details(self):
        import time
        self.window5 = Toplevel(self.root)
        self.window5.title("Password Management System")
        self.window5.geometry("1530x800+0+0")
        self.window5.config(bg='white')
        self.window5.resizable(False, False)
        self.window5.focus_force()
        self.window5.grab_set()

        self.bg122 = Image.open("student1.jpg")
        self.resizeL = self.bg122.resize((1490, 400), Image.ANTIALIAS)
        self.photo122 = ImageTk.PhotoImage(self.resizeL)

        self.bg123 = Image.open("student2.jpg")
        self.resizeL = self.bg123.resize((1490, 400), Image.ANTIALIAS)
        self.photo123 = ImageTk.PhotoImage(self.resizeL)

        Frame_slider=Frame(self.window5)
        Frame_slider.place(x=10,y=0,width=1530,height=400)

        self.lbl1=Label(Frame_slider,image=self.photo122,bd=0)
        self.lbl1.place(x=10,y=0)

        self.lbl2 = Label(Frame_slider, image=self.photo123, bd=0)
        self.lbl2.place(x=1490, y=0)
        self.x=1480
        self.slider_func()

        label1 = Label(self.window5, text="Student Information", font=("time new roman", 25, "bold"),bg='blue',fg='red')
        label1.place(x=700,y=400)

        p1= Label(self.window5, text="First Name", font=("time new roman", 13, "bold"))
        p1.grid(row=1, column=0, padx=28,pady=450)

        p2 = Label(self.window5, text="Last Name", font=("time new roman", 13, "bold"))
        p2.grid(row=1, column=1, padx=28, pady=450)

        p3 = Label(self.window5, text="Email", font=("time new roman", 13, "bold"))
        p3.grid(row=1, column=2, padx=28, pady=450)

        p4 = Label(self.window5, text="Phone number", font=("time new roman", 13, "bold"))
        p4.grid(row=1, column=3, padx=28, pady=450)

        p5 = Label(self.window5, text="Text_Base Password", font=("time new roman", 13, "bold"))
        p5.grid(row=1, column=4, padx=28, pady=450)

        p6 = Label(self.window5, text="Question", font=("time new roman", 13, "bold"))
        p6.grid(row=1, column=5, padx=28, pady=450)

        p7 = Label(self.window5, text="Answer", font=("time new roman", 13, "bold"))
        p7.grid(row=1, column=6, padx=28, pady=450)

        p8 = Label(self.window5, text="Colour_base password", font=("time new roman", 13, "bold"))
        p8.grid(row=1, column=7, padx=28, pady=450)

        p9 = Label(self.window5, text="Image_base password", font=("time new roman", 13, "bold"))
        p9.grid(row=1, column=8, padx=28, pady=450)

        con = pymysql.connect(host="localhost", user="root", password="", database="employee3")
        cur = con.cursor()
        cur.execute("select * from student where email=%s",self.txt_user.get())
        row = cur.fetchone()
        print(row)
        F_name = Label(self.window5, text=row[1], font=("time new roman", 13), bg='white',fg='black')
        F_name.place(x=28,y=500)

        L_name = Label(self.window5, text=row[2], font=("time new roman", 13), bg='white', fg='black')
        L_name.place(x=190,y=500)

        Email= Label(self.window5, text=row[3], font=("time new roman", 13), bg='white', fg='black')
        Email.place(x=280, y=500)

        Ph_no = Label(self.window5, text=row[4], font=("time new roman", 13), bg='white', fg='black')
        Ph_no.place(x=450, y=500)

        T_password = Label(self.window5, text=row[5], font=("time new roman", 13), bg='white', fg='black')
        T_password.place(x=600, y=500)

        Question = Label(self.window5, text=row[6], font=("time new roman", 13), bg='white', fg='black')
        Question.place(x=790, y=500)

        Ans = Label(self.window5, text=row[7], font=("time new roman", 13), bg='white', fg='black')
        Ans.place(x=990, y=500)

        C_password= Label(self.window5, text=row[8], font=("time new roman", 13), bg='white', fg='black')
        C_password.place(x=1090, y=500)

        I_password= Label(self.window5, text=row[9], font=("time new roman", 13), bg='white', fg='black')
        I_password.place(x=1360, y=500)

        con.commit()
        con.close()
    def slider_func(self):
        self.x-=1
        if self.x==0:
            self.x=1480
            time.sleep(1)
            #---swap-------
            self.new_photo=self.photo122
            self.photo122=self.photo123
            self.photo123=self.new_photo
            self.lbl1.config(image=self.photo122)
            self.lbl2.config(image=self.photo123)

        self.lbl2.place(x=self.x,y=0)
        self.lbl2.after(1,self.slider_func)

root=Tk()
obj=login(root)
root.mainloop()
