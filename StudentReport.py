from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

 
    
def SReport(studentid):

    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,bookInfo7,bookInfo8,bookInfo9,bookInfo10,con,cur,root,bookTable
    # Add your own database name and password here to reflect in the code
    mypass = "Tusharsai@1"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"

    root = Toplevel()
    root.title("Library")
    root.minsize(width=1350,height=700)
    root.geometry("600x500")


    # Take n greater than 0.25 and less than 5
    same=True
    n=0.4

    #sid = studentid

    background_image =Image.open("Reports.jpg")
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
    headingFrame1.place(relx=0.25,rely=0.03,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Student Report", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame3 = Frame(root,bg='black')
    labelFrame3.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.55)
    y = 0.25

    sid = studentid
    
    Label(labelFrame3, text="%-17s%-15s%-20s%-20s%-17s%-15s"%('SID','BID','Issue Date','Due Date','Return Date','Money Due'),bg='black',fg='white', font='Courier').place(relx=0.03,rely=0.1)
    Label(labelFrame3, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.02,rely=0.2)
    getBooks = "select * from returnbook WHERE sid ='{sid}'".format(sid = sid)
    print(sid)
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            temp1 = str(i[0])
            a1 = len(temp1)
            b1 = 17-a1
            temp2 = str(i[1])
            a2 = len(temp2)
            b2 = 15-a2
            temp3 = str(i[2])
            a3 = len(temp3)
            b3 = 20-a3
            temp4 = str(i[3])
            a4 = len(temp4)
            b4 = 20-a4
            temp5 = str(i[4])
            a5 = len(temp5)
            b5 = 20-a5
            temp6 = str(i[5])
            a6 = len(temp6)
            b6 = 3-a6

            #print(temp5+' '*b5+temp6+' '*b6)

            #Label(labelFrame, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+'   '*b5+temp6,bg='black',fg='white').place(relx=0.03,rely=y)
            Label(labelFrame3, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+' '*b5+temp6,bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
            #Label(labelFrame, text="%-20s%-45s%-58s%-20s%-60s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.03,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.6,rely=0.8, relwidth=0.18,relheight=0.08)
    
    
    root.mainloop()

# def SViewReport():

#     #sid = bookInfo10.get()
#     sid = 'S20190046'

#     labelFrame3 = Frame(root,bg='black')
#     labelFrame3.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.55)
#     y = 0.25
    
#     Label(labelFrame3, text="%-15s%-15s%-15s%-15s%-15s%-10s"%('SID','BID','Issue Date','Return Date','Due Date','Money Due'),bg='black',fg='white', font='Courier').place(relx=0.03,rely=0.1)
#     Label(labelFrame3, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.02,rely=0.2)
#     getBooks = "select * from returnbook WHERE sid ='{sid}'".format(sid = sid)
#     print(sid)
#     try:
#         cur.execute(getBooks)
#         con.commit()
#         for i in cur:
#             temp1 = str(i[0])
#             a1 = len(temp1)
#             b1 = 8-a1
#             temp2 = str(i[1])
#             a2 = len(temp2)
#             b2 = 20-a2
#             temp3 = str(i[2])
#             a3 = len(temp3)
#             b3 = 20-a3
#             temp4 = str(i[3])
#             a4 = len(temp4)
#             b4 = 12-a4
#             temp5 = str(i[4])
#             a5 = len(temp5)
#             b5 = 30-a5
#             temp6 = str(i[5])
#             a6 = len(temp6)
#             b6 = 3-a6

#             #print(temp5+' '*b5+temp6+' '*b6)

#             #Label(labelFrame, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+'   '*b5+temp6,bg='black',fg='white').place(relx=0.03,rely=y)
#             Label(labelFrame3, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+' '*b5+temp6,bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
#             #Label(labelFrame, text="%-20s%-45s%-58s%-20s%-60s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.03,rely=y)
#             y += 0.1
#     except:
#         messagebox.showinfo("Failed to fetch files from database")

#     root.mainloop()