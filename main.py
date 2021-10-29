from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd?"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    long = reps / 4
    if reps % 8 == 0:
        title.config(text="Long Break", fg='yellow')
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title.config(text="Short Break", fg='yellow')
        countdown(SHORT_BREAK_MIN * 60)
    else:
        title.config(text="Timer", fg='yellow')
        countdown(WORK_MIN * 60)









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timertext,text = f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000,countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check.config(text = mark)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx=100,pady=50, bg=PINK)


canvas = Canvas(width=200, height=224,bg=PINK, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
timertext = canvas.create_text(100,130,text="00:00",fill="yellow",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
# countdown(5)
start = Button(text="Start", command = start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset")
reset.grid(column=2,row=2)

title = Label(text="Timer",fg='yellow',bg=PINK, font=(FONT_NAME,40,"bold"))
title.grid(column=1, row=0)

check = Label(text="",fg='green',bg=PINK, font=(FONT_NAME,20,"bold"))
check.grid(column=1, row=2)



window.mainloop()
