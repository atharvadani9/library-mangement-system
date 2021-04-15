from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import date
from datetime import timedelta
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Tusharsai@1"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
borrowTable = "borrow" #Borrow Table
bookTable = "books" #Book Table
returnTable = "returnbook" #returnbook table
studentTable = "students" 

allBid = [] #List To store all Book IDs

def returnn(studentid):
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()
    sid = studentid  # need to change this
    fine = 1

    extractBid = "select bid from {table} where sid ='{sid}'".format(table=borrowTable,sid = sid)
    try:
        cur.execute(extractBid)
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            status = True

        else:
            status = False
            allBid.clear()
            messagebox.showinfo("Error", "Book ID not present")
            root.destroy()
            return
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")
    
    checkIssueDate = "select IssueDate from {table} where bid='{bid}' AND sid='{sid}'".format(table=borrowTable, bid=bid, sid=sid)
    cur.execute(checkIssueDate)
    for i in cur:
        issuedate = i[0]

    #checkDueDate = "select DueDate from {table} where bid='{bid} AND sid='{sid}''".format(table=borrowTable, bid=bid, sid=sid)
    #cur.execute(checkDueDate)
    #for i in cur:
     #   duedate = i[0]
    
    #duedate = issuedate + datetime.timedelta(days=14)
    duedate = issuedate + timedelta(days=14)
    delta = date.today() - duedate
    fine = (delta.days)

    deleteBorrow = "delete from {table} where bid = '{bid}' AND sid='{sid}'".format(table=borrowTable, bid=bid, sid=sid)
    updateBook = "update {table} set Copies = Copies+1 where bid = '{bid}'".format(table=bookTable, bid=bid)
    updateStudent = "update {table} set MoneyDue = {fine} where sid = '{sid}'".format(table=studentTable, sid=sid, fine=fine)
    insertReturnNoFine = "insert into {table}(sid,bid,IssueDate,ReturnDate,moneydue) VALUES('{sid}','{bid}','{IssueDate}',CURDATE(),0)".format(table=returnTable, sid=sid, bid=bid, IssueDate=issuedate)
    insertReturnWithFine = "insert into {table}(sid,bid,IssueDate,ReturnDate,moneydue) VALUES('{sid}','{bid}','{IssueDate}',CURDATE(),DATEDIFF(CURDATE(),'{DueDate}'))".format(table=returnTable, sid=sid, bid=bid, IssueDate=issuedate,fine=fine, DueDate=duedate)

    try:
        if bid in allBid and status == True:
            if duedate >= date.today():
                con.begin()
                cur.execute(updateBook)
                cur.execute(insertReturnNoFine)
                cur.execute(deleteBorrow)
                con.commit()
                messagebox.showinfo('Success',"Book Returned Successfully")
                root.destroy()
            #elif duedate < date.today():
            else:
                # con.begin()
                # cur.execute(updateBook)
                # cur.execute(updateStudent)
                # cur.execute(insertReturnWithFine)
                # cur.execute(deleteBorrow)
                # con.commit()
                messagebox.showinfo('Success', "Pay Fine Please")
                root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    root.destroy()
    
def returnBook(studentid): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Toplevel()
    root.title("Return Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    same = True
    n = 0.33

    Sid = studentid
    #background image

    bg_image = Image.open("returnbook.jpg")
    [imageSizeWidth, imageSizeHeight] = bg_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n)
    else:
        newImageSizeHeight = int(imageSizeHeight/n)

    bg_image = bg_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth,height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    #root = Tk()
    #root.title("Return Book")
    #root.minsize(width=400,height=400)
    #root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command= lambda: returnn(studentid))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
