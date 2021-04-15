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
issueTable = "borrow" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    copies_new = bookInfo9.get()
    remarks_new = bookInfo8.get()
    
    deleteSql = "delete from {table} where bid = '{bid}'".format(table = bookTable , bid = bid)
    deleteIssue = "delete from {table} where bid = '{bid}'".format(table = issueTable , bid = bid)
    
    updateRemarks = "UPDATE {table} SET remarks = '{remarks_2}' WHERE bid = '{bid}'".format(table = bookTable ,remarks_2 = remarks_new ,bid = bid)
    updateCopies = "UPDATE {table} SET copies= '{copies_2}' WHERE bid = '{bid}'".format(table = bookTable , copies_2 = copies_new , bid = bid)
    try:
        if(copies_new!="" and remarks_new == ""):
            cur.execute(updateCopies)
            con.commit()  
        if((copies_new =="") and (remarks_new=="") ):
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit() 
        if(remarks_new!="" and copies_new == ""):
            cur.execute(updateRemarks)
            con.commit()
        messagebox.showinfo('Success',"Book Record Updated Successfully")
    except: 
        messagebox.showinfo("Please check Book ID")
    

    print(bid)
    print(remarks_new)
    print(copies_new)
    if((copies_new!="") and (remarks_new!="") ):
        bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,bookInfo7,bookInfo8,bookInfo9,bookInfo10,Canvas1,con,cur,bookTable,root
    
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
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.3, relwidth=0.62)

    # Copies to delete 
    lb3 = Label(labelFrame,text="Copies : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4)
        
    bookInfo9 = Entry(labelFrame)
    bookInfo9.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Remarks to update
    lb4 = Label(labelFrame,text="Remarks : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5)
        
    bookInfo8 = Entry(labelFrame)
    bookInfo8.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()