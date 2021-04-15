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
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

def paymentmethod(studentid):
    
    global payBtn,labelFrame,lb1,inf1,quitBtn,root,Canvas1,status
    
    amt = inf1.get()
    sid = studentid
    payBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()

    getMoney = "select moneydue from students where SID='{sid}'".format(sid = sid)
    try:
        cur.execute(getMoney)
        con.commit()
        for i in cur:
            amtdue = int(i[0])
    except:
        messagebox.showinfo("Failed to fetch files from database")

    balance = amtdue-int(amt)

    if balance==0:
        updateMoney = "update students moneydue set moneydue=0 where SID='{sid}'".format(sid = sid)
        try:
            cur.execute(updateMoney)
            con.commit()
            messagebox.showinfo("Successful", "Your dues have been paid")
        except:
            messagebox.showinfo("Unsuccessful", "Your dues have not been paid")
    else:
        messagebox.showinfo("Failed", "Incorrect Amount entered")
    root.destroy()    

    
    
def issueBook(studentid): 
    
    global payBtn,labelFrame,lb1,inf1,quitBtn,root,Canvas1,status
    sid = studentid
    root = Toplevel()
    root.title("Payment Tab")
    root.minsize(width=1000,height=500)
    root.geometry("600x500")
    
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
        
    headingLabel = Label(headingFrame1, text="Money Due", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Enter Amount : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    Label(labelFrame, text="Money To be Paid" ,bg='black',fg='white', font='Courier').place(relx=0.4,rely=0.5)
    y=0.6
    getBooks = "select moneydue from students where SID='{sid}'".format(sid = sid)
    #getBooks = "select moneydue from students where sid=101"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:

            Label(labelFrame, text='Rs. '+str(i[0]), bg='black',fg='white', font='Courier').place(relx=0.47,rely=y)
            #Label(labelFrame, text="%-20s%-45s%-20s%-20s%-30s%-50s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")


    
    # # Issued To Student name 
    # lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    # lb2.place(relx=0.05,rely=0.4)
        
    # inf2 = Entry(labelFrame)
    # inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    payBtn = Button(root,text="Pay",bg='#d1ccc0', fg='black',command=lambda: paymentmethod(sid))
    payBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

