from customtkinter import *
from PIL import Image
from function_signup import *




def login_page():
    root.destroy()
    import login # type: ignore
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
image = CTkImage(dark_image=Image.open("signup_page.jpg"),size=(width,height))
image_label =CTkLabel(root, image=image,text="")
image_label.place(relx=0.5, rely=0.5, anchor="center")


#text 
font = CTkFont(family="arial",size=40)
text = CTkLabel(master=root,text="Sign up",font=font,bg_color="white",text_color="black")
text.place(relx=0.5, rely=0.15,x=20,y=20)
font_2 = CTkFont(family="arial",size=15)
text_2 = CTkLabel(master=root,text="To become a member",font=font_2,bg_color="white",text_color="black")
text_2.place(relx=0.5, rely=0.15,x=25,y=65)


email = CTkLabel(root,text="Email",font=("arial",15),text_color="Black",bg_color="white")
email.place(rely=0.5,relx=0.5,x=20,y=-50)
user_passwoed = CTkLabel(root,text="Password",font=("arial",15),text_color="Black",bg_color="white")
user_passwoed.place(rely=0.5,relx=0.5,x=20,y=10)

email_entry = CTkEntry(root,width=200,height=30 ,placeholder_text="Email",fg_color="white",bg_color="White",border_width=2,border_color="black",text_color="black")
email_entry.place(relx=0.5, rely=0.5,x=150,y=-50)
password = CTkEntry(root,width=200,height=30 ,placeholder_text="password",fg_color="white",bg_color="white",border_width=2,border_color="black",text_color="black")
password.place(relx=0.5, rely=0.5,x=150,y=10)

button_1 = CTkButton(root,text="Already a member..? Log in",font=("arial",12),text_color="black",fg_color="white",bg_color="white",hover_color="white",command=login_page)
button_1.place(relx=0.5, rely=0.5,x=160,y=150)

button_2 = CTkButton(root,width=100,height=30,text="Sign up",font=("arial",15),text_color="white",fg_color="black",bg_color="white",hover_color="#5780d3",command=lambda: check_input(email_entry.get(),password.get()),corner_radius=15)
button_2.place(relx=0.5, rely=0.5,x=190,y=80)


root.mainloop()
