import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from ViewReport import *
from ViewBooks import *
from ViewStudents import *
from ViewEmployee import *
from AddEmployee import *
from AddStudent import *
from EditEmplyeeDetails import *
from EditStudentDetails import *
mypass = "Tusharsai@1"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Admin Page")
root.minsize(width=400, height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same = True
n = 0.4

# Adding a background image
background_image = Image.open("Adminpageresized.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(800, 840, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth,
                   height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome Admin" ,bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="View Student Details", bg='black', fg='white', command=ViewS)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.075)

btn2 = Button(root, text="View Employee Details", bg='black', fg='white', command=ViewE)
btn2.place(relx=0.28, rely=0.375, relwidth=0.45, relheight=0.075)

btn3 = Button(root, text="View Book Details",bg='black', fg='white', command=ViewB)
btn3.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.075)

btn4 = Button(root, text="View Reports", bg='black', fg='white' , command = Report)
btn4.place(relx=0.28, rely=0.525, relwidth=0.45, relheight=0.075)

btn5 = Button(root, text="Add Students", bg='black', fg='white', command=addstudent)
btn5.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.075)

btn6 = Button(root, text="Update/Delete Student Details", bg='black', fg='white', command=deleteS)
btn6.place(relx=0.28, rely=0.675, relwidth=0.45, relheight=0.075)

btn7 = Button(root, text="Add Employees",bg='black', fg='white', command=addEmployee)
btn7.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.075)

btn8 = Button(root, text="Update/Delete Employee Details", bg='black', fg='white' , command = deleteE)
btn8.place(relx=0.28, rely=0.825, relwidth=0.45, relheight=0.075)

root.mainloop()
