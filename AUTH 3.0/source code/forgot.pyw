from customtkinter import *
from PIL import Image
from tkinter import messagebox
import json

#redirect window
def login_window():
    root.destroy()
    import login #type: ignore
    if __name__=='__main__':
        login
#display forgot password
'''display forgot password'''
def get_password():
    try:
        Email = email_entry.get().strip()
        file = open('record.json','r')
        record = file.read()
        final = json.loads(record)
        if Email in final:
            password.configure(text=final[Email])
        elif not Email.strip():
            messagebox.showerror("Email","Email cannot be empty")
        else:
            messagebox.showerror('Email','does not exist')
    except:
        messagebox.showerror('file error',"File not exist")


# root 
root  = CTk()

#root title 
root.title("Auth 2.O")
root.iconbitmap("logo.ico")

#geometry 
width = 1080
height = 720
root.geometry(f"{width}x{height}")
root.maxsize(width,height)
root.minsize(width,height)

#root background 
image = CTkImage(dark_image=Image.open("forgot_page.jpg"),size=(width,height))
image_label =CTkLabel(root, image=image,text="")
image_label.place(relx=0.5, rely=0.5, anchor="center")


#text 
font = CTkFont(family="arial",size=30)
text = CTkLabel(master=root,text="Forgot password",font=font,bg_color="white",text_color="black")
text.place(relx=0.5, rely=0.15,x=20,y=20)
font_2 = CTkFont(family="arial",size=15)
text_2 = CTkLabel(master=root,text="Enter your Email",font=font_2,bg_color="white",text_color="black")
text_2.place(relx=0.5, rely=0.15,x=25,y=65)


email = CTkLabel(root,text="Email",font=("arial",15),text_color="Black",bg_color="white")
email.place(rely=0.5,relx=0.5,x=20,y=-50)
user_passwoed = CTkLabel(root,text="Password",font=("arial",15),text_color="Black",bg_color="white")
user_passwoed.place(rely=0.5,relx=0.5,x=20,y=10)

email_entry = CTkEntry(root,width=200,height=30 ,placeholder_text="Email",fg_color="white",bg_color="White",border_width=2,border_color="black",text_color="black")
email_entry.place(relx=0.5, rely=0.5,x=150,y=-50)
password = CTkLabel(root,width=200,height=30 ,text="",fg_color="white",bg_color="white",text_color="black")
password.place(relx=0.5, rely=0.5,x=150,y=10)


button_1 = CTkButton(root,text="Sign in...",font=("arial",12),text_color="black",fg_color="white",bg_color="white",hover_color="white",command=login_window)
button_1.place(relx=0.5, rely=0.5,x=170,y=150)

button_2 = CTkButton(root,width=100,height=30,text="Next",font=("arial",15),text_color="white",fg_color="black",bg_color="white",hover_color="#5780d3",command=get_password,corner_radius=15)
button_2.place(relx=0.5, rely=0.5,x=190,y=80)


root.mainloop()
