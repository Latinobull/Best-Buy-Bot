from tkinter import *

window = Tk(
    screenName="BB-Bot",
)


def test():
    print(first_value.get())
    print(last_value.get())
    print(address_value.get())
    print(city_value.get())
    print(zipcode_value.get())
    print(email_value.get())
    print(phone_value.get())
    print(card_value.get())
    print(month_value.get())
    print(year_value.get())
    print(ccv_value.get())


firstLabel = Label(window, text="Firstname:")
firstLabel.grid(row=0, column=0)

first_value = StringVar()
first = Entry(window, width=20, textvariable=first_value)
first.grid(row=0, column=1)

lastLabel = Label(window, text="Lastname:")
lastLabel.grid(row=1, column=0)

last_value = StringVar()
last = Entry(window, width=20, textvariable=last_value)
last.grid(row=1, column=1)

addressLabel = Label(window, text="Address St(apt if necessary):")
addressLabel.grid(row=2, column=0)

address_value = StringVar()
address = Entry(window, width=20, textvariable=address_value)
address.grid(row=2, column=1)

cityLabel = Label(window, text="City:")
cityLabel.grid(row=3, column=0)

city_value = StringVar()
city = Entry(window, width=20, textvariable=city_value)
city.grid(row=3, column=1)

zipcodeLabel = Label(window, text="Zipcode:")
zipcodeLabel.grid(row=4, column=0)

zipcode_value = StringVar()
zipcode = Entry(window, width=20, textvariable=zipcode_value)
zipcode.grid(row=4, column=1)

emailLabel = Label(window, text="Email:")
emailLabel.grid(row=5, column=0)

email_value = StringVar()
email = Entry(window, width=20, textvariable=email_value)
email.grid(row=5, column=1)

phoneLabel = Label(window, text="Phone Number: (1)")
phoneLabel.grid(row=6, column=0)

phone_value = StringVar()
phone = Entry(window, width=20, textvariable=phone_value)
phone.grid(row=6, column=1)

cardLabel = Label(window, text="Card Number (no spaces):")
cardLabel.grid(row=7, column=0)

card_value = StringVar()
card = Entry(window, width=20, textvariable=card_value)
card.grid(row=7, column=1)

monthLabel = Label(window, text="Month of Expiration (MM):")
monthLabel.grid(row=8, column=0)

month_value = StringVar()
month = Entry(window, width=20, textvariable=month_value)
month.grid(row=8, column=1)

yearLabel = Label(window, text="Year of Expiration (YYYY):")
yearLabel.grid(row=9, column=0)

year_value = StringVar()
year = Entry(window, width=20, textvariable=year_value)
year.grid(row=9, column=1)

ccvLabel = Label(window, text="Security Code:")
ccvLabel.grid(row=10, column=0)

ccv_value = StringVar()
ccv = Entry(window, width=20, textvariable=ccv_value)
ccv.grid(row=10, column=1)

siteLabel = Label(window, text="Link to Website:")
siteLabel.grid(row=11, column=0)

site_value = StringVar()
site = Entry(window, width=20, textvariable=site_value)
site.grid(row=11, column=1)


b1 = Button(window, text="Submit", command=test)
b1.grid(row=12, column=1)


window.mainloop()
