
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# WORK_MIN = .1
# SHORT_BREAK_MIN = .1
# LONG_BREAK_MIN = .1

reps = 0
timer = None

from tkinter import *
from path_util import resource_path

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer, reps
    if timer:
        try:
            window.after_cancel(timer)
        except Exception:
            pass
        finally:
            timer = None
    header_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(canvas_text, text = f"00:00")
    check_marks.config(text='' )
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, timer
    if timer is not None:
        return
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        header_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        header_label.config(text='Short Break', fg=PINK)
    else:
        count_down(work_secs)
        header_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    remaining = int(count)
    count_min = remaining // 60
    count_sec = remaining % 60

    canvas.itemconfig(canvas_text, text = f"{count_min:02d}:{count_sec:02d}")

    if remaining > 0:
        timer = window.after(1000, count_down, remaining - 1)
    else:
        timer = None
        start_timer()
        work_completed = reps // 2
        check_marks.config(text='✔' * work_completed)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

tomato_img = PhotoImage(file=resource_path("tomato.png"))

# Initialize canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 100, image=tomato_img)
canvas_text = canvas.create_text(103, 115, fill='white', text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


# Header label
header_label = Label(text="Timer", font=('Times New Roman', 30, 'bold'), fg=GREEN, bg=YELLOW)
header_label.grid(row=0, column=1)

# Start button
btn_start = Button(text='Start', command=start_timer)
btn_start.grid(row=2, column=0)


# Reset button
btn_reset = Button(text='Reset', command=reset_timer)
btn_reset.grid(row=2, column=2)


check_marks = Label(text='', font=('Times New Roman', 24, 'bold'), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()