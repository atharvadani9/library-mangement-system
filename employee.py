from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from BorrowBook import *
from ReturnBook import *
from ViewReport import *
# Add your own database name and password here to reflect in the code
mypass = "Tusharsai@1"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def employee(studentid):
    
    root = Tk()
    root.title("Library")
    root.minsize(width=800,height=600)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.4

    # Adding a background image
    background_image =Image.open("EmployeeView.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(400,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    #head frame
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.08,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Employee Page", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=ViewB)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="View Report",bg='black', fg='white', command = Report)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    # Book Report(Student Id:)
    #labelFrame = Frame(root,bg='black')
    #labelFrame.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    #lb4 = Label(labelFrame,text="Student Id : ", bg='black', fg='white')
    #lb4.place(relx=0.05,rely=0.5,relheight=0.08)
        
    #bookInfo10 = Entry(labelFrame)
    #bookInfo10.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    #bid = bookInfo10.get()
    
        


    root.mainloop()
