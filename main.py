from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.Keys import Keys
import time

My_login = "********************@gmail.com"
My_password = "**********"
My_phonenumber = "*********"

def abort_application():
    #Close button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    #discard button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3683096434&distance=25&f_AL=true&geoId=103112676&keywords=Python%20Developer&location=Chicago%2C%20Illinois%2C%20Stany%20Zjednoczone&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
#reject cookies
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

#click sign in button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")

#sign in
time.sleep(5)
login_username = driver.find_element(by=By.ID, value="username")
login_username.send_keys(My_login)

password = driver.find_element(by=By.ID, value="password")
password.send_keys(My_password)
password.send_keys(Keys.ENTER)

#Captcha
input("Press ENTER when you have solved Captcha")

#Get listings
time.sleep(3)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

#Apply for jobs:
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(3)
    try:

        #lokate apply button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        #phone number
        time.sleep(5)
        phone_number_place = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone_number_place.text == "":
            phone_number_place.send_keys(My_phonenumber)

        #check submit button:
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name")=="continue_unify":
            abort_application()
            print("Too complex application, skipped.")
            continue
        else:
            #click submit button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        #click close button
        close_button = driver.find_element(by = By.CLASS_NAME, value="artdeco-modal__dissmiss")
        close_button.click()

    except:
        abort_application()
        print("Lack of application button, skipped.")
        continue

time.sleep(10)
driver.quit()




