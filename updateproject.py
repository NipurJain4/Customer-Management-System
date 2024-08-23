import csv
from tkinter import *
import pymysql
from tkinter import messagebox, Frame
from tkinter import ttk
import pandas as pd
from tkinter import filedialog

con = pymysql.Connect(host="localhost", user="root", password="0852", database="project")
cur = con.cursor()
print("connection established successfully")
# qry = "create table custable1(id int primary key,Name varchar(30),Age int,mob varchar(10));
print("table created")


def savetreeview():
    with open("new.csv", "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        data1 = []
        for row_id in tree.get_children():
            row = tree.item(row_id)['values']
            csvwriter.writerow(row)
            data1.append(row)

        df = pd.DataFrame(data1, columns=["Id", "Name", "Age", "Mob"])

        # Ask the user for the file save location
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        # If the user cancels the save dialog, return
        if not file_path:
            return

            # Save the data to an Excel file
        df.to_excel(file_path, index=False)
        # print("Data exported to Excel successfully!")


def addframe():
    global root_add
    root_add = Tk()
    root_add.title("Add Customers")
    root_add.geometry("340x200+640+230")
    id_var = Label(root_add, text="Enter ID :", height=2, width=10, bg="skyblue")
    id_var.grid(row=0, column=0)
    global entr_id
    entr_id = StringVar()
    entr_id = Entry(root_add)
    entr_id.grid(row=0, column=1)
    name_var = Label(root_add, text="Enter name :", height=2, width=10, bg="skyblue")
    name_var.grid(row=1, column=0)
    global entr_name
    entr_name = StringVar()
    entr_name = Entry(root_add)
    entr_name.grid(row=1, column=1)
    age_var = Label(root_add, text="Enter age :", height=2, width=10, bg="skyblue")
    age_var.grid(row=2, column=0)
    global entr_age
    entr_age = StringVar()
    entr_age = Entry(root_add)
    entr_age.grid(row=2, column=1)
    mob_var = Label(root_add, text="Enter Mob:", height=2, width=10, bg="skyblue")
    mob_var.grid(row=3, column=0)
    global entr_mob
    entr_mob = StringVar()
    entr_mob = Entry(root_add)
    entr_mob.grid(row=3, column=1)
    global result_label_s
    result_label_s = Label(root_add, text="")
    result_label_s.grid(row=5, column=1)
    btn = Button(root_add, text="add", height=2, width=12, command=addata, bg="skyblue")
    btn.grid(row=6, column=1)
    root_add.mainloop()


def addata():
    try:
        id = entr_id.get()
        name = entr_name.get()
        age = entr_age.get()
        mob = entr_mob.get()
        qry = f"insert into custable1 values({id},'{name}',{age},'{mob}')"
        cur.execute(qry)
        con.commit()
        messagebox.showinfo("Cust Added", message="Customer Added Successfully")
        root_add.destroy()
        Display_All()
    except:
        result_label_s.config(text=" mandatory!!", fg="red")


def deletedata():
    id = enter_id.get()
    try:
        qry1 = f"select * from custable1 where id={id}"
        cur.execute(qry1)
        data = cur.fetchone()
        # print(data)
        # print(f"Data Found with {id} is:", data)
        if data is None:
            result_label_s.config(text="Not Found!!", fg="red")
        else:
            qry = f"delete from custable1 where id={id}"
            cur.execute(qry)
            con.commit()
            messagebox.showinfo("Deleted", "Data deleted Successfully")
            root_dlt.destroy()
            Display_All()
    except:
        result_label_s.config(text="Blank Field!!", fg="red")


def delete_frame():
    global root_dlt
    root_dlt = Tk()
    root_dlt.title("Delete")
    root_dlt.geometry("300x200+640+230")
    id_var = Label(root_dlt, text=" Enter ID", height=2, width=12, bg="sky blue")
    id_var.grid(row=1, column=1)
    global enter_id
    enter_id = Entry(root_dlt)
    enter_id.grid(row=1, column=2)
    global result_label_s
    result_label_s = Label(root_dlt, text="")
    result_label_s.grid(row=2, column=1)
    btn = Button(root_dlt, text="Delete", height=2, width=12, bg="sky blue", command=deletedata)
    btn.grid(row=3, column=1)
    root_dlt.mainloop()


def searchdata():
    id = entr_id.get()
    try:
        qry2 = f"select * from custable1 where id={id}"
        cur.execute(qry2)
        data = cur.fetchone()
        if data == None:
            result_label_s.config(text="Not Found!!", fg="red")
        # print(data[1])
        else:
            lblid_heading = Label(s_root, text="Customer ID", bg="Black", fg="white", width=13)
            lblid_heading.grid(row=4, column=0)
            lblname_heading = Label(s_root, text="Customer Name", bg="Black", fg="white", width=13)
            lblname_heading.grid(row=4, column=1)
            lblage_heading = Label(s_root, text="Customer Age", bg="Black", fg="white", width=13)
            lblage_heading.grid(row=4, column=2)
            lblage_heading = Label(s_root, text="Customer Mob", bg="Black", fg="white", width=13)
            lblage_heading.grid(row=4, column=3)
            lbl_id1 = Label(s_root, text=data[0], bg="Orange", width=13)
            lbl_id1.grid(row=5, column=0)
            lbl_name1 = Label(s_root, text=data[1], bg="Orange", width=13)
            lbl_name1.grid(row=5, column=1)
            lbl_age1 = Label(s_root, text=data[2], bg="Orange", width=13)
            lbl_age1.grid(row=5, column=2)
            lbl_age1 = Label(s_root, text=data[3], bg="Orange", width=13)
            lbl_age1.grid(row=5, column=3)
    except:
        result_label_s.config(text="Blank Field!!", fg="red")


def search_frame():
    global s_root
    s_root = Tk()
    s_root.title("Search Bar")
    s_root.geometry("420x140+640+230")
    id_var = Label(s_root, text="Enter ID:", height=2, width=10)
    id_var.grid(row=1, column=0)
    global entr_id
    entr_id = Entry(s_root)
    entr_id.grid(row=1, column=1)
    global result_label_s
    result_label_s = Label(s_root, text="")
    result_label_s.grid(row=2, column=0)
    btn = Button(s_root, text="Search", height=1, width=10, command=searchdata)
    btn.grid(row=3, column=0)
    s_root.mainloop()


def Display_All():
    qry = "select * from custable1"
    cur.execute(qry)
    data = cur.fetchall()
    for row in tree.get_children():
        tree.delete(row)

    for row in data:
        tree.insert("", "end", values=row)


def editdata():
    id = enter_id.get()
    name = enter_name.get()
    age = enter_age.get()
    mob = enter_mob.get()
    try:
        qry = f"update custable1 set Name='{name}',Age={age},mob={mob} where id={id}"
        cur.execute(qry)
        con.commit()
        root_edit.destroy()

    except:
        result_label_s.config(text="All fields are Mandatory!!", fg="red")


def edit_frame():
    global root_edit
    root_edit = Tk()
    root_edit.geometry("300x200+640+230")
    id_var = Label(root_edit, text=" Enter ID:", height=2, width=10, bg="skyblue")
    id_var.grid(row=0, column=0)
    global enter_id
    enter_id = Entry(root_edit)
    enter_id.grid(row=0, column=1)
    name_var = Label(root_edit, text="Enter name :", height=2, width=10, bg="skyblue")
    name_var.grid(row=1, column=0)
    global enter_name
    enter_name = StringVar()
    enter_name = Entry(root_edit)
    enter_name.grid(row=1, column=1)
    age_var = Label(root_edit, text="Enter age :", height=2, width=10, bg="skyblue")
    age_var.grid(row=2, column=0)
    global enter_age
    enter_age = StringVar()
    enter_age = Entry(root_edit)
    enter_age.grid(row=2, column=1)
    mob_var = Label(root_edit, text="Enter Mob :", height=2, width=10, bg="skyblue")
    mob_var.grid(row=3, column=0)
    global enter_mob
    enter_mob = StringVar()
    enter_mob = Entry(root_edit)
    enter_mob.grid(row=3, column=1)
    global result_label_s
    result_label_s = Label(root_edit, text="")
    result_label_s.grid(row=4, column=1)
    btn = Button(root_edit, text="edit", height=2, width=12, command=editdata)
    btn.grid(row=5, column=0)
    root_edit.mainloop()


def exitButtonClick():
    win.destroy()


def main_page():
    print("enter in main program")
    global framemain
    framemain = Frame(win, bg="sky blue", height=500, width=700)
    framemain.grid(row=0, column=0)
    header = Label(framemain, text="Welcome to Nipur CMS", bg="red", fg="white", height=5, width=80, font=30)
    header.place(x=0, y=0)
    global frame_main
    left_button = Button(frame, relief=RAISED, text="<<", cursor="spider", bg="black", fg="white", command=loginframe)
    left_button.place(x=20, y=100)

    addlbl = Label(framemain, text=" Add Data", height=2, width=15, bg="Black", fg="white")
    addlbl.place(x=20, y=120)
    addbtn = Button(framemain, text="click here", height=2, width=12, command=addframe)
    addbtn.place(x=150, y=120)

    dltlbl = Label(framemain, text=" Delete Data", height=2, width=15, bg="Black", fg="white")
    dltlbl.place(x=20, y=160)
    dltbtn = Button(framemain, text="click here", height=2, width=12, command=delete_frame)
    dltbtn.place(x=150, y=160)

    editlbl = Label(framemain, text=" Edit Data", height=2, width=15, bg="Black", fg="white")
    editlbl.place(x=20, y=200)
    editbtn = Button(framemain, text="click here", height=2, width=12, command=edit_frame)
    editbtn.place(x=150, y=200)

    dspllbl = Label(framemain, text=" Display All", height=2, width=15, bg="Black", fg="white")
    dspllbl.place(x=20, y=240)
    dsplbtn = Button(framemain, text="click here", height=2, width=12, command=Display_All)
    dsplbtn.place(x=150, y=240)

    srchlbl = Label(framemain, text=" Search", height=2, width=15, bg="Black", fg="white")
    srchlbl.place(x=20, y=280)
    srchbtn = Button(framemain, text="click here", height=2, width=12, command=search_frame)
    srchbtn.place(x=150, y=280)

    exitbtn = Button(framemain, text="Exit", height=2, width=12, command=exitButtonClick)
    exitbtn.place(x=100, y=400)

    global tree
    tree = ttk.Treeview(framemain, columns=("ID", "Name", "Age", "Mob"))
    tree['columns'] = ('Id', 'Name', 'Age', 'Mob')
    tree.column('#0', width=0, stretch=NO)
    tree.column('Id', anchor=CENTER, width=80)
    tree.column('Name', anchor=CENTER, width=80)
    tree.column('Age', anchor=CENTER, width=80)
    tree.column('Mob', anchor=CENTER, width=80)
    tree.heading("Id", text="Id", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Age", text="Age", anchor=CENTER)
    tree.heading("Mob", text="Mob", anchor=CENTER)
    tree.place(x=300, y=120)
    export_button = Button(framemain, text="Export to Excel", command=savetreeview)
    export_button.place(x=320, y=400)


def login():
    user = user_entry_l.get()
    pswd = pswd_entry_l.get()
    cur.execute(f"select * from cred")
    data = cur.fetchall()
    for i in range(len(data)):
        if data[i][2] == user:
            if data[i][3] == pswd:
                main_page()
            else:
                result_label.config(text="Wrong Password!!", fg="red")
                break
        else:
            result_label.config(text="User not found", fg="red")


def loginframe():
    frame = Frame(win, bg="sky blue", height=500, width=700)
    frame.grid(row=0, column=0)
    header = Label(frame, text="Welcome to Nipur CMS", bg="red", fg="white", height=5, width=80, font=30)
    header.place(x=0, y=0)

    left_button = Button(frame, relief=RAISED, text="<<", cursor="spider", bg="black", fg="white", command=start)
    left_button.place(x=20, y=100)

    user_label = Label(frame, text="Username :", font=('Arial', 10, 'bold'))
    user_label.place(x=200, y=200)
    global user_entry_l
    user_entry_l = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    user_entry_l.place(x=280, y=200)
    # user_entry_l.insert(0,'Username')
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=220)
    pswd_label = Label(frame, text="Password :", font=('Arial', 10, 'bold'))
    pswd_label.place(x=200, y=240)
    global pswd_entry_l
    pswd_entry_l = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    pswd_entry_l.place(x=280, y=240)
    # pswd_entry_l.insert(0, 'Password')
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=260)
    lbtn = Button(win, text="Submit", height=1, width=8, command=login)
    lbtn.place(x=240, y=300)
    global result_label
    result_label = Label(frame, text="", bg="sky blue")
    result_label.place(x=200, y=270)


def signin():
    first = first_entry.get()
    last = last_entry.get()
    user = user_entry.get()
    pswd = pswd_entry.get()
    if not first_entry.get():
        messagebox.showerror("Error", "First name cannot be blank.")
    else:
        if not last_entry.get():
            messagebox.showerror("Error", "Last name cannot be blank.")
        else:
            if not user_entry.get():
                messagebox.showerror("Error", "Username cannot be blank.")
            else:
                if not pswd_entry.get():
                    messagebox.showerror("Error", "password cannot be blank.")
                else:
                    qry = f"insert into cred values('{first}','{last}','{user}','{pswd}')"
                    cur.execute(qry)
                    con.commit()
                    messagebox.showinfo("Signed In", "Account Created Successfully")
                    loginframe()
                    messagebox.showinfo("Everyhting looks good")



def signupframe():
    frame = Frame(win, bg="sky blue", height=500, width=700)
    frame.grid(row=0, column=0)
    header = Label(frame, text="Welcome to Nipur CMS", bg="red", fg="white", height=5, width=80, font=30)
    header.place(x=0, y=0)
    left_button = Button(frame, relief=RAISED, text="<<", cursor="spider", bg="black", fg="white", command=start)
    left_button.place(x=20, y=100)
    first_label = Label(frame, text="First Name :", width=10)
    first_label.place(x=200, y=200)
    global first_entry
    first_entry = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    first_entry.place(x=280, y=200)
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=220)
    last_label = Label(frame, text="Last Name :", width=10)
    last_label.place(x=200, y=240)
    global last_entry
    last_entry = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    last_entry.place(x=280, y=240)
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=260)
    user_label = Label(frame, text="Username :", width=10)
    user_label.place(x=200, y=280)
    global user_entry
    user_entry = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    user_entry.place(x=280, y=280)
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=300)
    pswd_label = Label(frame, text="Password :", width=10)
    pswd_label.place(x=200, y=320)
    global pswd_entry
    pswd_entry = Entry(frame, bg="sky blue", border=0, font=('Arial', 10, 'bold', 'italic'))
    pswd_entry.place(x=280, y=320)
    Frame(frame, height=2, width=150, bg="Black").place(x=280, y=340)
    sign_btn = Button(frame, text="Sign in", height=2, width=10, command=signin)
    sign_btn.place(x=300, y=370)
    global result_label
    result_label = Label(frame, text="", bg="sky blue")
    result_label.place(x=200, y=345)


def Display_credential():
    root_cred = Tk()
    qry = "select * from cred"
    cur.execute(qry)
    data = cur.fetchall()
    lblfirst_heading = Label(root_cred, text="First Name", font=20, bg="Black", fg="white", width=20)
    lblfirst_heading.grid(row=0, column=0)
    lbllast_heading = Label(root_cred, text="Last Name", font=20, bg="Black", fg="white", width=20)
    lbllast_heading.grid(row=0, column=1)
    lbluser_heading = Label(root_cred, text="User Name", font=20, bg="Black", fg="white", width=20)
    lbluser_heading.grid(row=0, column=2)
    lblpswd_heading = Label(root_cred, text="Password", font=20, bg="Black", fg="white", width=20)
    lblpswd_heading.grid(row=0, column=3)
    for i in range(len(data)):
        lbl_first = Label(root_cred, text=data[i][0], font=20, bg="grey", width=20)
        lbl_first.grid(row=i + 1, column=0)
        lbl_last = Label(root_cred, text=data[i][1], font=20, bg="grey", width=20)
        lbl_last.grid(row=i + 1, column=1)
        lbl_user = Label(root_cred, text=data[i][2], font=20, bg="grey", width=20)
        lbl_user.grid(row=i + 1, column=2)
        lbl_pswd = Label(root_cred, text=data[i][3], font=20, bg="grey", width=20)
        lbl_pswd.grid(row=i + 1, column=3)


win = Tk()
win.title("Nipur CMS")
win.geometry('700x500+300+80')
win.resizable(0, 0)
frame = Frame(win)


def start():
    frame = Frame(win, bg="sky blue", height=500, width=700)
    frame.grid(row=0, column=0)
    header = Label(frame, text="WELCOME!!  CUSTOMER MANAGEMENT SYSTEM", bg="red", fg="white", height=5, width=80,
                   font=30)
    header.place(x=0, y=0)
    log_btn = Button(frame, text="Log in", height=2, width=15, relief=RAISED, bg="black", fg="white", cursor="spider",
                     command=loginframe)
    log_btn.place(x=200, y=200)
    reg_btn = Button(frame, text="Sign Up", height=2, width=15, relief=RAISED, bg="black", fg="white", cursor="spider",
                     command=signupframe)
    reg_btn.place(x=400, y=200)
    footer = Label(frame, text="@Copyright 2023", fg="black", height=1, width=100)
    footer.place(x=0, y=479)
    mb = Button(frame, text="Setting", relief=RAISED, bg="black", fg="white", cursor="spider",command=Display_credential)
    mb.place(x=0, y=475)


start()
win.mainloop()
con.close()
