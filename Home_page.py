from tkinter import *
from PIL import Image,ImageTk
import webbrowser
class home_page:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.maxsize(0,0)
        #root.minsize(1500,900)ww
        self.root.title("Graphical Password Interface")
        self.root.bg=Image.open("bg.jpg")
        self.root.resizeA=root.bg.resize((1550,800), Image.ANTIALIAS)
        self.root.photo= ImageTk.PhotoImage(self.root.resizeA)
        root.bg_image=Label(root,image=self.root.photo).place(x=0,y=0)
        self.root.wm_attributes("-transparentcolor", 'red')
        my_text1= Label(root,text="Welcome!", font=("time new roman", 30,"bold"),fg="blue").place(x=650,y=50)
        my_text2= Label(root,text="Graphical Password Authentication System", font=("time new roman", 25,"bold"),bg="white",fg="#E67E22").place(x=390,y=150)

        Reg = Button(self.root, text="Registration",cursor="hand2", font=("time new roman", 13), border=5, bg="blue", fg="white",
                     command=self.reg).place(x=200, y=450, width=180, height=40)
        Sign_in = Button(self.root, text="Sign In", cursor="hand2",font=("time new roman", 13), border=5, bg="blue", fg="white",
                         command=self.signup).place(x=700, y=450, width=180, height=40)
        sign_in = Button(self.root, text="About",cursor="hand2", font=("time new roman", 13), border=5, bg="blue", fg="white",
                         command=self.about).place(x=1200, y=450, width=150, height=40)

    def reg(self):
        self.root.destroy()
        import registration_page


    def signup(self):
        self.root.destroy()
        import login_page

    def about(self):
        self.window4=Toplevel()
        self.window4.title("About Developer")
        self.window4.geometry('1530x800+0+0')
        self.window4.config(bg='white')
        self.window4.resizable(False, False)
        self.window4.bg = Image.open("photo4.jpg")
        self.window4.resizeA = self.window4.bg.resize((1530, 800), Image.ANTIALIAS)
        self.window4.photo = ImageTk.PhotoImage(self.window4.resizeA)

        self.window4.bg2 = Image.open("Pathik Nandi.jpg")
        self.window4.resizeB = self.window4.bg2.resize((150, 180), Image.ANTIALIAS)
        self.window4.photo1 = ImageTk.PhotoImage(self.window4.resizeB)

        cannvas= Canvas(self.window4)
        cannvas.create_image(0,0, image=self.window4.photo, anchor=NW)
        cannvas.create_image(1400,500, image=self.window4.photo1)
        cannvas.create_text(950,400, text="Hey, I'm Pathik Nandi", fill='red',font=("time new roman", 30,"bold"))
        cannvas.create_text(990, 480, text="Welcome to my profile! I'm a background of \nInformation And Cyber security"
                                           " & Python \nDeveloper.I had great experience with Graphical\n Passowrd Authentication"
                                           " System. you can follow me \n by following social media. ", fill='white', font=("time new roman", 15))
        cannvas.pack(fill="both", expand=True)

        def facebook():
            webbrowser.open("https://www.facebook.com/pathik.nandi.37")
        def linkedin():
            webbrowser.open("https://www.linkedin.com/in/pathik-nandi-15041999/")

        self.bg10 = Image.open("facebook.jpg")
        self.resizeJ = self.bg10.resize((40, 40), Image.ANTIALIAS)
        self.photo10 = ImageTk.PhotoImage(self.resizeJ)

        self.bg11 = Image.open("instagram.jpg")
        self.resizeK = self.bg11.resize((40, 40), Image.ANTIALIAS)
        self.photo11 = ImageTk.PhotoImage(self.resizeK)

        self.bg12 = Image.open("linkedin1.jpg")
        self.resizeL = self.bg12.resize((40, 40), Image.ANTIALIAS)
        self.photo12 = ImageTk.PhotoImage(self.resizeL)
        Next = Button(self.window4, image=self.photo10, font=("time new roman", 13, "bold"), border=2,command=facebook).place(x=850, y=550,width=40,height=40)
        Next = Button(self.window4, image=self.photo11, font=("time new roman", 13, "bold"), border=2,command='').place(x=950,y=550,width=40,height=40)
        Next = Button(self.window4, image=self.photo12, font=("time new roman", 13, "bold"), border=2,command=linkedin).place(x=1050,y=550,width=40,height=40)

root=Tk()
obj=home_page(root)
root.mainloop()