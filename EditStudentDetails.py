from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Tusharsai@1"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here 
studentTable = "students" #student Table


def editstudent():
    print (1)
    sid = studentInfo1.get()
    name_new = studentInfo8.get()
    gender_new = studentInfo9.get()
    age_new = studentInfo10.get()
    contact_new = studentInfo11.get()
    email_new = studentInfo12.get()
    moneyDue_new = studentInfo13.get()
    
    deleteSql = "delete from "+studentTable+" where sid = '"+sid+"'"
    
    
    updateName = "UPDATE students SET name = '"+name_new+"' WHERE sid = '"+sid+"'"
    updateGender = "UPDATE students SET gender= '"+gender_new+"'WHERE sid = '"+sid+"'"
    updateAge = "UPDATE students SET age = '"+age_new+"' WHERE sid = '"+sid+"'"
    updateContact = "UPDATE students SET contact= '"+contact_new+"'WHERE sid = '"+sid+"'"
    updateEmail = "UPDATE students SET email = '"+email_new+"' WHERE sid = '"+sid+"'"
    updateMoneyDue = "UPDATE students SET moneydue = '"+moneyDue_new+"' WHERE sid = '"+sid+"'"
    try:
        if(name_new!=""):
            cur.execute(updateName)
            con.commit()  
        if((name_new == "") and (gender_new =="") and (age_new =="") and (contact_new =="") and (email_new =="") and (moneyDue_new =="")):
            cur.execute(deleteSql)
            con.commit()
        if(gender_new!=""):
            cur.execute(updateGender)
            con.commit()
        if(age_new!=""):
            cur.execute(updateAge)
            con.commit()
        if(contact_new!=""):
            cur.execute(updateContact)
            con.commit()
        if(email_new!=""):
            cur.execute(updateEmail)
            con.commit()
        if(moneyDue_new!=""):
            cur.execute(updateMoneyDue)
            con.commit()

        messagebox.showinfo('Success',"student Record Updated Successfully")
    except:
        messagebox.showinfo("Please check student ID")
    

    print(sid)
    
    if((name_new == "") and (gender_new =="") and (age_new =="") and (contact_new =="") and (email_new =="") and (moneyDue_new =="")):
        studentInfo1.delete(0, END)
    root.destroy()
    
def deleteS(): 
    
    global studentInfo1,studentInfo2,studentInfo3,studentInfo4,studentInfo5,studentInfo6,studentInfo7,studentInfo8,studentInfo9,studentInfo10,studentInfo11,studentInfo12,studentInfo13,Canvas1,con,cur,studentTable,root
    
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    
    Canvas1 = Canvas(root)
    
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
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Edit student Detail", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.55)   
        
    # student ID
    lb1 = Label(labelFrame,text="student ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.125, relheight=0.08)
        
    studentInfo1 = Entry(labelFrame)
    studentInfo1.place(relx=0.3,rely=0.125, relwidth=0.62, relheight=0.08)
        
    # e_name
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    studentInfo8 = Entry(labelFrame)
    studentInfo8.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # student gender
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.375, relheight=0.08)
        
    studentInfo9 = Entry(labelFrame)
    studentInfo9.place(relx=0.3,rely=0.375, relwidth=0.62, relheight=0.08)
        
    # student age
    lb4 = Label(labelFrame,text="Remarks : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    studentInfo10 = Entry(labelFrame)
    studentInfo10.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # student contact
    lb5 = Label(labelFrame,text="Source : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.625, relheight=0.08)
        
    studentInfo11 = Entry(labelFrame)
    studentInfo11.place(relx=0.3,rely=0.625, relwidth=0.62, relheight=0.08)

    # student email
    lb6 = Label(labelFrame,text="Publisher : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.75, relheight=0.08)
        
    studentInfo12 = Entry(labelFrame)
    studentInfo12.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.08)

    # student money due
    lb6 = Label(labelFrame,text="Money Due : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.875, relheight=0.08)
        
    studentInfo13 = Entry(labelFrame)
    studentInfo13.place(relx=0.3,rely=0.875, relwidth=0.62, relheight=0.08)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=editstudent)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()