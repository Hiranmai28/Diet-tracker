from tkinter import *
import csv
from datetime import datetime
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.tix import ButtonBox




# todo if calorie_sum > 1400: calorie_sum = RED
# todo save log to csv

base_path = "/Users/hiranmaidevarasetty/Downloads/DietTracker-Project/"

BLACK = "#191919"
GREY = "#30475e"
WHITE = "#e8e8e8"
FONT = ("Courier", 12, "bold")

daily_goal = 1800
calorie_sum = 0

window = Tk()
window.title("Diet Tracker")
window.config(bg=BLACK)


# Function to Add Calories
def add_calories(amount):
    global calorie_sum
    calorie_sum += amount
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def one_add():
    global calorie_sum
    calorie_sum += 1
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def ten_add():
    global calorie_sum
    calorie_sum += 10
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def fifty_add():
    global calorie_sum
    calorie_sum += 50
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def points_add():
    global calorie_sum
    calorie_sum += 100
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def two_add():
    global calorie_sum
    calorie_sum += 200
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def dosa_add():
    global calorie_sum
    calorie_sum += 35
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def idli_add():
    global calorie_sum
    calorie_sum += 370
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def greentea_add():
    global calorie_sum
    calorie_sum += 0
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def upma_add():
    global calorie_sum
    calorie_sum += 15
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def chapatti_add():
    global calorie_sum
    calorie_sum += 71
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def coffee_add():
    global calorie_sum
    calorie_sum += 35
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def kichdi_add():
    global calorie_sum
    calorie_sum += 15
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def Paneer_add():
    global calorie_sum
    calorie_sum += 15
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def rice_add():
    global calorie_sum
    calorie_sum += 206
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def dal_add():
    global calorie_sum
    calorie_sum += 124
    total_label.config(text=f"{calorie_sum}/{daily_goal}")

def check_sum():
    if calorie_sum > 1800:
      empty_label.config(text="Warning! You have crossed the calorie limit goal!!")
    elif calorie_sum < 1800:
      empty_label.config(text="You have not reached your goal yet!Keep Going!!")
    else :
      empty_label.config(text="Hurray!!! You have reached your daily goal!",fg='green')
      '''
def reset():
    total_label = IntVar(label)
    total_label.set(0)
    total_label.config(textvariable=total_label)      
  '''  

empty_label= Label(window,fg='red',font='Arial')
empty_label.grid(row=1,column=2,sticky=W)

btn=Button(window,text="SUBMIT",fg='WHITE',bg='BLACK',font='FONT',command=check_sum)
btn.grid(column=2,row=9)

def end_day():
    pass



def load_resized_image(image_path, width=250, height=300):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)  # Resize image
    return ImageTk.PhotoImage(img)


# heading
heading = Label(text="Diet Tracker", fg=WHITE, bg=BLACK, font=FONT)
heading.grid(column=1, row=0, columnspan=3)

# Total Calories Display
total_label = Label(text=f"0/{daily_goal}", fg=WHITE, bg=BLACK, font=FONT)
total_label.grid(column=1, row=4, columnspan=4)

one = Button(text="1", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=one_add)
one.grid(column=0, row=0)

ten = Button(text="10", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=ten_add)
ten.grid(column=1, row=0)

fifty = Button(text="50", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=fifty_add)
fifty.grid(column=2, row=0)

points_btn = Button(text="100", bg=BLACK, fg=WHITE, activebackground=GREY, command=points_add)
points_btn.grid(column=3, row=0)

two = Button(text="200", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=fifty_add)
two.grid(column=4, row=0)

dosa = load_resized_image(os.path.join(base_path, "Dosa_FIXED.png"))
upma = load_resized_image(os.path.join(base_path, "Upma_FIXED.png"))
idli = load_resized_image(os.path.join(base_path, "idli_FIXED.png"))
coffee = load_resized_image(os.path.join(base_path, "Coffee_FIXED.png"))
greentea = load_resized_image(os.path.join(base_path, "Green_FIXED.png"))
kichdi = load_resized_image(os.path.join(base_path, "Kichdi_FIXED.png"))
Paneer = load_resized_image(os.path.join(base_path, "Paneer_FIXED.png"))
rice = load_resized_image(os.path.join(base_path, "Rice_FIXED.png"))
Chapatti = load_resized_image(os.path.join(base_path, "Chapatti_FIXED.png"))
dal = load_resized_image(os.path.join(base_path, "Dal_FIXED.png"))



dosa_btn = Button(image=dosa, bg=BLACK, activebackground=GREY, command=dosa_add)
dosa_btn.image = dosa 
dosa_btn.grid(column=0, row=1)


upma_btn = Button(image=upma, bg=BLACK, activebackground=GREY, command=upma_add)
upma_btn.image = upma 
upma_btn.grid(column=1, row=1)


idli_btn = Button(image=idli, bg=BLACK, activebackground=GREY, command=idli_add)
idli_btn.image = idli
idli_btn.grid(column=2, row=1)


coffee_btn = Button(image=coffee, bg=BLACK, activebackground=GREY, command=coffee_add)
coffee_btn.image = coffee 
coffee_btn.grid(column=3, row=1)


greentea_btn = Button(image=greentea, bg=BLACK, activebackground=GREY, command=greentea_add)
greentea_btn.image = greentea 
greentea_btn.grid(column=4, row=1)


kichdi_btn = Button(image=kichdi, bg=BLACK, activebackground=GREY, command=kichdi_add)
kichdi_btn.image = kichdi 
kichdi_btn.grid(column=0, row=2)


Paneer_btn = Button(image=Paneer, bg=BLACK, activebackground=GREY, command=Paneer_add)
Paneer_btn.image =Paneer
Paneer_btn.grid(column=1, row=2)


rice_btn = Button(image=rice, bg=BLACK, activebackground=GREY, command=rice_add)
rice_btn.image = rice 
rice_btn.grid(column=2, row=2)


Chapatti_btn = Button(image=Chapatti, bg=BLACK, activebackground=GREY, command=chapatti_add)
Chapatti_btn.image = Chapatti 
Chapatti_btn.grid(column=3, row=2)


dal_btn = Button(image=dal, bg=BLACK, activebackground=GREY, command=dal_add)
dal_btn.image = dal 
dal_btn.grid(column=4, row=2)

# reset new day button (saves the previous day to csv)
'''
sun = PhotoImage(file="C:/Users/srchi/OneDrive/Desktop/GP/sun.png")
sun_btn = Button(image=sun, bg=BLACK, activebackground=GREY, command=end_day)
sun_btn.grid(column=2, row=0)
'''

window.mainloop()