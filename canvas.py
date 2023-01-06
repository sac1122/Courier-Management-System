from tkinter import *
from tkinter import messagebox
import time
root=0
creds='sac.txt'
credss='det.txt'
det='track.txt'
ac='Profile.txt'
saves='feedback.txt'
menu=[]
menuh=[]
########################################*****************************LOGIN***************************##################################################################
def login():
    global root
    global canvas
    global name
    global pwrd
    global menu
    global gif3
    global img1
    global img
    global ham
    global gif4
    global log
    global pet
    root=Tk()
    canvas=Canvas(root,width=1366,height=680,bg="white")
    img=PhotoImage(file="pick.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
    canvas.pack()
    root.title("welcome to log_in")
    #canvas.create_rectangle(550,60,800,300,outline="white",width=3)
    canvas.create_text(620,280,text="LOG IN",fill="#ff0000",font=('calibri(body)', 50, 'bold','underline'))

    canvas.create_text(500,410,text="Username",fill="#ff0000",font=('calibri(body)', 16, 'bold'))
    name=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(700,410,window=name)
    
    canvas.create_text(500,460,text="Password",fill="#ff0000",font=('calibri(body)', 16, 'bold'))
    pwrd=Entry(canvas,bg="white",show="*",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(700,460,window=pwrd)
    
    btn1=Button(canvas,text="log_in",width=12,command=checklogin)
    canvas.create_window(540,550,window=btn1)
    
    btn2=Button(canvas,text="New User",width=12,command=account)
    canvas.create_window(700,550,window=btn2)
    a=canvas.create_text(620,590,text="Forgot password",fill="black",font=('Georgia', 10,'bold','underline'))
    canvas.tag_bind(a, '<ButtonPress-1>',forgot)
    
    #canvas.create_oval(550,60,800,300,outline="white",width=3)
    root.mainloop()
user=""
def checklogin():
    global user
    global pet
    global passw
    with open(creds,'r') as f:
         data=f.readlines()
         for i in range(len(data)):
             uname,passw,pet=data[i].split()
             if name.get()==uname and pwrd.get()==passw.rstrip():
                 canvas.delete("all")
                 #root.destroy()
                 user=uname
                 home()
                 #canvas.create_text(200,280,text="logged in succesfully...",fill="grey",font=('calibri(body)', 20, 'italic'))
                 return
         messagebox.showerror("log in failed","Invalid logged in")
         #canvas.create_text(200,280,text="Invalid logged in...",fill="grey",font=('calibri(body)', 20, 'italic'))
         
def logout(event):
    global root
    global canvas
    root.destroy()
    login()
def cancel():
    global root
    global canvas
    root.destroy()
    login()


def forgot(event):
    global pet
    global t
    global img
    global btn2
    global pwd
    canvas.delete("all")
    img=PhotoImage(file="dr.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
    canvas.create_rectangle(370,150,940,420,outline="black",width=3)
    canvas.create_text(550,170,text="Find your account",fill="black",font=('calibri(body)', 20, 'bold'),anchor=NW)
    canvas.create_text(400,220,text="Username",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
    canvas.create_text(400,270,text="What is your pet name?",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
    pet=Entry(canvas,bg="white",bd=2,font=('calibri(body)',15, 'italic'))
    canvas.create_window(810,280,window=pet)
    t=Entry(canvas,bg="white",bd=2,font=('calibri(body)',15, 'italic'))
    canvas.create_window(810,230,window=t)
    canvas.create_text(400,320,text="New password",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
    pwd=Entry(canvas,bg="white",bd=2,font=('calibri(body)',15, 'italic'))
    canvas.create_window(810,330,window=pwd)
    btn2=Button(canvas,text="Submit",width=12,command=password)
    canvas.create_window(580,390,window=btn2)
    btn=Button(canvas,text="cancel",width=12,command=cancel)
    canvas.create_window(730,390,window=btn)

def password():
    global pet
    global pname
    global t
    global pet
    global pets
    global pwd
    global so
    flag=0
    f=pwd.get()
    with open(creds,'r') as s:
        so=s.readlines()
        s.close()
        for i in range(len(so)):
            pname,passw,pets=so[i].split()
            if t.get()==pname and pet.get()==pets.rstrip():
                so[i]=pname+" "+f+" "+pets+"\n"
                
                flag=1
        if flag:
            with open(creds,'w') as s:
                for i in so:
                    s.write(i)
                    
            s.close()
            messagebox.showinfo("password reset ","Your password is successfully reset.")
            root.destroy()
            login()
        else:
            messagebox.showerror("password reset failed","Invalid username or security question?")
            canvas.delete("all")
            
            
                  
                
                
            
                
        #canvas.create_text(650,650,text="your account is not found.",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    
#####################################################*************************Register***********************##########################################################    
def account():
    global root
    global canvas
    global fname
    global lname
    global email
    global mob
    global add
    global city
    global pin
    global pet
    canvas.delete("all")
    img=PhotoImage(file="vc.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
    canvas.pack()
    root.title("welcome to account")
    
    canvas.create_rectangle(475,135,890,675,outline="#1e90ff",width=3)

    imgs=PhotoImage(file="userss.gif")
    canvas.create_image(620,70,image=imgs,anchor=NW)
    canvas.pack()

    canvas.create_text(680,40,text="Create an account",fill="#1e90ff",font=('calibri(body)', 30, 'italic'))
    
    

    canvas.create_text(580,210,text="First Name",fill="black",font=('Georgia', 16, 'bold'))
    fname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,210,window=fname)
    
    canvas.create_text(580,260,text="Last Name",fill="black",font=('Georgia', 16, 'bold'))
    lname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,260,window=lname)
    v=IntVar()
    rb=Radiobutton(root,text="Male", variable=v,value=1,bg="white",fg="black",font=('Georgia', 15, 'italic'))
    canvas.create_window(610,330,window=rb)
    rb2=Radiobutton(root,text="Female",variable=v, value=2,bg="white",fg="black",font=('Georgia', 15, 'italic'))
    canvas.create_window(740,330,window=rb2)
    canvas.create_text(600,300,text="Chose your sex : ",fill="black",font=('Georgia',12, 'bold'))

    canvas.create_text(580,370,text="E-mail",fill="black",font=('Georgia', 16, 'bold'))
    email=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,370,window=email)

    canvas.create_text(580,420,text="Mobile no.",fill="black",font=('Georgia', 16, 'bold'))
    mob=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,420,window=mob)

    canvas.create_text(580,470,text="Address",fill="black",font=('Georgia', 16, 'bold'))
    add=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,470,window=add)

    canvas.create_text(580,520,text="City",fill="black",font=('Georgia', 16, 'bold'))
    city=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,520,window=city)

    canvas.create_text(580,570,text="pincode",fill="black",font=('Georgia', 16, 'bold'))
    pin=Entry(canvas,bg="white",bd=2,font=('calibri(body)',12, 'italic'))
    canvas.create_window(760,570,window=pin)

    canvas.create_text(600,610,text="What is your pet name?",fill="black",font=('Georgia', 12, 'bold'))
    pet=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(780,610,window=pet)
    

    btn2=Button(canvas,text="Register",width=12,bg="#1e90ff",fg="white",command=signup)
    canvas.create_window(680,650,window=btn2)
    root.mainloop()    

def detail():
    global name
    with open(ac,'a') as g:
        g.write(name.get())
        g.write(" ")
        g.write(fname.get())
        g.write(" ")
        g.write(lname.get())
        g.write(" ")
        g.write(email.get())
        g.write(" ")
        g.write(mob.get())
        g.write(" ")
        g.write(add.get())
        g.write(" ")
        g.write(city.get())
        g.write(" ")
        g.write(pin.get())
        g.write("\n")
        fssignup()
###############################################*************************SIGNUP**************************#############################################################
def signup():
    global root
    global canvas
    global name
    global pwrd
    global menu
    global gif3
    global img1
    global img
    global ham
    global gif4
    global log
    menu=[]
    canvas.delete("all")
    img=PhotoImage(file="KMS1.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
    root.title("welcome to log_in")
    #canvas.create_rectangle(550,60,800,300,outline="white",width=3)
    canvas.create_text(1170,60,text="SIGN UP",fill="blue",font=('calibri(body)', 30, 'italic'))
    canvas.create_text(1100,120,text="Username",fill="blue",font=('calibri(body)', 16, 'italic'))
    name=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(1250,120,window=name)
    canvas.create_text(1100,160,text="Password",fill="blue",font=('calibri(body)', 16, 'italic'))
    pwrd=Entry(canvas,bg="white",show="*",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(1250,160,window=pwrd)
    btn1=Button(canvas,text="sign_up",width=12,bg="blue",fg="white",command=detail)
    canvas.create_window(1180,220,window=btn1)
    
    #canvas.create_oval(550,60,800,300,outline="white",width=3)
    
def fssignup():
    global name
    global pwrd
    global pet
    global creds
    with open(creds,'a') as f:
        f.write(name.get())
        f.write(" ")
        f.write(pwrd.get())
        f.write(" ")
        f.write(pet.get())
        f.write("\n")
    root.destroy()
    login()
        

def quito(event):
    global root
    root.destroy()
    
###########################################################*****************Home******************####################################################################

def callhome(event):
    global root
    global canvas
    canvas.delete("all")
    #root.destroy()
    home()


def home():
    global root
    global canvas
    global menu
    global gif3
    global img1
    global img
    global ham
    global gif4
    global log
    global y
    global menuh
    global uname
    menuh=[]
    img=PhotoImage(file="online.gif")
    canvas.create_image(90,80,image=img,anchor=NW)
    canvas.create_rectangle(1100,80,1350,575,outline="black",width=1,fill="white")
    canvas.create_rectangle(10,580,1350,680,outline="white",width=1,fill="white")                ##1e90ff
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)

    canvas.create_text(130,600,text="7,000,000+",fill="black",font=('Georgia', 14, 'bold'),anchor=NW)
    canvas.create_text(110,630,text="Orders every month",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    canvas.create_text(410,600,text="13000+ Pincodes",fill="black",font=('Georgia', 14, 'bold'),anchor=NW)
    canvas.create_text(410,630,text="1400+ cities serviced",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    canvas.create_text(720,600,text="Cash on Delivery",fill="black",font=('Georgia', 14, 'bold'),anchor=NW)
    canvas.create_text(700,630,text="Multiple delivery options",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    canvas.create_text(1040,600,text="2 Day Remittance",fill="black",font=('Georgia', 14, 'bold'),anchor=NW)
    canvas.create_text(1030,630,text="fastest remittance cycle",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)

    #canvas.create_text(1120,100,text="CMS seamlessly",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
    #canvas.create_text(1120,140,text="CMS everywhere",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
   # canvas.create_text(1120,180,text="CMS faster",fill="black",font=('Georgia', 16, 'bold'),anchor=NW)
    
    canvas.create_text(1110,100,text="Our Logistics and fulfillment ",fill="red",font=('Georgia', 12, 'bold'),anchor=NW)
    canvas.create_text(1110,120,text="support for your business.",fill="red",font=('Georgia', 12, 'bold'),anchor=NW)
    canvas.create_text(1120,160,text="WHAT",fill="black",font=('Bodoni MT', 22, 'bold'),anchor=NW)
    canvas.create_text(1210,162,text="we offer?",fill="black",font=('Bodoni MT', 20, 'bold'),anchor=NW)
    canvas.create_text(1120,200,text="Transportation",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,240,text="Freight",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,280,text="Warehousing",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,320,text="International",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,360,text="WHY",fill="black",font=('Bodoni MT', 22, 'bold'),anchor=NW)
    canvas.create_text(1190,362,text="us?",fill="black",font=('Bodoni MT', 20, 'bold'),anchor=NW)
    canvas.create_text(1120,400,text="Largest Network",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,440,text="Unbeatable Prices",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,480,text="Fast Deliveries",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    canvas.create_text(1120,520,text="Tech Support",fill="blue",font=('Georgia', 16, 'italic'),anchor=NW)
    
    menu=[]
    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15,5, image = gif3, anchor = NW)
    #gif4=PhotoImage(file = "do.gif")
    #log=canvas.create_image(1100, 30, image = gif4, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")

    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="red",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()
y=0

def movemenu(event):
    global canvas
    global menu
    global ham
    global y
    if y%2==0:
        for mv in range(0,20,1):
            canvas.move(ham,mv-1,0)
            for i in range(len(menu)):
                canvas.move(menu[i],mv,0)
            canvas.update()
            time.sleep(0.05)
    else:
        for mv in range(0,-20,-1):
            canvas.move(ham,mv+1,0)
            for i in range(len(menu)):
                canvas.move(menu[i],mv,0)
            canvas.update()
            time.sleep(0.05)
    y+=1  

##############################################**************************TRACK************************************#####################################################
    
def goto_track(event):
    global root
    global canvas
    canvas.delete("all")
    #root.destroy()
    track()

def track():
    global root
    global canvas
    global t_id
    global m_no
    global menu
    global img1
    global img
    global gif3
    global ham
    global y
    global uname
    global menuh
    global a
    global b
    #root=Tk()
    menuh=[]
    menu=[]
    y=0
    canvas.delete("all")
    img=PhotoImage(file="banner1.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
    
    root.title("welcome to track consignment")
                    ##1e90ff
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))

    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)

    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15,5, image = gif3, anchor = NW)
    #gif4=PhotoImage(file = "do.gif")
    #log=canvas.create_image(1100, 30, image = gif4, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")
    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)

    canvas.create_text(450,200,text='"Todays delivery problems solved tomorrow."',fill="white",font=('calibri(body)', 30, 'italic'))
    canvas.create_text(450,250,text='"When there is no tomorrow."',fill="white",font=('calibri(body)', 30, 'italic'))

    canvas.create_text(1150,80,text="Tracking Courier",fill="white",font=('calibri(body)', 30, 'italic'))
    #canvas.create_rectangle(550,60,800,300,outline="white",width=3)
    a=canvas.create_text(1050,150,text="Tracking_Id",fill="#ff0000",font=('calibri(body)', 18, 'italic'))
    t_id=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(1200,150,window=t_id)
    b=canvas.create_text(1050,200,text="Mobile_no.",fill="#ff0000",font=('calibri(body)', 18, 'italic'))
    m_no=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(1200,200,window=m_no)
    btn1=Button(canvas,text="Track",width=12,command=tracking)
    canvas.create_window(1150,250,window=btn1)
    #canvas.create_oval(550,60,800,300,outline="white",width=3)
    
    

 

def tracking():
    global img
    global imgwgt
    global fl
    global a
    global b
    global c
    global g
    global d
    global f
    global e
    global h
    global i
    global menuh
    global ham
    global gif3
    global img1
    global menu
    global ip
    menuh=[]
    with open(credss,'r') as s:
         data=s.readlines()
         with open(det,'r') as s1:
             data1=s1.readlines()
             canvas.delete("all")
             #img=PhotoImage(file="a.gif")
             #canvas.create_image(0,0,image=img,anchor=NW)
             for i in range(len(data)):
                    track_id,b_date,s_name,s_add,s_phone,r_name,r_add,r_phone,weight,st,mo,ip,price=data[i].split()
                    if t_id.get()==track_id and m_no.get()==s_phone :
                        for j in range(len(data1)):
                            track2_id,loc1,update1,del_ex,cs,rem,loc2,update2,cs2,rem2=data1[j].split()
                            if track_id==track2_id:
                                canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
                                canvas.create_line(60,0,60,45,fill="black",width=1)
                                canvas.create_line(150,0,150,45,fill="black",width=1)
                                canvas.create_line(240,0,240,45,fill="black",width=1)
                                canvas.create_line(330,0,330,45,fill="black",width=1)
                                canvas.create_line(420,0,420,45,fill="black",width=1)
                                canvas.create_line(530,0,530,45,fill="black",width=1)
                                canvas.create_line(640,0,640,45,fill="black",width=1)
                                canvas.create_line(730,0,730,45,fill="black",width=1)           
                                canvas.create_line(1270,0,1270,45,fill="black",width=1)
                                #canvas.create_line(1340,0,1340,45,fill="black",width=1)
                                menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                                canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
                                canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
                                canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
                                canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
                                canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
                                canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
                                canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
                                canvas.tag_bind(menuh[5],'<Enter>',contact)
                                menu=[]
                                gif3=PhotoImage(file = "images3.gif")
                                ham=canvas.create_image(15,5, image = gif3, anchor = NW)
                                #gif4=PhotoImage(file = "do.gif")
                                #log=canvas.create_image(1100, 30, image = gif4, anchor = NW)
                                menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
                                img1=PhotoImage(file="users.gif")
                                menu.append(canvas.create_image(-100,80,image=img1))
                                menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
                                menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
                                menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="red",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
                                menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

                                canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
                                canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
                                canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
                                canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
                                canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
                                canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
                                canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
                                canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
                                canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
                                 
                                canvas.create_rectangle(210,60,1090,540,outline="black",width=2)
                                canvas.create_rectangle(210,380,1090,420,outline="black",width=2,fill="white")
                                canvas.create_text(230,70,text="Booking Details :- ",fill="#ff0000",font=('calibri(body)', 15, 'bold'),anchor=NW)
                                canvas.create_text(410,70,text=track_id,fill="black",font=('calibri(body)', 15, 'bold'),anchor=NW)
                                
                                canvas.create_line(210,100,1090,100,fill="black",width=2)
                                canvas.create_line(410,100,410,380,fill="black",width=2)
                                canvas.create_line(850,100,850,380,fill="black",width=2)
                                canvas.create_line(650,100,650,380,fill="black",width=2)
                                canvas.create_line(210,140,1090,140,fill="black",width=2)
                                canvas.create_line(210,175,1090,175,fill="black",width=2)
                                canvas.create_line(210,220,1090,220,fill="black",width=2)
                                canvas.create_line(210,265,1090,265,fill="black",width=2)
                                canvas.create_line(210,300,1090,300,fill="black",width=2)
                                canvas.create_line(210,340,1090,340,fill="black",width=2)
                                #canvas.create_line(60,415,940,415,fill="black",width=2)
                                #canvas.create_line(60,455,940,455,fill="black",width=2)
                                canvas.create_line(210,465,1090,465,fill="black",width=2)
                                canvas.create_line(210,500,1090,500,fill="black",width=2)
                                #canvas.create_line(60,535,940,575,fill="black",width=2)
                                canvas.create_line(410,420,410,540,fill="black",width=2)
                                canvas.create_line(850,420,850,540,fill="black",width=2)
                                canvas.create_line(650,420,650,540,fill="black",width=2)
                                canvas.create_text(550,390,text="Shipment Status",fill="#ff0000",font=('calibri(body)', 15, 'bold'),anchor=NW)
                                canvas.create_text(230,110,text="Booking Date",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,150,text="Courier_Id",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,150,text="Invoice Price",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,190,text="Sender Name",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,230,text="Address Info",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,270,text="Mobile no.",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,310,text="Mode Of Payment",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,310,text="Shipment Type",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW) 
                                canvas.create_text(230,350,text="Total Weight (gm)",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,350,text="Total freight",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)         
                                canvas.create_text(690,190,text="Receiver Name",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,230,text="Address Info",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,270,text="Mobile no.",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,150,text="",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,110,text="Delivery Expected",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(230,430,text="Updated On",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(430,430,text="Location",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(690,430,text="Current Status",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                canvas.create_text(890,430,text="Remarks",fill="#ff0000",font=('calibri(body)', 10, 'bold'),anchor=NW)
                                btn2=Button(canvas,text="Track Again",width=12,command=track)
                                canvas.create_window(650,590,window=btn2)
                                canvas.create_text(230,470,text=update1,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(230,510,text=update2,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(430,470,text=loc1,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(430,510,text=loc2,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(690,470,text=cs,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(690,510,text=cs2,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                                canvas.create_text(870,470,text=rem,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                                canvas.create_text(870,510,text=rem2,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                                canvas.create_text(870,110,text=del_ex,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        canvas.create_text(430,110,text=b_date,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(430,150,text=track_id,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(870,150,text=ip,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(430,190,text=s_name,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(430,230,text=s_add,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(430,270,text=s_phone,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(870,190,text=r_name,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(870,230,text=r_add,fill="black",font=('calibri(body)', 12, 'italic'),anchor=NW)
                        canvas.create_text(870,270,text=r_phone,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        canvas.create_text(430,310,text=mo,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        canvas.create_text(870,310,text=st,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        canvas.create_text(430,350,text=weight,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        canvas.create_text(870,350,text=price,fill="black",font=('calibri(body)',12, 'italic'),anchor=NW)
                        
                        return
         messagebox.showerror("tracking failed","Invalid track")
         track()
         
    
##############################################********************ABOUT US**********************#####################################################################
    
def goto_about(event):
    global root
    global canvas
    canvas.delete("all")
    about()



def about():
    global root
    global canvas
    global menu
    global gif3
    global img1
    global img
    global ham
    global gif4
    global log
    global y
    global menuh
    menuh=[]
    menu=[]
    y=0
    #canvas=Canvas(root,width=1366,height=680)
    
   # canvas.pack()
                    ##1e90ff
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    

    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)

    canvas.create_rectangle(150,110,1150,650,outline="orange",width=1,fill="white")
    canvas.create_line(740,140,740,620,fill="orange",width=1)
   

    canvas.create_text(160,60,text="Welcome to courier management service",fill="orange",font=('Georgia',32, 'bold'),anchor=NW)
    canvas.create_text(160,130,text="As a customer-driven company, CMS is dedicated to understanding and ",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,150,text="fulfilling customers’ needs and whatever it takes to provide customers with  ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,170,text="the highest level of reliability and service quality.",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,195,text="The Technological Advantage-What sets CMS apart from other courier ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,225,text="companies is our extensive use of information technology and we assure our ",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,245,text="customers timely fulfillments and customer-recipient satisfaction.",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,265,text="We have about 600 Branches and Agencies of business service stations ",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,285,text="all over Bangladesh and Malaysia.",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,320,text="We manage the delivery and distribution for a rapidly expanding list of our",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,340,text="active clients consisting of Individuals, Government offices, foreign ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,360,text="National & Multinational Mobile Companies,Corporations, Banks, and ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,380,text="Insurance & organizations, leasing companies, Industries, Pharmaceuticals etc.",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,415,text="We have information system that allows us to obtain customer data & ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,435,text="delivery status. Our fleet-Our vehicle resources range from vans to trucks.",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,470,text="Because we believe in long-term business relationship we maintain fair ",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,490,text="prices with consistently fast, reliable and efficient service. By listing to ",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,510,text="our customers needs,we have put together a wide range of delivery solutions ",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,530,text="to suit your needs.",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,565,text="CMS is committed to quality practices and focusing on competing against or ",fill="black",font=('Georgia', 12, 'italic'),anchor=NW)
    canvas.create_text(160,585,text="collaborating with the very best service in courier field.",fill="black",font=('Georgia',12, 'italic'),anchor=NW)
    canvas.create_text(160,620,text="CMS has maintained certain criteria of excellence.",fill="black",font=('Georgia',12, 'italic'),anchor=NW)   
    img=PhotoImage(file="ab1.gif")
    canvas.create_image(780,140,image=img,anchor=NW)
    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15,5, image = gif3, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")

    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()





######################################################################********order*********##########################################################################
def goto_order(event):
    global root
    global canvas
    canvas.delete("all")
    #root.destroy()
    order()
    
def order():
    global root
    global canvas
    global sname
    global sloc
    global semail
    global smob
    global sadd
    global spin
    global sstate
    global scity
    global spcode
    global menu
    global img1
    global img
    global gif3
    global ham
    global y
    global uname
    global menuh
    global ip
   
    menuh=[]
    menu=[]
    y=0
   
    img=PhotoImage(file="plain1.gif")
    canvas.create_image(0,0,image=img,anchor=NW)
   
    root.title("welcome to order")
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))

    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)
    
    #canvas.create_rectangle(475,135,890,645,outline="#1e90ff",width=3)

    #imgs=PhotoImage(file="userss.gif")
    #canvas.create_image(620,70,image=imgs,anchor=NW)
    #canvas.pack()

    canvas.create_text(680,80,text="Give an Order",fill="#1e90ff",font=('calibri(body)', 30, 'italic'))
    canvas.create_rectangle(60,135,410,620,outline="black",width=2,fill="white")
    
    canvas.create_text(220,160,text="Sender Info",fill="#1e90ff",font=('calibri(body)', 16, 'italic'))
    
    canvas.create_text(80,200,text="Your Name",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,210,window=sname)

    canvas.create_text(80,250,text="country/location",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sloc=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,260,window=sloc)
    
    canvas.create_text(80,300,text="Address",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sadd=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,310,window=sadd)

    canvas.create_text(80,350,text="City",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    scity=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,360,window=scity)

    canvas.create_text(80,400,text="State",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sstate=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,410,window=sstate)
    
    canvas.create_text(80,550,text="E-mail",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    semail=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,560,window=semail)

    canvas.create_text(80,500,text="Mobile no.",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    smob=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,510,window=smob)


    canvas.create_text(80,450,text="pincode",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    spin=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,460,window=spin)

    btn=Button(canvas,text="continue",width=10,bg="#1e90ff",fg="white",command=receiver)
    canvas.create_window(230,600,window=btn)


    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15, 5, image = gif3, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")
    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()

#######################################################************receiver***************############################################################################
def receiver():
    global root
    global canvas
    global rname
    global rloc
    global remail
    global rmob
    global radd
    global rpin
    global rstate
    global rcity
    global rpcode
    global menu
    global img2
    global img
    global gif3
    global ham
    global y
    global uname
    global menuh
    menuh=[]
    menu=[]
    y=0
    canvas.delete("all")
    img2=PhotoImage(file="plain1.gif")
    canvas.create_image(0,0,image=img2,anchor=NW)
    root.title("welcome to account")
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,510,45,fill="black",width=1)
    canvas.create_line(640,0,620,45,fill="black",width=1)
    canvas.create_line(730,0,710,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))

    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)
    
    #canvas.create_rectangle(475,135,890,645,outline="#1e90ff",width=3)

    #imgs=PhotoImage(file="userss.gif")
    #canvas.create_image(620,70,image=imgs,anchor=NW)
    #canvas.pack()

    canvas.create_text(680,80,text="Give an Order",fill="#1e90ff",font=('calibri(body)', 30, 'italic'))
    canvas.create_rectangle(60,135,410,620,outline="black",width=2,fill="white")
    
    canvas.create_text(220,160,text="Receiver Info",fill="#1e90ff",font=('calibri(body)', 16, 'italic'))
    
    canvas.create_text(80,200,text="Your Name",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,210,window=rname)

    canvas.create_text(80,250,text="country/location",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rloc=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,260,window=rloc)
    
    canvas.create_text(80,300,text="Address",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    radd=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,310,window=radd)

    canvas.create_text(80,350,text="City",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rcity=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,360,window=rcity)

    canvas.create_text(80,400,text="State",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rstate=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,410,window=rstate)
    
    canvas.create_text(80,550,text="E-mail",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    remail=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,560,window=remail)

    canvas.create_text(80,500,text="Mobile no.",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rmob=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,510,window=rmob)


    canvas.create_text(80,450,text="pincode",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    rpin=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,460,window=rpin)

    btn2=Button(canvas,text="continue",width=10,bg="#1e90ff",fg="white",command=courier)
    canvas.create_window(230,600,window=btn2)


    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15, 5, image = gif3, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")
    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()

######################################################*************courier***************#############################################################################
def courier():
    global root
    global canvas
    global weight
    global length
    global width
    global price
    global radd
    global rpin
    global sp
    global st
    global mo
    global menu
    global img2
    global img
    global gif3
    global ham
    global y
    global uname
    global menuh
    global sdate
    global ip
    menuh=[]
    menu=[]
    y=0
    canvas.delete("all")
    img2=PhotoImage(file="plain1.gif")
    a=canvas.create_image(0,0,image=img2,anchor=NW)
    root.title("welcome to account")
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))

    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menuh[5],'<Enter>',contact)
    
    #canvas.create_rectangle(475,135,890,645,outline="#1e90ff",width=3)

    #imgs=PhotoImage(file="userss.gif")
    #canvas.create_image(620,70,image=imgs,anchor=NW)
    #canvas.pack()

    canvas.create_text(680,80,text="Give an Order",fill="#1e90ff",font=('calibri(body)', 30, 'italic'))
    canvas.create_rectangle(60,135,410,670,outline="#1e90ff",width=2,fill="white")
    
    a=canvas.create_text(220,160,text="Courier Info",fill="#1e90ff",font=('calibri(body)', 16, 'italic'))

    canvas.create_text(70,200,text="courier width",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sfname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,210,window=sfname)

    canvas.create_text(70,250,text="courier length",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    slname=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,260,window=slname)
        
    canvas.create_text(70,300,text="courier weight(gm)",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    weight=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,310,window=weight)

    v=IntVar()
    rb=Radiobutton(root,text="Documents", variable=v,value=1,bg="white",fg="black",font=('Georgia', 10, 'italic'))
    canvas.create_window(160,370,window=rb)
    rb2=Radiobutton(root,text="Products",variable=v, value=2,bg="white",fg="black",font=('Georgia', 10, 'italic'))
    canvas.create_window(290,370,window=rb2)
    canvas.create_text(70,330,text="courier contents : ",fill="black",font=('Georgia',12, 'bold'),anchor=NW)

    canvas.create_text(70,400,text="Invoice price",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    ip=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,410,window=ip)

    canvas.create_text(70,450,text="Shiping Date",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sdate=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,460,window=sdate)    

    canvas.create_text(70,500,text="Shipment Purpose",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    sp=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,510,window=sp)

    canvas.create_text(70,550,text="Shipment Type",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    st=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,560,window=st)

    canvas.create_text(70,600,text="Mode Of Payment",fill="black",font=('Georgia', 12, 'bold'),anchor=NW)
    mo=Entry(canvas,bg="white",bd=2,font=('calibri(body)',10, 'italic'))
    canvas.create_window(320,610,window=mo)

    
    btn=Button(canvas,text="order",width=10,bg="#1e90ff",fg="white",command=order_Fed)
    canvas.create_window(230,650,window=btn)


    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15, 5, image = gif3, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")
    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

    canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()

def order_Fed():
     global sdate
     global rname
     global rmob
     global radd
     global weight
     global sname
     global smob
     global sadd
     global st
     global mo
     global ip
     global lastline
     track=0
     with open(credss,'r') as inf:
         myfile=inf.readlines()
         lastline=myfile[-1].split()
         track=int(lastline[0])
         w=int(weight.get())
         price=((w/100)*2)
         messagebox.showinfo("order successfull","order placed, your tracking id is "+str(track+1)+" and your total price is "+str(price))
     with open(credss,'a') as g:
        g.write(str(track+1)+' ')
        g.write(sdate.get())
        g.write(" ")
        g.write(sname.get())
        g.write(" ")
        g.write(sadd.get())
        g.write(" ")
        g.write(smob.get())
        g.write(" ")
        g.write(rname.get())
        g.write(" ")
        g.write(radd.get())
        g.write(" ")
        g.write(rmob.get())
        g.write(" ")
        g.write(str(weight.get()))
        g.write(" ")
        g.write(st.get())
        g.write(" ")
        g.write(mo.get())
        g.write(" ")
        g.write(ip.get())
        g.write(" ")
        g.write(str(price))
        g.write("\n")
        canvas.delete("all")
        order()
        

######################################******************************Profile**********************************###########################################################
def go_pro(event):
    global root
    global canvas
    canvas.delete("all")
    #root.destroy()
    Profile()

def Profile():
    global root
    global canvas
    global img2
    global imgwgt
    global ham
    global y
    global menuh
    global menu
    global user
    global name
    global img1
    with open(ac,'r') as s:
        #img2=PhotoImage(file="a.gif")
        #canvas.create_image(0,0,image=img2,anchor=NW)
        #a='sachin'
        data=s.readlines()
        for i in range(len(data)):
            print(data[i])
            usern,fname,lname,email,mob,add,city,pin=data[i].split()
            if  usern==user:
                print(data[i])
                img=PhotoImage(file="images.gif")
                imgwgt=canvas.create_image(550,30,image=img,anchor=NW)
                y=0
                menuh=[]
                canvas.create_rectangle(10,580,1350,680,outline="white",width=1,fill="white")                ##1e90ff
                canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
                canvas.create_line(60,0,60,45,fill="black",width=1)
                canvas.create_line(150,0,150,45,fill="black",width=1)
                canvas.create_line(240,0,240,45,fill="black",width=1)
                canvas.create_line(330,0,330,45,fill="black",width=1)
                canvas.create_line(420,0,420,45,fill="black",width=1)
                canvas.create_line(530,0,530,45,fill="black",width=1)
                canvas.create_line(640,0,640,45,fill="black",width=1)
                canvas.create_line(730,0,730,45,fill="black",width=1)           
                canvas.create_line(1270,0,1270,45,fill="black",width=1)
                #canvas.create_line(1340,0,1340,45,fill="black",width=1)
                menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
                canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
                canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
                canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
                canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
                canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
                canvas.tag_bind(menuh[4], '<ButtonPress-1>',goto_feedback)
                canvas.tag_bind(menuh[5],'<Enter>',contact)
                
                canvas.create_text(570,220,text="Hello "+user,fill="blue",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(240,300,text="Custmer Name",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(240,350,text=fname,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                canvas.create_text(320,350,text=lname,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                canvas.create_text(600,300,text="Mobile_no",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(600,350,text=mob,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)

                canvas.create_text(900,300,text="Pincode",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(900,350,text=pin,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                
                #canvas.create_text(140,205,text="Custmer Name",fill="#ff0000",font=('calibri(body)', 20, 'italic'),anchor=NW)
                
                canvas.create_text(240,450,text="E-mail",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(240,500,text=email,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                canvas.create_text(600,450,text="Address",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(600,500,text=add,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                canvas.create_text(900,450,text="City",fill="#ff0000",font=('calibri(body)', 24, 'italic'),anchor=NW)
                canvas.create_text(900,500,text=city,fill="black",font=('calibri(body)', 18, 'italic'),anchor=NW)
                menu=[]
                gif3=PhotoImage(file = "images3.gif")
                ham=canvas.create_image(15,5, image = gif3, anchor = NW)
                #gif4=PhotoImage(file = "do.gif")
                #log=canvas.create_image(1100, 30, image = gif4, anchor = NW)
                menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
                img1=PhotoImage(file="users.gif")

                menu.append(canvas.create_image(-100,80,image=img1))
                menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
                menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
                menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="red",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,310,text="feedback" ,fill="#000",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
                menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))

                canvas.tag_bind(menu[10], '<ButtonPress-1>',quito)
                canvas.tag_bind(menu[8], '<ButtonPress-1>',goto_about)
                canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
                canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
                canvas.tag_bind(menu[9], '<ButtonPress-1>',logout)
                canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
                canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
                canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
                canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
                root.mainloop()
############################################*******************************Feedback************************############################################################


def goto_feedback(event):
    global root
    global canvas
    canvas.delete("all")
    #root.destroy()
    feedback()
def save():
    global fedo
    global do
    with open(saves,'a') as f:
        f.write(fedo.get())
        f.write("\n")
        messagebox.showinfo("Feedback","feedback submitted successfully")
        
    

def feedback():
    global menuh
    global rb
    global rb2
    global rb3
    global rb4
    global rb5
    global img2
    global img3
    global img
    global ham
    global menu
    global gif3
    global fedo
    menuh=[]               ##1e90ff
    img2=PhotoImage(file="a.gif")
    canvas.create_image(0,0,image=img2,anchor=NW)
    
    img=PhotoImage(file="Whats.gif")
    canvas.create_image(850,170,image=img,anchor=NW)
    img3=PhotoImage(file="images50.gif")
    canvas.create_image(1150,50,image=img3,anchor=NW)
    #canvas.create_rectangle(200,60,900,680,outline="black",width=1,fill="white")
    canvas.create_rectangle(2,0,1356,45,outline="black",width=1,fill="blue")
    canvas.create_line(60,0,60,45,fill="black",width=1)
    canvas.create_line(150,0,150,45,fill="black",width=1)
    canvas.create_line(240,0,240,45,fill="black",width=1)
    canvas.create_line(330,0,330,45,fill="black",width=1)
    canvas.create_line(420,0,420,45,fill="black",width=1)
    canvas.create_line(530,0,530,45,fill="black",width=1)
    canvas.create_line(640,0,640,45,fill="black",width=1)
    canvas.create_line(730,0,730,45,fill="black",width=1)           
    canvas.create_line(1270,0,1270,45,fill="black",width=1)
    #canvas.create_line(1340,0,1340,45,fill="black",width=1)
    menuh.append(canvas.create_text(80,15,text="Home",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(170,15,text="Profile",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(260,15,text="Order",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(350,15,text="Track",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(440,15,text="Feedback",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(540,15,text="Contact us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(650,15,text="About us",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    menuh.append(canvas.create_text(1290,15,text="logout",fill="white",font=('Georgia', 12, 'bold'),anchor=NW))
    canvas.tag_bind(menuh[7], '<ButtonPress-1>',logout)
    canvas.tag_bind(menuh[6], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menuh[2], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menuh[0], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menuh[3], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menuh[1], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(menuh[5],'<Enter>',contact)
    
    
    canvas.create_text(90,80,text="Give Feedback",fill="blue",font=('Georgia', 30, 'bold'),anchor=NW)
    canvas.create_text(90,150,text="Overall,how did you feel about the service you recived today?",fill="black",font=('Georgia', 18, 'bold'),anchor=NW)
    v=IntVar()
    rb=Radiobutton(root,text="Very Satisfied", variable=v,value=1,bg="white",fg="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_window(170,200,window=rb)
    rb2=Radiobutton(root,text="Satisfied",variable=v, value=2,bg="white",fg="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_window(145,230,window=rb2)
    rb3=Radiobutton(root,text="Neither Satisfied", variable=v,value=3,bg="white",fg="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_window(180,260,window=rb3)
    rb4=Radiobutton(root,text="dissatisfied",variable=v, value=4,bg="white",fg="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_window(157,290,window=rb4)
    rb5=Radiobutton(root,text="Very dissatisfied",variable=v, value=5,bg="white",fg="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_window(180,320,window=rb5)
    canvas.create_text(90,350,text="How could we improve this service?",fill="black",font=('Georgia', 18, 'bold'),anchor=NW)
    #fed=Entry(canvas,bg="white",bd=3,font=('calibri(body)',50, 'italic'))
    #canvas.create_window(460,440,window=fed)

    canvas.create_rectangle(83,385,700,480,outline="black",width=1,fill="white")
    fedo=Entry(canvas,bg="white",bd=0,width=55,font=('calibri(body)',15, 'italic'))
    canvas.create_window(390,400,window=fedo)
    canvas.create_text(90,480,text="(Limit is 1200 character)",fill="black",font=('Georgia', 14, 'italic'),anchor=NW)
    canvas.create_text(90,520,text="Please don't include any personal or financial information,for example ",fill="black",font=('Georgia', 15, 'italic'),anchor=NW)
    canvas.create_text(90,540,text="your national insaurance & credit card details etc.",fill="black",font=('Georgia', 15, 'italic'),anchor=NW)
    btn=Button(canvas,text="Send feedback",font=('Georgia', 12, 'bold'),bg="#1e90ff",fg="white",command=save)
    canvas.create_window(150,620,window=btn)
    menu=[]
    gif3=PhotoImage(file = "images3.gif")
    ham=canvas.create_image(15,5, image = gif3, anchor = NW)
    #gif4=PhotoImage(file = "do.gif")
    #log=canvas.create_image(1100, 30, image = gif4, anchor = NW)
    menu.append(canvas.create_rectangle(-320,0,0,768,fill="white"))
    img1=PhotoImage(file="users.gif")

    menu.append(canvas.create_image(-100,80,image=img1))
    menu.append(canvas.create_text(-100,170,text="Hello "+user+',' ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,190,text="Home" ,fill="#000",font=("segoe print",10,'bold')))
    menu.append(canvas.create_text(-100,220,text="My Profile" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,250,text="New Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,280,text="Tracking Order" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,310,text="feedback" ,fill="red",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,340,text="About us" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,370,text="Logout" ,fill="#000",font=("STENCIL",10)))
    menu.append(canvas.create_text(-100,400,text="Quit" ,fill="#000",font=("STENCIL",10)))
    canvas.tag_bind(menu[9], '<ButtonPress-1>',quito)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_about)
    canvas.tag_bind(menu[6], '<ButtonPress-1>',goto_track)
    canvas.tag_bind(menu[5], '<ButtonPress-1>',goto_order)
    canvas.tag_bind(menu[8], '<ButtonPress-1>',logout)
    canvas.tag_bind(menu[3], '<ButtonPress-1>',callhome)
    canvas.tag_bind(menu[7], '<ButtonPress-1>',goto_feedback)
    canvas.tag_bind(menu[4], '<ButtonPress-1>',go_pro)
    canvas.tag_bind(ham, '<ButtonPress-1>',movemenu)
    root.mainloop()
s=0
def contact(event):
    global canvas
    global root
    global a
    global b
    global menuh
    global p
    global b
    global s
    global q
    p=canvas.create_rectangle(530,45,680,75,outline="black",width=1,fill="white")
    q=canvas.create_rectangle(530,75,680,110,outline="black",width=1,fill="white")
    a=canvas.create_text(540,50,text="+91-7737363498",fill="black",font=('calibri(body)', 12, 'bold'),anchor=NW)
    b=canvas.create_text(540,80,text="+91-9079983701",fill="black",font=('calibri(body)', 12, 'bold'),anchor=NW)
    canvas.tag_bind(a,'<Enter>',lambda ebt,temp=0:change_color(ebt,temp))
    canvas.tag_bind(a,'<Leave>',lambda ebt,temp=0:leave1(ebt,temp))
    canvas.tag_bind(b,'<Enter>',lambda ebt,temp=1:change_color(ebt,temp))
    canvas.tag_bind(b,'<Leave>',lambda ebt,temp=1:leave1(ebt,temp))
    canvas.tag_bind(b,'<Leave>',leave)
    
        
    
def leave(event):
    global a
    global b
    global p
    global q
    canvas.delete(p,a,b,q)
    


def leave1(event,text):
     global a
     global b
     if text==0:
         canvas.itemconfig(a,fill="#000")
         canvas.itemconfig(p,fill="white")
         
     elif text==1:
         canvas.itemconfig(b,fill="#000")
         canvas.itemconfig(q,fill="white")
        
def change_color(event,text):
    global a
    global b
    global p
    global q
    if text==0:
        canvas.itemconfig(a,fill="white")
        canvas.itemconfig(p,fill="red")
    elif text==1:
        canvas.itemconfig(b,fill="white")
        canvas.itemconfig(q,fill="red")

login()










