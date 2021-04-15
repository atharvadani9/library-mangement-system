from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def employeeRegister():
    
    eid = employeeInfo1.get()
    name = employeeInfo2.get()
    gender = employeeInfo3.get()
    age = employeeInfo4.get()
    contact = employeeInfo5.get()
    email = employeeInfo6.get()

    email = email.lower()
    
    insertemployees = "insert into "+employeeTable+" values('"+eid+"','"+name+"','"+gender+"','"+age+"','"+contact+"','"+email+"')"
    try:
        cur.execute(insertemployees)
        con.commit()
        messagebox.showinfo('Success',"Employee added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(eid)
    print(name)
    print(gender)
    print(age)
    print(contact)
    print(email)


    root.destroy()
    
def addEmployee(): 
    global employeeInfo1,employeeInfo2,employeeInfo3,employeeInfo4,employeeInfo5,employeeInfo6,Canvas1,con,cur,employeeTable,root
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
    employeeTable = "employees" # employee Table


    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Employee", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.55)
        
    # Employee ID
    lb1 = Label(labelFrame,text="Employee ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.125, relheight=0.08)
        
    employeeInfo1 = Entry(labelFrame)
    employeeInfo1.place(relx=0.3,rely=0.125, relwidth=0.62, relheight=0.08)
        
    # name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    employeeInfo2 = Entry(labelFrame)
    employeeInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # employee gender
    lb3 = Label(labelFrame,text="Gender : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.375, relheight=0.08)
        
    employeeInfo3 = Entry(labelFrame)
    employeeInfo3.place(relx=0.3,rely=0.375, relwidth=0.62, relheight=0.08)
        
    # employee age
    lb4 = Label(labelFrame,text="Age : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    employeeInfo4 = Entry(labelFrame)
    employeeInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # employee contact
    lb5 = Label(labelFrame,text="Contact : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.625, relheight=0.08)
        
    employeeInfo5 = Entry(labelFrame)
    employeeInfo5.place(relx=0.3,rely=0.625, relwidth=0.62, relheight=0.08)

    # employee email
    lb6 = Label(labelFrame,text="Email : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.75, relheight=0.08)
        
    employeeInfo6 = Entry(labelFrame)
    employeeInfo6.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.08)
      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=employeeRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop() 