from tkinter import  *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
#from student import *
from employee import *
class Login:
	global s
	def __init__(self,root):

		self.root = root 
		self.root.title("Login")
		self.root.geometry("1199x600+100+50")
		self.root.resizable(False,False)
		self.bg = ImageTk.PhotoImage(file="login.jpg")
		self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
		Frame_login = Frame(self.root,bg="black")
		Frame_login.place(x=314,y=109,height=383,width=571)
		title=Label(Frame_login,text = "Login" , font = ("Gaudy old style",35,"bold") , fg = "white" , bg = "black").place(x= 225,y=10)
		title=Label(Frame_login,text = "Username :" , font = ("Gaudy old style",20) , fg = "white" , bg = "black").place(x= 90,y=120)
		self.txt_user = Entry(Frame_login,font=("times new roman",15),bg = "lightgray")
		self.txt_user.place(x= 235,y=126,width = 130 , height = 30)
		title=Label(Frame_login,text = "Password :" , font = ("Gaudy old style",20) , fg = "white" , bg = "black").place(x= 90,y=202)
		self.txt_pass = Entry(Frame_login,font=("times new roman",15),bg = "lightgray",show = "*")
		self.txt_pass.place(x= 235,y=206,width = 130 , height = 30)

		Login_btn=Button(Frame_login,text = "Login" ,command = self.logged, fg = "white" , bg = "black" ,bd = 0 , font = ("times new roman" , 20)).place(x = 250 , y = 300 )
		

	def logged(self):
		if self.txt_pass.get() == "" or self.txt_user.get() == "":
			messagebox.showerror("Error" , "All fields need to be filled" , parent = self.root)
		else:
			try:
				conn = pymysql.connect(host = "localhost" , user = "root" , password = "mysqldatabase" , database = "db")
				cur = conn.cursor()
				cur.execute("select * from Login where username = %s and password = %s",(self.txt_user.get(),self.txt_pass.get()))
				row = cur.fetchone()
				if row==None:
					messagebox.showerror("Error" , "Invalid Username and Password" , parent = self.root)
					self.root.destroy()
				else:
					s = self.txt_user.get()
					if s[0] == "S":
						self.root.destroy() 
						#student(s)
					elif s[0] == "E":
						self.root.destroy()
						employee(s)
					elif s[0] == "A":
						self.root.destroy()
						import admin
					messagebox.showinfo("Success" , "Welcome" ,parent = self.root)
				conn.close()	

			except Exception as es:
				messagebox.showerror("Error" , f"Error Due to {str(es)}" , parent = self.root)	
   
    

root=Tk()
obj = Login(root)
root.mainloop()