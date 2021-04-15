import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "mysqldatabase"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "students" 
    
def ViewS(): 
    
    root = Toplevel()
    root.title("Students")
    root.minsize(width=1500,height=500)
    root.geometry("600x500")


    # Canvas1 = Canvas(root) 
    # Canvas1.config(bg="#12a4d9")
    # Canvas1.pack(expand=True,fill=BOTH)
    same=True
    n=0.4

    background_image =Image.open("StudentView.jpg")
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
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Student List", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.05,rely=0.3,relwidth=0.85,relheight=0.5)
    y = 0.25
    
    #create table students( SID varchar(20) primary key , Name varchar(30) , Gender varchar(10) , age int , contact bigint , email varchar(60) , moneydue int);
    Label(labelFrame, text="%-18s%-25s%-15s%-10s%-25s%-20s%-10s"%('SID','Name','Gender','Age','Contact','Email','MoneyDue'),bg='black',fg='white', font='Courier').place(relx=0.03,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.02,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:

            temp1 = str(i[0])
            a1 = len(temp1)
            b1 = 13-a1
            temp2 = str(i[1])
            a2 = len(temp2)
            b2 = 30-a2
            temp3 = str(i[2])
            a3 = len(temp3)
            b3 = 15-a3
            temp4 = str(i[3])
            a4 = len(temp4)
            b4 = 10-a4
            temp5 = str(i[4])
            a5 = len(temp5)
            b5 = 15-a5
            temp6 = str(i[5])
            a6 = len(temp6)
            b6=35-a6
            temp7 =str(i[6])

            Label(labelFrame, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+' '*b5+temp6+' '*b6+temp7,bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
            #Label(labelFrame, text="%-20s%-45s%-20s%-20s%-30s%-50s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()