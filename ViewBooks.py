from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
<<<<<<< HEAD
mypass = "mysqldatabase"
=======
mypass = "1234"
>>>>>>> parent of 39a05a2 (proj)
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
<<<<<<< HEAD
    #create table books(bid  int primary key, title varchar(30), author varchar(16), copies int, remarks varchar(35), publisher varchar(25));
    Label(labelFrame, text="%-11s%-28s%-17s%-12s%-22s%-10s"%('BID','Title','Author','Copies','Remarks','Publisher'),bg='black',fg='white', font='Courier').place(relx=0.03,rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.02,rely=0.2)
=======
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
>>>>>>> parent of 39a05a2 (proj)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
<<<<<<< HEAD
            temp1 = str(i[0])
            a1 = len(temp1)
            b1 = 10-a1
            temp2 = str(i[1])
            a2 = len(temp2)
            b2 = 28-a2
            temp3 = str(i[2])
            a3 = len(temp3)
            b3 = 20-a3
            temp4 = str(i[3])
            a4 = len(temp4)
            b4 = 8-a4
            temp5 = str(i[4])
            a5 = len(temp5)
            b5 = 25-a5
            temp6 = str(i[5])
            a6 = len(temp6)
            b6 = 3-a6

            #print(temp5+' '*b5+temp6+' '*b6)

            #Label(labelFrame, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+'   '*b5+temp6,bg='black',fg='white').place(relx=0.03,rely=y)
            Label(labelFrame, text= temp1+' '*b1+temp2+' '*b2+temp3+' '*b3+temp4+' '*b4+temp5+' '*b5+temp6,bg='black',fg='white', font='Courier').place(relx=0.03,rely=y)
            #Label(labelFrame, text="%-20s%-45s%-58s%-20s%-60s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.03,rely=y)
=======
            Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
>>>>>>> parent of 39a05a2 (proj)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()