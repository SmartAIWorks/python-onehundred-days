from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    with open('data.txt', 'a') as data_file:
        pass
# ---------------------------- UI SETUP ------------------------------- #




window = Tk()

ran = random.randint(8, 10)
print(ran)

# window.title('Password Manager')
# window.config(padx=20, pady=20)


# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='logo.png')

# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)

# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=1)

# website_text = Entry(width=35)
# website_text.grid(row=1, column=2)

# generate_button = Button(text='Generate Password', command=save)
# generate_button.grid(row=3, column=3)

# window.mainloop()