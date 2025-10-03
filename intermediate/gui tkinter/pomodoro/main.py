from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, timer_count
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    tick.config(text="")
    window.after_cancel(timer_count)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(
        timer_text,
        text=f"{"0"+str(minutes) if minutes < 10 else minutes}:{"0"+str(seconds) if seconds < 10 else seconds}",
    )

    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += "✔️"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=300, height=400)

timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(
    105, 132, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white"
)
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)
window.mainloop()
