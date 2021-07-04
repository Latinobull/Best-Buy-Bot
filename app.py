from tkinter import *

window = Tk(
    screenName="BB-Bot",
)


def test():
    print(e1_value.get())


firstLabel = Label(window, text="Firstname:")
firstLabel.grid(row=0, column=0)

lastLabel = Label(window, text="Lastname:")
lastLabel.grid(row=1, column=0)

addressLabel = Label(window, text="Address St(apt if necessary):")
addressLabel.grid(row=2, column=0)

cityLabel = Label(window, text="City:")
cityLabel.grid(row=3, column=0)

zipcodeLabel = Label(window, text="Zipcode:")
zipcodeLabel.grid(row=4, column=0)

emailLabel = Label(window, text="Email:")
emailLabel.grid(row=5, column=0)

phoneLabel = Label(window, text="Phone Number: (1)")
phoneLabel.grid(row=6, column=0)

cardLabel = Label(window, text="Card Number (no spaces):")
cardLabel.grid(row=7, column=0)

monthLabel = Label(window, text="Month of Expiration (MM):")
monthLabel.grid(row=8, column=0)

yearLabel = Label(window, text="Year of Expiration (YYYY):")
yearLabel.grid(row=9, column=0)

ccvLabel = Label(window, text="Security Code:")
ccvLabel.grid(row=10, column=0)

siteLabel = Label(window, text="Link to Website:")
siteLabel.grid(row="11", column=0)

e1_value = StringVar()
e1 = Entry(window, width=20, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Submit", command=test)
b1.grid(row=2, column=2)


window.mainloop()
