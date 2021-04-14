import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
#from AddBook import *
#from DeleteBook import *
from ViewBooks import *
from BorrowBook import *
from ReturnBook import *
from ViewReport import *
from MoneyDue import *
# Add your own database name and password here to reflect in the code
mypass = "Tusharsai@1"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def student(studentid):

    sid = studentid
    studentTable = "students"
    checkthename = 'abcdegfhis'
    checkName = "select Name from {table} where sid='{sid}'".format(table=studentTable, sid=sid)
    cur.execute(checkName)
    for i in cur:
        checkthename = i[0]

    root = Tk()
    root.title("Student Page")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    # Take n greater than 0.25 and less than 5
    same=True
    n=0.33

    # Adding a background image
    background_image =Image.open("student.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome "+checkthename+"!", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
    #btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    #btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    #btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=ViewB)
    btn3.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Borrow Book",bg='black', fg='white', command = lambda: borrowBook(studentid))
    btn4.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = lambda: returnBook(studentid))
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    btn6 = Button(root, text="View Report", bg='black', fg='white', command = lambda: Report(studentid))
    btn6.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
    btn7 = Button(root, text="Pay dues", bg='black', fg='white', command = lambda: issueBook(studentid))
    btn7.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


    root.mainloop()
student('S20190046')



