from tkinter import *
import csv
from datetime import datetime
import os
from PIL import Image, ImageTk

# Base Path
base_path = "/Users/hiranmaidevarasetty/Downloads/DietTracker-Project/"

# Colors and Font
BLACK = "#f5f5f5"  # Changed to a lighter color for visibility
GREY = "#30475e"
WHITE = "#191919"
FONT = ("Courier", 14, "bold")

daily_goal = 1800
calorie_sum = 0

# Function to update calorie label and message
def update_calorie_label():
    global calorie_sum

    if calorie_sum == daily_goal:
        message = "🎉 Hurray! You made it!"
        total_label.config(fg="green")
    elif calorie_sum < daily_goal:
        message = "💪 Keep going!"
        total_label.config(fg="black")
    else:
        message = "⚠️ Stop eating much!"
        total_label.config(fg="red")

    total_label.config(text=f"{calorie_sum}/{daily_goal} - {message}")

# Submit function (logs calories and updates UI)
def submit():
    global calorie_sum
    with open("calorie_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), calorie_sum])

    # Update UI Labels
    confirmation_label.config(text="✅ Calories Logged Successfully!", fg="green")
    total_logged_label.config(text=f"📊 Total Calories: {calorie_sum}/{daily_goal}", fg="black")

    # Show Close button after submission
    close_button.grid(column=1, row=8, columnspan=3, pady=10)

# Reset function (Resets calorie count)
def reset():
    global calorie_sum
    calorie_sum = 0
    update_calorie_label()
    confirmation_label.config(text="")
    total_logged_label.config(text="")
    close_button.grid_remove()  # Hide Close button after reset

# Function to add calories
def add_calories(amount):
    global calorie_sum
    calorie_sum += amount
    update_calorie_label()

# Load and resize images (adjusted for better fit)
def load_resized_image(image_path, width=120, height=120):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# UI Setup
window = Tk()
window.title("Diet Tracker")
window.config(bg=BLACK)

# Heading
heading = Label(text="Diet Tracker", fg=WHITE, bg=BLACK, font=FONT)
heading.grid(column=1, row=0, columnspan=3, pady=5)

# Calorie Buttons
buttons = [("1", 1), ("10", 10), ("50", 50), ("100", 100)]
for i, (label, value) in enumerate(buttons):
    btn = Button(text=label, width=5, bg=WHITE, fg=BLACK, font=FONT, command=lambda v=value: add_calories(v))
    btn.grid(column=i, row=0, padx=5, pady=5)

# Load Food Images
foods = [
    ("Dosa", "Dosa_FIXED.png", 35),
    ("Upma", "Upma_FIXED.png", 15),
    ("Idli", "idli_FIXED.png", 370),
    ("Coffee", "Coffee_FIXED.png", 35),
    ("Green Tea", "Green_FIXED.png", 0),
    ("Kichdi", "Kichdi_FIXED.png", 15),
    ("Paneer", "Paneer_FIXED.png", 15),
    ("Rice", "Rice_FIXED.png", 206),
    ("Chapatti", "Chapatti_FIXED.png", 71),
    ("Dal", "Dal_FIXED.png", 124)
]

# Display Food Images in a Grid
for index, (name, img_file, cal) in enumerate(foods):
    img = load_resized_image(os.path.join(base_path, img_file))
    btn = Button(image=img, bg=BLACK, activebackground=GREY, command=lambda c=cal: add_calories(c))
    btn.image = img
    btn.grid(column=index % 5, row=(index // 5) + 1, padx=10, pady=10)

# Total Calories Display
total_label = Label(text=f"0/{daily_goal} 💪 Keep going!", fg=WHITE, bg=BLACK, font=FONT)
total_label.grid(column=1, row=6, columnspan=3, pady=10)

# Submit Button (Logs calories and updates UI)
submit_btn = Button(text="Submit", bg="blue", fg="white", font=FONT, command=submit)
submit_btn.grid(column=1, row=7, columnspan=3, pady=10)

# Confirmation Message (Appears after clicking submit)
confirmation_label = Label(text="", fg="green", bg=BLACK, font=FONT)
confirmation_label.grid(column=1, row=8, columnspan=3, pady=5)

# Total Calories Logged Display (Appears after clicking submit)
total_logged_label = Label(text="", fg=WHITE, bg=BLACK, font=FONT)
total_logged_label.grid(column=1, row=9, columnspan=3, pady=5)

# Close (Reset) Button (Appears after clicking submit)
close_button = Button(text="Close", bg="red", fg="white", font=FONT, command=reset)
close_button.grid_remove()  # Initially hidden

window.mainloop()
