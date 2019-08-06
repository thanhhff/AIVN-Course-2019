from tkinter import *
import time

tk = Tk()

cas = Canvas(tk, width=1000, height=1000)


# for i in range(1000):
cas.create_oval(100, 5, 432, 500)
cas.create_text(100, 300, text ='Hello', font=('Times', 200))

# btn = Button(tk, text='Click me')
# btn.pack()
# btn.mainloop()
# time.sleep(10)

cas.pack()
cas.mainloop()
