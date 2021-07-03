from tkinter import *

window = Tk(
    screenName="BB-Bot",
)


def test():
    print(e1_value.get())
    t1.delete("1.0", END)
    t1.insert(END, e1_value.get())


firstLabel = Label(window, text="Firstname")
firstLabel.grid(row=0, column=0)

t1 = Text(window, height=1)
t1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, width=20, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Submit", command=test)
b1.grid(row=2, column=2)


window.mainloop()
