#Author: Georgia Iferi
#Date: 09/27/24
#Short Desc: The Pomodoro Technique App is designed to help you improve focus and productivity using timed work sessions.
# The app follows the Pomodoro method: 25-minute work intervals followed by short breaks, with a longer break after completing a set of four Pomodoros.
# You can customize the durations of work sessions and breaks to fit your preferences.


import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "black"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 5
reps = 0
timer = None
marks = ''

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    titl.config(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    mark.config(text='')
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        count_down(short_break_sec)
        titl.config(text='Short Break', fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        titl.config(text='Break', fg=RED)
    else:
        count_down(work_sec)
        titl.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, marks

    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Technique")

window.config(padx=100, pady=50, bg=YELLOW)
titl = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
titl.grid(row=0, column=2)
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 135, text="00:00", font=(FONT_NAME, 35, 'bold'))
start_btn = Button(text='Start', command=start_timer, highlightthickness=0)
reset_btn = Button(text='Reset', highlightthickness=0, command=reset)
reset_btn.grid(row=3, column=3)
start_btn.grid(row=3, column=0)
mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
mark.grid(row=4, column=2)
canvas.grid(row=2, column=2)

window.mainloop()

