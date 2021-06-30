from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

page = "https://www.bestbuy.com/site/bose-soundlink-revolve-ii-portable-bluetooth-speaker-triple-black/6452118.p?skuId=6452118"

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(8)
driver.get(page)
# variables
classname = driver.find_element_by_class_name
xpath = driver.find_element_by_xpath
ids = driver.find_element_by_id
button = "add-to-cart-button"
cart = "cart-icon"
shipping1 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/label/strong'
shipping2 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[1]/form/ul/li[2]/div[1]/div/label/strong'
checkout = "checkout-buttons__checkout"
guest = "button-wrap"
first = "consolidatedAddresses.ui_address_2.firstName"
last = "consolidatedAddresses.ui_address_2.lastName"
street = "consolidatedAddresses.ui_address_2.street"
city = "consolidatedAddresses.ui_address_2.city"
state = '//*[@id="consolidatedAddresses.ui_address_2.state"]'
zipcode = "consolidatedAddresses.ui_address_2.zipcode"
email = "user.emailAddress"
phone = "user.phone"
continueBtn = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'
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
        ids(first).send_keys("John")
        ids(last).send_keys("Doe")
        ids(street).send_keys("123 Fairview")
        ids(city).send_keys("Queens")
        select = Select(xpath(state))
        select.select_by_visible_text("NY")
        ids(zipcode).send_keys(21034)
        ids(email).send_keys("johndoe123@gmail.com")
        ids(phone).send_keys(7184567890)
        xpath(continueBtn).click()

        break