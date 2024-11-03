
from tkinter import *


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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLACK)


canvas = Canvas(width=200, height=224, bg=BLACK, highlightthickness=0)
img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= img)
canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer =Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50))
timer.grid(column= 1, row= 0)

start = Button(text="start")
start.grid(column=0, row=2)

reset = Button(text="reset")
reset.grid(column=2, row=2)






window.mainloop()