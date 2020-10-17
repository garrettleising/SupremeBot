from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import time
from datetime import datetime
from pytz import timezone

def doIt(profile):
    itemName = profile["itemName"]
    size = profile["size"]
    itemColor = profile["itemColor"]
    itemType = profile["itemType"]
    name = profile["name"]
    email = profile["email"]
    telephone = profile["telephone"]
    address = profile["address"]
    aptUnitEtc = profile["aptUnitEtc"]
    zipcode = profile["zipcode"]
    city = profile["city"]
    state = profile["state"]
    country = profile["country"]
    
    creditCardNumber = profile["creditCardNumber"]
    experationMonth = profile["experationMonth"]
    experationYear = profile["experationYear"]
    cvv = profile["cvv"]

    linkToSupreme = "https://www.supremenewyork.com"
    linkToStore = "https://www.supremenewyork.com/shop/all/" + itemType

    chrome_path = r'../Drivers/chromedriver'

    timeCycle = False  # True if you want the bot to wait for a specific time//False otherwise

    time_input = input("Optimized Time Loop? y/n\n")

    while( not (time_input == "y" or time_input == "n")):
        time_input = input("Please enter y or n\nOptimized Time Loop? y/n\n")

    if time_input == "y":
        timeCycle = True

    pacific = timezone('US/Pacific')
    USPacific_time = datetime.now(pacific)

    # waits for the correct time to run the bot
    while (USPacific_time.strftime('%H:%M:%S') != "07:59:25" and timeCycle):
        time.sleep(0.5)
        USPacific_time = datetime.now(pacific)
        print(USPacific_time)


    # Removes images from site
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_path, chrome_options=options)

    # driver = webdriver.Chrome(chrome_path)
    driver.get(linkToStore)

    t0 = time.time()
    print("Profile: " + name + " fetching at t= " + str(time.time() - t0))

    # consantly checks for the item and refreshes the page

    loop = True #Don't change ever
    hrefList = []
    while loop:
        productNames = driver.find_elements_by_class_name("name-link")
        for option in productNames:
            if re.search(itemName, option.text, re.IGNORECASE):
                newSearch = option.find_element_by_xpath('../../div[2]/a')
                if newSearch.text.lower() == itemColor.lower():
                    print("Profile: " + name + " picking up: " + option.text + " in the color: " + newSearch.text)
                    option.click()
                    loop = False
                    break
        time.sleep(1)
        driver.refresh()

    # tries to select a size option if there is one
    try:
        sizeOptions = driver.find_element_by_xpath("//select[@name='s'][@id='s']")
        all_sizeOptions = sizeOptions.find_elements_by_tag_name("option")
        for option in all_sizeOptions:
            if re.search(size, option.text, re.IGNORECASE):
                print("Profile: " + name + " selected size: " + option.text)
                option.click()
                break
    except:
        print("Profile: " + name + " no size option")


    # Waits for submit and checkout button to appear and clicks them
    wait = WebDriverWait(driver, 30)
    submit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='submit'][@name='commit'][@value='add to cart']")))
    submit.click()
    checkout = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='button checkout'][@data-no-turbolink='true']")))
    checkout.click()


    # Grabs form info
    order_billing_name = driver.find_element_by_id("order_billing_name")
    order_email = driver.find_element_by_id("order_email")
    order_tel = driver.find_element_by_id("order_tel")
    bo = driver.find_element_by_id("bo")
    order_billing_zip = driver.find_element_by_id("order_billing_zip")
    order_billing_city = driver.find_element_by_id("order_billing_city")
    order_billing_state = driver.find_element_by_id("order_billing_state")
    state_options = order_billing_state.find_elements_by_tag_name("option")
    order_billing_country = driver.find_element_by_id("order_billing_country")
    country_options = order_billing_country.find_elements_by_tag_name("option")
    creditCardNumberr = driver.find_element_by_id("rnsnckrn")
    credit_card_month = driver.find_element_by_id("credit_card_month")
    creditMonth_options = credit_card_month.find_elements_by_tag_name("option")
    credit_card_year = driver.find_element_by_id("credit_card_year")
    creditYear_options = credit_card_year.find_elements_by_tag_name("option")
    vval = driver.find_element_by_id("orcer")
    iCheckHelper = driver.find_elements_by_class_name("iCheck-helper")
    iCheckHelper = iCheckHelper[1]

    # fills form
    order_billing_name.send_keys(name)
    order_email.send_keys(email)
    order_tel.send_keys(telephone)
    bo.send_keys(address)
    order_billing_zip.send_keys(zipcode)
    order_billing_city.send_keys(city)
    for option in state_options:
        if (option.text == state):
            option.click()
            break
    for option in country_options:
        if (option.text == country):
            option.click()
            break
    creditCardNumberr.send_keys(creditCardNumber)
    for option in creditMonth_options:
        if (option.text == experationMonth):
            option.click()
            break
    for option in creditYear_options:
        if (option.text == experationYear):
            option.click()
            break
    vval.send_keys(cvv)
    iCheckHelper.click()

    print("Profile: " + name + " checkout complete at t= " + str(time.time() - t0))

    # 30 mins of sleeping
    time.sleep(1800)

    # assert "No results found." not in driver.page_source
    # click pay
    driver.close()

