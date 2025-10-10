import tkinter


window = tkinter.Tk()
window.title('Hello')
window.minsize(width=500, height=300)


button_text  = 'Click Me'
button: tkinter.Button = tkinter.Button()

def button_clicked():
    button['text'] = 'Clicked!'

label1 = tkinter.Label(text='Name', font=("Arial", 24, "bold"))
label1.pack()
button['text'] = button_text
button['command'] = button_clicked
# button = tkinter.Button(text=button_text, background='red', command=button_clicked)
button.pack()


# def add (*args: int):
#     print(sum(args))

# add(1, 2, 3, 4, 5, 6, 7)


window.mainloop()