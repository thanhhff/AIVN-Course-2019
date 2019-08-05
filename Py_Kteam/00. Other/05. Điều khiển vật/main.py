from tkinter import *

tk = Tk()

cas = Canvas(tk, width=1000, height=1000)
cas.create_polygon(10, 10, 10, 30, 50, 30)
cas.pack()
cas.mainloop()


def diChuyen(event):
    if event.keysym == "Up":
        cas.move(1, 0, -3)


cas.bind_all('<KeyPress-Up>', diChuyen())
