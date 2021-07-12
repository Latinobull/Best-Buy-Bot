from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from tkinter import *
from threading import Thread


# variables

button = "add-to-cart-button"
cart = "cart-icon"
shipping1 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/label/strong'
shipping2 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[1]/form/ul/li[2]/div[1]/div/label/strong'
checkout = "checkout-buttons__checkout"
guest = "button-wrap"
first = '//*[@id="consolidatedAddresses.ui_address_2.firstName"]'
last = '//*[@id="consolidatedAddresses.ui_address_2.lastName"]'
street = '//*[@id="consolidatedAddresses.ui_address_2.street"]'
city = '//*[@id="consolidatedAddresses.ui_address_2.city"]'
state = '//*[@id="consolidatedAddresses.ui_address_2.state"]'
zipcode = '//*[@id="consolidatedAddresses.ui_address_2.zipcode"]'
email = "user.emailAddress"
phone = "user.phone"
continueBtn = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'
invalidadd = "/html/body/div[4]/div[2]/div/div/div/button[1]"
card = "optimized-cc-card-number"
xprmonth = '//*[@id="credit-card-expiration-month"]/div/div/select'
xpryear = '//*[@id="credit-card-expiration-year"]/div/div/select'
ccv = "credit-card-cvv"
final_btn = "payment__order-summary"


def startBot():
    print("please work")
    process = Thread(target=Test())
    process.start()


def Test():
    window.destroy()
    # content = [
    #     first_value.get(),
    #     last_value.get(),
    #     address_value.get(),
    #     city_value.get(),
    #     zipcode_value.get(),
    #     email_value.get(),
    #     phone_value.get(),
    #     card_value.get(),
    #     month_value.get(),
    #     year_value.get(),
    #     ccv_value.get(),
    #     site_value.get(),
    # ]

    # (
    #     userFirst,
    #     userLast,
    #     userAddress,
    #     userCity,
    #     userZipcode,
    #     userEmail,
    #     userPhone,
    #     userCard,
    #     userMonth,
    #     userYear,
    #     userCCV,
    #     userSite,
    # ) = content

    print(first_value.get())
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    PAGE = "https://www.bestbuy.com/site/samsung-galaxy-buds-true-wireless-earbud-headphones-black/6400885.p?skuId=6400885"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
    driver.get(PAGE)
    classname = driver.find_element_by_class_name
    xpath = driver.find_element_by_xpath
    ids = driver.find_element_by_id

    while True:
        if classname(button).text == "Sold Out":
            print(classname(button).text)
            time.sleep(2)
            driver.refresh()
            continue
        else:
            classname(button).click()
            classname(cart).click()
            try:
                xpath(shipping1).click()
            except NoSuchElementException:
                xpath(shipping2).click()
            time.sleep(1)
            classname(checkout).click()
            classname(guest).click()
            xpath(first).send_keys("John")
            xpath(last).send_keys("Doe")
            xpath(street).send_keys("1760 Utica Ave")
            xpath(city).send_keys("Brooklyn")
            select = Select(xpath(state))
            select.select_by_visible_text("NY")
            xpath(zipcode).send_keys(11239)
            ids(email).send_keys("johndoe123@gmail.com")
            ids(phone).send_keys(7184567890)
            xpath(continueBtn).click()
            time.sleep(2)
            # try:
            #     xpath(invalidadd).click()
            # except NoSuchElementException:
            #     continue
            ids(card).send_keys("4916531789621660")
            select = Select(xpath(xprmonth))
            select.select_by_visible_text("10")
            select = Select(xpath(xpryear))
            select.select_by_visible_text("2023")
            ids(ccv).send_keys("331")
            classname(final_btn).click()
            time.sleep(4)
            driver.close()
            break


def startApp():

    global window

    window = Tk(
        screenName="BB-Bot",
    )

    firstLabel = Label(window, text="Firstname:")
    firstLabel.grid(row=0, column=0)

    global first_value
    first_value = StringVar()
    first = Entry(window, width=20, textvariable=first_value)
    first.grid(row=0, column=1)

    lastLabel = Label(window, text="Lastname:")
    lastLabel.grid(row=1, column=0)

    global last_value
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

    b1 = Button(window, text="Submit", command=startBot)
    b1.grid(row=12, column=1)

    window.mainloop()


startApp()