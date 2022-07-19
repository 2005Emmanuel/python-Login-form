from tkinter import *
import tkinter.messagebox as MessageBOX
root = Tk()
root.title("Login form")
root.geometry("600x300")
root.configure(bg="#a83232")


# FUCTION DECLEARATION
def Validation():
    username_result = t_username.get()
    password_result = t_password.get()
    if username_result == "Emmanuel" and password_result == "12345":
        MessageBOX.showinfo("Login Access", "Login Successful")
    else:
        MessageBOX.showinfo("Wrong Entry", "Login Denied")


title = Label(root, text ="LOGIN", bg="#a83232", fg="white", font=("bold", 15))
title.place(x=250, y=20)

username = Label(root, text="USERNAME", bg="#a83232", fg="White", font=("bold", 13))
username.place(x=100, y=80)
t_username = Entry()
t_username.place(x=230, y=80)

password = Label(root, text="PASSWORD", bg="#a83232", fg="White", font=("bold", 13))
password.place(x=100, y=110)
t_password = Entry(root,show="*")
t_password.place(x=230, y=110)

submit = Button(root, text="LOGIN", bg="#003E53", fg="White", font=("bold", 13) ,command=Validation)
submit.place(x=250, y=140)
root.mainloop()