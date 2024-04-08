from stuff_module import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import re


def is_persian(text):
    return re.match("^[آ-ی\s]*$",text)



def reset_form():
    code.set(0)
    name.set("")
    serial.set("")
    model.set("")
    count.set(0)
    price.set("")
    search_mn.set(0)
    search_mx.set(0)
    available.set(True)

def refresh_table():
    for row in table.get_children():
        table.delete(row)

    for stuff in find_all() :
        stuff = list(stuff)
        table.insert("",END,values= stuff)


def searching_by_name(event):
    for row in table.get_children():
        table.delete(row)

    result = find_by_name("%" + search.get() + "%")
    if result :
        for stuff in result :
            table.insert("",END,values = stuff)



def searching_by_count(event):
    for row in table.get_children():
        table.delete(row)

    result_c = find_by_count(search2.get())
    if result_c:
        for stuff in result_c:
            table.insert("",END,values=stuff)


def searching_by_price(event):
    for row in table.get_children():
        table.delete(row)

    if (search_mn.get() == "0" or search_mn.get() == ""   ) and (search_mx.get() == "0" or search_mx.get() == ""   )  :
        result_mx = find_all()
    else:
        result_mx = find_by_price(search_mn.get(), search_mx.get())

    if result_mx :
        for stuff in result_mx :
            table.insert("",END,values = stuff)



def selected_stuff(event):
    selected_row = table.focus()
    stuff = table.item(selected_row)["values"]
    print(table.item(selected_row)["tags"])
    code.set(stuff[0])
    name.set(stuff[1])
    serial.set(stuff[2])
    model.set(stuff[3])
    count.set(stuff[4])
    price.set(stuff[5])
    available.set(True)
    print(stuff)




def save_click():
    try :
        if is_persian(name.get()) :
            save(name.get(),model.get(),serial.get(),count.get(),price.get(),available.get())
            msg.showinfo("save","the stuff is saved")
            reset_form()
            refresh_table()
    except :
        msg.showerror("save","Invalid Data")




def edit_click():
    try:
        if is_persian (name.get()):
            edit(code.get(),name.get(),serial.get(),model.get(),count.get(),price.get(),available.get())
            msg.showinfo("Edit","the stuff is Edited")
            reset_form()
            refresh_table()
    except:
        msg.showerror("Edit","Invalid Data")


def remove_click():
    remove(code.get())
    if msg.askyesno("delete","Are you sure to Remove the stuff ?"):
        msg.showinfo("Delete","stuff Deleted")
    reset_form()
    refresh_table()


def exit_click():
    msg.askyesno("Exit","Are you sure to Exit ?")
    win.destroy()


win = Tk()

win.title("Market")
win.geometry("750x350")


Label(win,text="code").place(x=20,y=20)
code = IntVar()
Entry(win,textvariable=code,background="plum1").place(x=90,y=20)

Label(win,text="Name").place(x=20,y=50)
name = StringVar()
Entry(win,textvariable=name,background="plum1").place(x=90,y=50)



Label(win,text="Model").place(x=20,y=110)
model = StringVar()
Entry(win,textvariable=model,background="plum1").place(x=90,y=110)


Label(win,text="Count").place(x=20,y=140)
count = IntVar()
Entry(win,textvariable=count,background="plum1").place(x=90,y=140)



Label(win,text="Price").place(x=20,y=170)
price = StringVar()
Entry(win,textvariable=price,background="plum1").place(x=90,y=170)



Label(win,text="Serial").place(x=20,y=80)
serial = StringVar()
Entry(win,textvariable=serial,background="plum1").place(x=90,y=80)


style = ttk.Style()
style.map("TButton",
          foreground=[('pressed', 'maroon1'), ('active', 'black')],
          background=[('pressed', '!disabled', 'black'), ('active', 'orchid1')]
          )



btn1 = ttk.Button(win,text="save",width = 10,command=save_click)
btn1.place(x=30,y=270)

btn2 = ttk.Button(win,text="Edit",width = 10,command=edit_click)
btn2.place(x=120,y=270)

btn3 = ttk.Button(win,text="Remove",width = 10,command=remove_click)
btn3.place(x=210,y=270)

btn4= ttk.Button(win,text="Exit",width = 10,command=exit_click)
btn4.place(x=300,y=270)




available= BooleanVar()
ttk.Radiobutton(win,text="available",variable=available,value =1).place(x=30,y=200)
ttk.Radiobutton(win,text="unavailable",variable=available,value=0).place(x=30,y=230)
available.set(True)



table = ttk.Treeview(win,columns=(1,2,3,4,5),height=8,show = "headings")
table.column(1,width=50)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=100)
table.column(5,width=100)

table.heading(1,text="Code")
table.heading(2,text="Name")
table.heading(3,text="Model")
table.heading(4,text="Count")
table.heading(5,text="Price")




table.place(x=250,y=20)
table.bind("<ButtonRelease>",selected_stuff)
table.bind("<KeyRelease>", selected_stuff)

refresh_table()



Label(win,text="Search by Name :").place(x=450,y=210)
search = StringVar()
search_table = Entry(win,textvariable=search)
search_table.bind("<KeyRelease>",searching_by_name)
search_table.place(x=500,y=230)

Label(win,text="search by Count :").place(x=450,y=250)
search2=IntVar()
search_count = Entry(win,textvariable=search2)
search_count.bind("<KeyRelease>",searching_by_count)
search_count.place(x=500,y=270)




Label(win,text="search by price :").place(x=450,y=290)

search_mx = StringVar()
Label(win,text = "Max").place(x=500,y=320)
search_max =Entry(win,width=10,textvariable = search_mx)
search_max.place(x=540,y=320)
search_max.bind("<KeyRelease>",searching_by_price)

search_mn = StringVar()
Label(win,text="Min").place(x=610,y=320)
search_min = Entry(win,width=10,textvariable = search_mn)
search_min.place(x=650,y=320)
search_min.bind("<KeyRelease>",searching_by_price)

reset_form()




win.mainloop()