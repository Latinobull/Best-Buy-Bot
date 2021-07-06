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
first = '//*[@id="consolidatedAddresses.ui_address_1154.firstName"]'
last = '//*[@id="consolidatedAddresses.ui_address_1154.lastName"]'
street = '//*[@id="consolidatedAddresses.ui_address_1154.street"]'
city = '//*[@id="consolidatedAddresses.ui_address_1154.city"]'
state = '//*[@id="consolidatedAddresses.ui_address_1154.state"]'
zipcode = '//*[@id="consolidatedAddresses.ui_address_1154.zipcode"]'
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
    print("Run the bot on Submit")


def Test():
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