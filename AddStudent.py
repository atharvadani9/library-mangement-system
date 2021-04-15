from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def studentRegister():
    
    sid = studentInfo1.get()
    name = studentInfo2.get()
    gender = studentInfo3.get()
    age = studentInfo4.get()
    contact = studentInfo5.get()
    email = studentInfo6.get()
    moneyDue = studentInfo7.get()

    email = email.lower()
    
    insertstudents = "insert into "+studentTable+" values('"+sid+"','"+name+"','"+gender+"','"+age+"','"+contact+"','"+email+"','"+moneyDue+"')"
    try:
        cur.execute(insertstudents)
        con.commit()
        messagebox.showinfo('Success',"Student added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(sid)
    print(name)
    print(gender)
    print(age)
    print(contact)
    print(email)


    root.destroy()
    
def addstudent(): 
    global studentInfo1,studentInfo2,studentInfo3,studentInfo4,studentInfo5,studentInfo6,studentInfo7,Canvas1,con,cur,studentTable,root
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    # Take n greater than 0.25 and less than 5
    same=True
    n=0.4

    background_image =Image.open("Wood.jpg")
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
    
    
    
    

    # Add your own database name and password here to reflect in the code
    mypass = "Tusharsai@1"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    studentTable = "students" # student Table


    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add student", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.55)
        
    # student ID
    lb1 = Label(labelFrame,text="Student ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.125, relheight=0.08)
        
    studentInfo1 = Entry(labelFrame)
    studentInfo1.place(relx=0.3,rely=0.125, relwidth=0.62, relheight=0.08)
        
    # name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    studentInfo2 = Entry(labelFrame)
    studentInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # student gender
    lb3 = Label(labelFrame,text="Gender : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.375, relheight=0.08)
        
    studentInfo3 = Entry(labelFrame)
    studentInfo3.place(relx=0.3,rely=0.375, relwidth=0.62, relheight=0.08)
        
    # student age
    lb4 = Label(labelFrame,text="Age : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    studentInfo4 = Entry(labelFrame)
    studentInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # student contact
    lb5 = Label(labelFrame,text="Contact : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.625, relheight=0.08)
        
    studentInfo5 = Entry(labelFrame)
    studentInfo5.place(relx=0.3,rely=0.625, relwidth=0.62, relheight=0.08)

    # student email
    lb6 = Label(labelFrame,text="Email : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.75, relheight=0.08)
        
    studentInfo6 = Entry(labelFrame)
    studentInfo6.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.08)

    # student money due
    lb6 = Label(labelFrame,text="Money Due : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.875, relheight=0.08)
        
    studentInfo7 = Entry(labelFrame)
    studentInfo7.place(relx=0.3,rely=0.875, relwidth=0.62, relheight=0.08)
      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=studentRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop() 