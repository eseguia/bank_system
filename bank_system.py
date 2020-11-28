from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import os

#class User():
#    def __init__(self,name,age,gender):
#        self.name = name
#        self.age = age
#        self.gender = gender
#    def show_details(self):
#        print(f'Account Details\nName: {self.name}\nAge: {self.age}\nGender: ${self.gender}')

#class Bank(User):
#    def __init__(self,name,age,gender):
#        super().__init__(name,age,gender)
#        self.balance = 0
#    def deposit(self,value):
#        self.value = value
#        self.balance += value
#    def withdraw(self,value):
#        self.value = value
#        if value > self.balance:
#            print(f'Not enough funds! Balance available: {self.balance}')
#        else:
#            self.balance -= value
#    def view_balance(self):
#        print(f'Account balance: ${self.balance}')

def save_register():
    name, age, gender, password, email = t_name.get(), t_age.get(), t_gender.get(), t_password.get(), t_email.get()
    all_files = os.listdir()
    if name == '' or age == '' or gender == '' or password == '' or email == '':
        tk.messagebox.showinfo(message="All fields are required", title="Missing Information")
        return
    for n in all_files:
        if name+'.txt' == n:
            tk.messagebox.showinfo(message="User already exists", title="Existing User")     #### doesn't break the for loop  and overwrites the file
            break
        else:
            new_user = open(f'{name}.txt', 'w')
            inicial_balance = 0
            new_user.write(f'{name}\n{age}\n{gender}\n{email}\n{password}\n{inicial_balance}')
            new_user.close()

def register():
    global t_name, t_age, t_gender, t_password, t_email
    t_name, t_age, t_gender, t_password,t_email = StringVar(), StringVar(), StringVar(), StringVar(),StringVar()

    register_window = Toplevel(root)
    register_window.resizable(False,False)
    register_window.geometry("350x400+750+370")
    register_window.title('Register')
    register_window.iconbitmap('eguia_bank_icon.ico')
    canvas = tk.Canvas(register_window, height = 300, width = 350,bg = '#DD6600').pack()
    register_background = tk.PhotoImage(file='root_background1.png')
    background = tk.Label(register_window, image = root_background)
    background.place(relwidth=1,relheight=1)

    tk.Frame(register_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=370)
    tk.Label(register_window, text = 'Enter your details to register', font = 'Calibri 14',bg = '#FFD0AB').place(x=50,y=30,width=250,height=30)
    tk.Label(register_window, text = 'Name', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=80,width=100,height=30)
    tk.Label(register_window, text = 'Age', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=130,width=100,height=30)
    tk.Label(register_window, text = 'Gender', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=180,width=100,height=30)
    tk.Label(register_window, text = 'Password', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=230,width=100,height=30)
    tk.Label(register_window, text = 'Email', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=280,width=100,height=30)

    entry_name = tk.Entry(register_window, bd=1,textvariable = t_name)
    entry_age = tk.Entry(register_window, bd=1,textvariable = t_age)
    entry_gender = tk.Entry(register_window, bd=1,textvariable = t_gender)
    entry_password = tk.Entry(register_window, bd=1, show = '*',textvariable = t_password)
    entry_email = tk.Entry(register_window, bd=1,textvariable = t_email)
    entry_name.place(x=160,y=85,width=135,height=20)
    entry_age.place(x=160,y=135,width=135,height=20)
    entry_gender.place(x=160,y=185,width=135,height=20)
    entry_password.place(x=160,y=235,width=135,height=20)
    entry_email.place(x=160,y=285,width=135,height=20)

    tk.Button(register_window, text = 'Register',bg = '#FFD0AB',font = 'Calibri 14', command = save_register).place(x=125,y=340,width=100,height=40)

def login():
    global l_name,l_password, login_window
    l_name, l_password = StringVar(), StringVar()
    login_window = Toplevel(root)
    login_window.resizable(False,False)
    login_window.geometry("350x300+750+370")
    login_window.title('Register')
    login_window.iconbitmap('eguia_bank_icon.ico')
    canvas = tk.Canvas(login_window, height = 300, width = 350,bg = '#DD6600').pack()
    background = tk.Label(login_window, image = root_background)
    background.place(relwidth=1,relheight=1)
    tk.Frame(login_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
    tk.Label(login_window, text = 'Enter your details to login', font = 'Calibri 14',bg = '#FFD0AB').place(x=50,y=30,width=250,height=30)
    tk.Label(login_window, text = 'Name', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=80,width=100,height=30)
    tk.Label(login_window, text = 'Password', font = 'Calibri 13',bg = '#FFF1E6').place(x=55,y=130,width=100,height=30)

    login_name = tk.Entry(login_window, bd=1,textvariable = l_name)
    login_password = tk.Entry(login_window, bd=1,textvariable = l_password, show = '*')
    login_name.place(x=160,y=85,width=130,height=20)
    login_password.place(x=160,y=135,width=130,height=20)

    tk.Button(login_window, text = 'Login', bg = '#FFD0AB',font = 'Calibri 14',command = enter_session).place(x=110,y=200,width=130,height=30)

def go_back():
    data_window.destroy()
def go_back_d():
    deposit_window.destroy() 
def go_back_w():
    withdraw_window.destroy()

def deposit():
     global deposit_window, amount,current_balance_label
     amount = StringVar()
     with open(f'{name}.txt','r+') as f:
        view_deposit = f.read()
        vdep = view_deposit.split('\n')
        deposit_window = Toplevel(dashboard_window)
        deposit_window.resizable(False,False)
        deposit_window.title('Deposit')
        deposit_window.iconbitmap('eguia_bank_icon.ico')
        deposit_window.geometry("350x300+750+370")
        canvas = tk.Canvas(deposit_window, height = 300, width = 350,bg = '#DD6600').pack()
        background = tk.Label(deposit_window, image = root_background)
        background.place(relwidth=1,relheight=1)
        tk.Frame(deposit_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
        tk.Label(deposit_window, text = 'Deposit Amount',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=40,width=250,height=30)
        entry_deposit = tk.Entry(deposit_window,textvariable = amount, font = 'Calibri 14')
        entry_deposit.place(x=130,y=100,width=90,height=25)
        current_balance_label = tk.Label(deposit_window, text = f'Current Balance: ${vdep[5]}',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=140,width=250,height=30)
        tk.Button(deposit_window, text = 'Deposit',bg = '#FFD0AB',font = 'Calibri 14',command = end_deposit).place(x=100,y=180,width=150,height=25)
        tk.Button(deposit_window, text = 'Go back',bg = '#FFD0AB',font = 'Calibri 14',command = go_back_d).place(x=100,y=250,width=150,height=25)

def end_deposit():
    value = amount.get()
    if value == '':
        tk.Label(deposit_window, text = 'Need to enter a valid amount',bg = '#FFD0AB',font = 'Calibri 14', fg = 'red').place(x=50,y=215,width=250,height=30)
        return
    value = float(value)
    if value<=0:
        tk.Label(deposit_window, text = 'Can not deposit negative values',bg = '#FFD0AB',font = 'Calibri 14', fg = 'red').place(x=50,y=215,width=250,height=30)
        return
    with open(f'{name}.txt','r+') as f:
        view_deposit = f.read()
        vdep = view_deposit.split('\n')
        current_balance = vdep[5]
        updated_balance = current_balance
        updated_balance = round(float(updated_balance) + float(value),2)
        view_deposit = view_deposit.replace(current_balance, str(updated_balance))
        f.seek(0)
        f.truncate(0)
        f.write(view_deposit)
        f.close()

        current_balance_label = tk.Label(deposit_window, text = f'Current Balance: ${str(updated_balance)}',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=140,width=250,height=30)
        tk.Label(deposit_window, text = '',bg = '#FFF1E6',font = 'Calibri 14').place(x=50,y=215,width=250,height=30)

def withdraw():
     global withdraw_window, withdraw_amount,current_balance_label
     withdraw_amount = StringVar()
     with open(f'{name}.txt','r+') as f:
        view_deposit = f.read()
        vdep = view_deposit.split('\n')
        withdraw_window = Toplevel(dashboard_window)
        withdraw_window.resizable(False,False)
        withdraw_window.title('Withdraw')
        withdraw_window.iconbitmap('eguia_bank_icon.ico')
        withdraw_window.geometry("350x300+750+370")
        canvas = tk.Canvas(withdraw_window, height = 300, width = 350,bg = '#DD6600').pack()
        background = tk.Label(withdraw_window, image = root_background)
        background.place(relwidth=1,relheight=1)
        tk.Frame(withdraw_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
        tk.Label(withdraw_window, text = 'Withdraw Amount',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=40,width=250,height=30)
        entry_withdraw = tk.Entry(withdraw_window,textvariable = withdraw_amount, font = 'Calibri 14')
        entry_withdraw.place(x=130,y=100,width=90,height=25)
        current_balance_label = tk.Label(withdraw_window, text = f'Current Balance: ${vdep[5]}',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=140,width=250,height=30)
        tk.Button(withdraw_window, text = 'Withdraw',bg = '#FFD0AB',font = 'Calibri 14',command =end_withdraw ).place(x=100,y=190,width=150,height=25)
        tk.Button(withdraw_window, text = 'Go back',bg = '#FFD0AB',font = 'Calibri 14',command = go_back_w).place(x=100,y=255,width=150,height=25)

def end_withdraw():
    value = withdraw_amount.get()
    if value == '':
        tk.Label(withdraw_window, text = 'Need to enter a valid amount',bg = '#FFD0AB',font = 'Calibri 13', fg = 'red').place(x=50,y=225,width=250,height=25)
        return
    #if type(value) == str:
        #tk.Label(withdraw_window, text = 'Do not enter a string',bg = '#FFD0AB',font = 'Calibri 13', fg = 'red').place(x=50,y=225,width=250,height=25) ### The entry numbers are also strings
        #return
    value = float(value)
    if value<=0:
        tk.Label(withdraw_window, text = 'Can not withdraw negative values',bg = '#FFD0AB',font = 'Calibri 13', fg = 'red').place(x=50,y=225,width=250,height=25)
        return
    with open(f'{name}.txt','r+') as f:
        view_withdraw = f.read()
        vdep = view_withdraw.split('\n')
        current_balance = vdep[5]
        if value > float(vdep[5]):
            tk.Label(withdraw_window, text = 'Not enough funds',bg = '#FFD0AB',font = 'Calibri 13', fg = 'red').place(x=50,y=225,width=250,height=25)
            return
        updated_balance = current_balance
        updated_balance = round(float(updated_balance) - float(value),2)
        view_withdraw = view_withdraw.replace(current_balance, str(updated_balance))
        f.seek(0)
        f.truncate(0)
        f.write(view_withdraw)
        f.close()

        current_balance_label = tk.Label(withdraw_window, text = f'Current Balance: ${str(updated_balance)}',bg = '#FFD0AB',font = 'Calibri 14').place(x=50,y=140,width=250,height=30)
        tk.Label(withdraw_window, text = '',bg = '#FFF1E6',font = 'Calibri 14',).place(x=50,y=225,width=250,height=25)

def view_data():
    with open(f'{name}.txt', 'r') as f:
        view = f.read()
        view = view.split('\n')
        global data_window
        data_window = Toplevel(dashboard_window)
        data_window.resizable(False,False)
        data_window.title('Personal Information')
        data_window.iconbitmap('eguia_bank_icon.ico')
        data_window.geometry("350x300+750+370")
        canvas = tk.Canvas(data_window, height = 300, width = 350,bg = '#DD6600').pack()
        background = tk.Label(data_window, image = root_background)
        background.place(relwidth=1,relheight=1)
        tk.Frame(data_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
        tk.Label(data_window, text = 'Personal Information',bg = '#FFD0AB',font = 'Calibri 13').place(x=50,y=40,width=250,height=30)
        tk.Label(data_window, text = f'Name:  {view[0]}',bg = '#FFD0AB',font = 'Calibri 13').place(x=50,y=90,width=250,height=30)
        tk.Label(data_window, text = f'Age:  {view[1]}',bg = '#FFD0AB',font = 'Calibri 13').place(x=50,y=120,width=250,height=30)
        tk.Label(data_window, text = f'Gender:  {view[2]}',bg = '#FFD0AB',font = 'Calibri 13').place(x=50,y=150,width=250,height=30)
        tk.Label(data_window, text = f'Email:   {view[3]}',bg = '#FFD0AB',font = 'Calibri 13').place(x=50,y=180,width=250,height=30)
        tk.Label(data_window, text = f'Balance:   ${view[5]}',bg = '#FFD0AB',font = 'Calibri 13',fg = 'blue').place(x=50,y=210,width=250,height=30)
        tk.Button(data_window, text = 'Go Back',bg = '#FFD0AB',font = 'Calibri 14', command = go_back).place(x=50,y=250,width=250,height=30)

def exit():
    dashboard_window.destroy()
    root.destroy()

def enter_session():
    global name, dashboard_window
    name, password = l_name.get(), l_password.get()
    all_files = os.listdir()
    for file in all_files:
        if name+'.txt' == file:
            with open(f'{name}.txt', 'r') as f:
                check_login = f.read()
                check_login = check_login.split('\n')
                if password == check_login[4]:
                    login_window.destroy()
                    dashboard_window = Toplevel(root)
                    dashboard_window.resizable(False,False)
                    dashboard_window.title('Dashboard')
                    dashboard_window.iconbitmap('eguia_bank_icon.ico')
                    dashboard_window.geometry("350x300+750+370")
                    canvas = tk.Canvas(dashboard_window, height = 300, width = 350,bg = '#DD6600').pack()
                    background = tk.Label(dashboard_window, image = root_background)
                    background.place(relwidth=1,relheight=1)
                    tk.Frame(dashboard_window, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
                    tk.Label(dashboard_window, text = 'Welcome',font = 'Bold 16',bg = '#FFF1E6').place(x=75,y=25,width=200,height=25)
                    tk.Label(dashboard_window, text = f'{name}',font = 'Bold 16',bg = '#FFF1E6').place(x=75,y=50,width=200,height=25)
                    tk.Button(dashboard_window, text = 'Deposit',font = 'Calibri 14', bg = '#FFD0AB',command = deposit).place(x=110,y=100,width=130,height=30)
                    tk.Button(dashboard_window, text = 'Withdraw',font = 'Calibri 14', bg = '#FFD0AB',command = withdraw).place(x=110,y=145,width=130,height=30)
                    tk.Button(dashboard_window, text = 'View Personal Data',font = 'Calibri 14', bg = '#FFD0AB',command = view_data).place(x=85,y=190,width=180,height=30)
                    tk.Button(dashboard_window, text = 'Exit',font = 'Calibri 14', bg = '#FFD0AB',command = exit).place(x=135,y=250,width=80,height=30)
                    return
                else:
                    tk.Label(login_window, text = 'Wrong password', fg = 'red',font = 'Calibri 14',bg = '#FFF1E6').place(x=100,y=250,width=150,height=20)    
                    return
        else:
            tk.Label(login_window, text = 'User not found', fg = 'red',font = 'Calibri 14',bg = '#FFF1E6').place(x=107,y=250,width=136,height=20)
            

root = tk.Tk()
root.resizable(False,False)
root.title('Eguia Bank')
root.iconbitmap('eguia_bank_icon.ico')
root.geometry("350x300+750+370")
canvas = tk.Canvas(root, height = 300, width = 350,bg = '#DD6600').pack()
root_background = tk.PhotoImage(file='root_background1.png')
root_background= root_background.subsample(2, 2)
background = tk.Label(root, image = root_background)
background.place(relwidth=1,relheight=1)
frame = tk.Frame(root, bg = '#FFF1E6').place(x=50,y=15,width=250,height=270)
bank_name = ImageTk.PhotoImage(Image.open('eguia_bank_logo.png'))
display_bank_name = tk.Label(frame, image = bank_name,bg = '#FFF1E6').place(x=110,y=15)
label_bank = tk.Label(frame, text = 'Eguia Bank', font = 'Cambria 20',bg ='#FFF1E6', fg = '#E03F04').place(x=110,y=100)
label_slogan = tk.Label(frame, text = 'The most secure Bank you have used', font = 'Cambria 10',bg ='#FFF1E6').place(x=75,y=135)
button_register = tk.Button(frame,command = register,text = 'Register',font = 'Cambria 15',bg ='#FFDDDD').place(x=125,y=170,width=100,height=30)
button_login = tk.Button(frame,command = login, text = 'Login',font = 'Cambria 15',bg ='#FFDDDD').place(x=125,y=220,width=100,height=30)



root.mainloop()