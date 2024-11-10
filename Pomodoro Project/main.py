from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLACK = "#000000"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
start_label = "Timer"
start_timer_text = "00:00"
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    start.config(text=start_label)
    check_marks.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    #If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        start.config(text="Break", fg=RED)

    #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        start.config(text="Break", fg=PINK)

    #If it's the 1st/3rd/5th/7th
    else:
        count_down(work_sec)
        start.config(text="Work", fg=GREEN)
#---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    global  reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        reps += 1
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start = Label(text=start_label, fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
start.grid(column= 1, row= 0)


check_marks = Label(fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
check_marks.grid(column= 1, row= 4)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset = Button(text="reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)






window.mainloop()