import tkinter as tk


def btn_click():
    global day, win
    day += 1
    win.title(f'카프리썬 {day}일차 Preview')


win = tk.Tk()
win.geometry('400x300')

btn = tk.Button(text='우웩', command=btn_click)
btn.pack()

day = 0
btn_click()
win.mainloop()

# Backend-- Java, Spring, Node.js, Go
