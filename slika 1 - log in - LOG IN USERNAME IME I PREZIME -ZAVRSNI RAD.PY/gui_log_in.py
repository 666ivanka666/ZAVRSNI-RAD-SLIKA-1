import ctypes
import tkinter as tk
from tkinter import messagebox
from crud import get_all_users
from datetime_utils import *
from weather_api import WeatherForecast
from main import session

root = tk.Tk()
root.title('Algebra | PyPosuda')
root.geometry('400x300')
root.configure(bg='#282828') 

def login():
    username ='ivanka'
    password ='666'
    ime = 'ivanka'
    prezime = 'budimir'
    if username_entry.get() == username and password_entry.get() == password and ime_entry.get() == ime and prezime_entry.get() == prezime:
        messagebox.showinfo(title='Successful login', message='You logged in sucessfuly')
    else:
        messagebox.showinfo(title='Error', message='Invalid login')


frame=tk.Frame(bg='#282828',width=800, height=600)
#login
login_label=tk.Label(frame, text='Login',bg='#282828', fg='white',font=('Arial', 12))
login_label.grid(row=0,column=0, columnspan=2, pady=10)
#username
username_label=tk.Label(frame, text= 'User name',bg='#282828',fg='white',font='Arial')
username_label.grid(row=1,column=0)

username_entry = tk.Entry(frame,font=('Arial, 8'))
username_entry.grid(row=1,column=1, pady= 5)
#password
password_entry = tk.Entry(frame, show='*',font=('Arial, 8'))
password_entry.grid(row=2,column=1, pady= 5)

password_label=tk. Label(frame, text= 'Password',bg='#282828',fg='white',font='Arial')
password_label.grid(row=2,column=0)

password_label=tk. Label(frame, text= 'Password',bg='#282828',fg='white',font='Arial')
password_label.grid(row=2,column=0)


# ime
ime_label=tk.Label(frame, text= 'Ime',bg='#282828',fg='white',font='Arial')
ime_label.grid(row=3,column=0)

ime_entry = tk.Entry(frame,font=('Arial, 8'))
ime_entry.grid(row=3,column=1, pady= 5)

#prezime
prezime_label=tk.Label(frame, text= 'Prezime',bg='#282828',fg='white',font='Arial')
prezime_label.grid(row=4,column=0)

prezime_entry = tk.Entry(frame,font=('Arial, 8'))
prezime_entry.grid(row=4,column=1, pady= 5)

#log in button
login_button=tk.Button(frame, text='Login',bg='grey',fg='white',font=('Arial, 10'), command=login)
login_button.grid(row=6,column=0,columnspan=2,pady=10)


frame.pack()
root.mainloop()