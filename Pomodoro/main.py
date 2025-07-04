from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    countdown(5 * 60)
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, countdown, )

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Pomodoro", fg=GREEN, font=(FONT_NAME, 30, "normal"), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



window.mainloop()