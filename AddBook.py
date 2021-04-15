from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    copies = bookInfo4.get()
    remarks = bookInfo6.get()
    publisher = bookInfo7.get()

    remarks = remarks.lower()
    books = "books"
    
    insertBooks = "insert into {table} values('{bid}','{title}','{author}',{copies},'{remarks}','{publisher}')".format(table = books , bid = bid , title = title ,author = author , copies = copies , remarks = remarks , publisher = publisher)
    print(bid)
    print(title)
    print(author)
    print(remarks)
    print(publisher)
    print(copies)
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
   


    root.destroy()
    
def addBook(): 
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,bookInfo7,bookInfo8,bookInfo9,bookInfo10,Canvas1,con,cur,bookTable,root
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
    books = "books" # Book Table


    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.55)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.125, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.125, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.375, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.375, relwidth=0.62, relheight=0.08)
        
    # Book Remarks
    lb4 = Label(labelFrame,text="Remarks : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)


    # Book Publisher
    lb6 = Label(labelFrame,text="Publisher : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.625, relheight=0.08)
        
    bookInfo7 = Entry(labelFrame)
    bookInfo7.place(relx=0.3,rely=0.625, relwidth=0.62, relheight=0.08)

    # Book Copies
    lb7 = Label(labelFrame,text="Copies : ", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.75, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.875, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.875, relwidth=0.18,relheight=0.08)
    
    root.mainloop() 