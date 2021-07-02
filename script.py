from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

# variables

button = "add-to-cart-button"
cart = "cart-icon"
shipping1 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/label/strong'
shipping2 = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[1]/form/ul/li[2]/div[1]/div/label/strong'
checkout = "checkout-buttons__checkout"
guest = "button-wrap"
first = '//*[@id="consolidatedAddresses.ui_address_1153.firstName"]'
last = '//*[@id="consolidatedAddresses.ui_address_1153.lastName"]'
street = '//*[@id="consolidatedAddresses.ui_address_1153.street"]'
city = '//*[@id="consolidatedAddresses.ui_address_1153.city"]'
state = '//*[@id="consolidatedAddresses.ui_address_1153.state"]'
zipcode = '//*[@id="consolidatedAddresses.ui_address_1153.zipcode"]'
email = "user.emailAddress"
phone = "user.phone"
continueBtn = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'
invalidadd = "/html/body/div[4]/div[2]/div/div/div/button[1]"


PATH = "C:\Program Files (x86)\chromedriver.exe"
PAGE = "https://www.bestbuy.com/site/mario-kart-8-deluxe-nintendo-switch/5723304.p?skuId=5723304"
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
        xpath(street).send_keys("123 Fairview")
        xpath(city).send_keys("Queens")
        select = Select(xpath(state))
        select.select_by_visible_text("NY")
        xpath(zipcode).send_keys(21034)
        ids(email).send_keys("johndoe123@gmail.com")
        ids(phone).send_keys(7184567890)
        xpath(continueBtn).click()
        time.sleep(2)
        try:
            xpath(invalidadd).click()
        except NoSuchElementException:
            continue

        break