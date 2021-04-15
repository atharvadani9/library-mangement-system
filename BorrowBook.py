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
borrowTable = "borrow" 
bookTable = "books"
studentTable = "students"
    
#List To store all Book IDs
allBid = [] 

def borrow(studentid):
    
    global borrowBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    sid = studentid #need to change this

    borrowBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()

    checkMoneyDue = "select MoneyDue from {table} where sid = '{sid}'".format(table=studentTable, sid=sid)
    cur.execute(checkMoneyDue)
    for i in cur:
        moneydue = i[0]
    if(moneydue > 0):
        allBid.clear()
        messagebox.showinfo('Message', "Pay Your Fine Before Borrowing")
        root.destroy()
        return

    checkthesid = 'abcdefghi'
    checkSid = "select sid from {table} where sid='{sid}'".format(table=borrowTable, sid=sid)
    cur.execute(checkSid)
    for i in cur:
        checkthesid = i[0]
    if(checkthesid == sid):
        allBid.clear()
        messagebox.showinfo('Message', "Return Previous Book Before Borrowing Another")
        root.destroy()
        return
    
    extractBid = "select bid from {table}".format(table=bookTable)
    try:
        cur.execute(extractBid)
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkCopies = "select Copies from {table} where bid='{bid}'".format(table=bookTable,bid=bid)
            cur.execute(checkCopies)
            for i in cur:
                check = i[0]

            if check >= 1:
                #checkSid = "select sid from {table} where sid='{sid}'".format(table=borrowTable,sid=sid)
                #cur.execute(checkSid)
                #for j in cur:
                #   checkthesid = j[0]
                #if checkthesid == sid:
                #    status = False
                #    allBid.clear()
                #    messagebox.showinfo("Error", "Student has already borrowed a book")
                #    root.destroy()
                #    return
                #else:
                status = True
            else:
                status = False

        else:
            allBid.clear()
            messagebox.showinfo("Error","Book ID not present")
            root.destroy()
            return
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    borrowSql = "insert into {table} (sid,bid,IssueDate) VALUES ('{sid}','{bid}',CURRENT_DATE())".format(table=borrowTable,sid=sid, bid=bid)
    show = "select * from {table}".format(table = borrowTable)
    
    updateStatus = "update {table} set Copies = Copies-1 where bid = '{bid}'".format(table=bookTable, bid=bid)
    try:
        if bid in allBid and status == True:
            con.begin()
            cur.execute(borrowSql)
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Borrowed Successfully")
            root.destroy()

        else:
            allBid.clear()
            messagebox.showinfo('Message',"All Copies Have Been Borrowed")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(sid)
    
    allBid.clear()
    
def borrowBook(studentid): 
    
    global borrowBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Toplevel() #Tk() before
    root.title("Borrow")
    root.minsize(width=400,height=400)
    root.geometry("800x700")

    same = True
    n = 0.33

    Sid = studentid

    #background image

    bg_image = Image.open("woodbg.jpg")
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
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)
    
    #Canvas1 = Canvas(root)
    #Canvas1.config(bg="#D6ED17")
    #Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Borrow Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    #lb2 = Label(labelFrame,text="Borrowed By : ", bg='black', fg='white')
    #lb2.place(relx=0.05,rely=0.4)
        
    #inf2 = Entry(labelFrame)
    #inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Borrow Button
    borrowBtn = Button(root,text="borrow",bg='#d1ccc0', fg='black',command=lambda: borrow(Sid))
    borrowBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
