from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

# this is for test ... 
# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(20)
#driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Select Two Way  0 or 1

to_way = 1

# Select Complete Train Coupe  0 or 1

c_coupe = 0

# Navigate to the application home page


#driver.get("https://alibaba.ir")

driver.get("https://indraproject.ir")

# time.sleep(2)

for i in range(10):
    try:

        search_vehicle = driver.find_element_by_xpath("//*[@data-test='train-link']")

        if search_vehicle:
            print("true")

        search_vehicle.click()
        break
    except NoSuchElementException as e:
        print("Retry in 1 second")
        time.sleep(1)
else:
    raise e

time.sleep(2)
# Select Two Way -------------------------------------------------------------------------------------------------------

if to_way == 1:
    search_vehicle = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[1]"
                                                  "/div/span[2]/label")
    search_vehicle.click()

time.sleep(2)

# Select Complete Train Coupe ------------------------------------------------------------------------------------------

if c_coupe == 1:

    complete_coupe = driver.find_element_by_xpath("//*[@data-test='exclusiveCheckBoxLabel']")
    complete_coupe.click()
time.sleep(1)
# starting city --------------------------------------------------------------------------------------------------------

search_origin =driver.find_element_by_xpath("//*[@placeholder='مبدا (شهر)']")

search_origin.send_keys("تهران")
search_origin.send_keys(u'\ue007')

time.sleep(1)

# Destination City -----------------------------------------------------------------------------------------------------

search_destination =driver.find_element_by_xpath("//*[@placeholder='مقصد (شهر)']")

search_destination.send_keys("کرج")
search_destination.send_keys(u'\ue007')


time.sleep(1)

# Date Picker ----------------------------------------------------------------------------------------------------------
if to_way == 0:


    search_test = driver.find_element_by_xpath("//*[@data-test='departingDatePicker']")
    if search_test:
        print("true")

    search_test.click()

    time.sleep(2)



# search_departure = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[3]/div"
#                                                 "/div[3]/div/div[2]/div[1]/div/div/div[2]/div[32]/span[1]")
    search_departure = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[3]/div"
                                                "/div[3]/div/div[2]/div[1]/div/div/div[2]/div[34]/span[1]")
    if search_departure:
        print("true")
    search_departure.click()

    time.sleep(1)
else:
    # 28 esfand mah 1399
    search_departure = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[3]/div"
        "/div[3]/div/div[2]/div[1]/div/div/div[2]/div[34]/span[1]")

    # 26 esfand mah 1399
    # search_departure = driver.find_element_by_xpath(
    #     "/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[3]/div"
    #     "/div[3]/div/div[2]/div[1]/div/div/div[2]/div[32]/span[1]")
    if search_departure:
        print("two way source")
    search_departure.click()
    time.sleep(2)

    search_departure = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[2]/section/div[3]/div/div/form/div[3]/div"
        "/div[3]/div/div[2]/div[1]/div/div/div[2]/div[36]/span[1]")
    if search_departure:
        print("two way destination")
    search_departure.click()


search_departure = driver.find_element_by_xpath("//*[@data-testid='datapicker-modal-submit-button']")
search_departure.click()

time.sleep(2)


# Select Number of passengers -------------------------------------------------------------------------------------------------

search_departure = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[4]/div"
                                                "/div/div/div[3]/div/span[1]")
if search_departure:
    print("true")
search_departure.click()

time.sleep(2)

search_departure = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div[3]/div/div/form/div[4]/div"
                                                "/div/div/div[4]/div/span[1]")
search_departure.click()

time.sleep(1)
# Submit Button For Travel Search --------------------------------------------------------------------------------------------------------

search_departure = driver.find_element_by_xpath("//*[@data-test='searchBtn']")
search_departure.click()

time.sleep(5)

# Select Ticket For Payment --------------------------------------------------------------------------------------------

if to_way == 0:
    search_departure = driver.find_element_by_xpath("//*[@data-test='purchaseBtn']")
    search_departure.click()
else:
    search_departure = driver.find_element_by_xpath("//*[@data-test='purchaseBtn']")
    search_departure.click()

    time.sleep(1)
    search_departure = driver.find_element_by_xpath("//*[@id='train-available-select-button0']")
    search_departure.click()

time.sleep(1)


# Complete passenger information ---------------------------------------------------------------------------------------
# First Passenger : ------------------------------------------

   # First Name ...

search_origin =driver.find_element_by_xpath("//*[@data-test='persianFirstName']")
search_origin.click()
search_origin.send_keys("تست")

   # Last Name ...

search_origin =driver.find_element_by_xpath("//*[@data-test='persianLastName']")
search_origin.click()
search_origin.send_keys("تستی اول")

time.sleep(1)

   # Gender ...

select = Select(driver.find_element_by_xpath("//*[@data-test='passengerGender']"))
select.select_by_index(1)

   # National Code ...

search_origin =driver.find_element_by_xpath("//*[@data-test='nationalId']")
search_origin.click()
search_origin.send_keys("3309540502")

   # Date of birth :



select = Select(driver.find_element_by_xpath("//*[@data-test='birthDay']"))
select.select_by_index(10)

select = Select(driver.find_element_by_xpath("//*[@data-test='birthMonth']"))
select.select_by_index(5)


select = Select(driver.find_element_by_xpath("//*[@data-test='birthYear']"))
select.select_by_index(20)

time.sleep(2)

# Second Passenger : -------------------------------------


   # First Name ...

search_origin =driver.find_element_by_id("persian-name-1")
search_origin.click()
search_origin.send_keys("تست")


   # Last Name ...

search_origin =driver.find_element_by_id("persian-lastname-1")
search_origin.click()
search_origin.send_keys("تستی دوم")

time.sleep(1)

   # Gender ...

select = Select(driver.find_element_by_id("gender-1"))
select.select_by_index(2)

   # National Code ...

search_origin =driver.find_element_by_id("national-id-1")
search_origin.click()
search_origin.send_keys("0650451252")

time.sleep(2)

   # Date of birth :



search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[2]/div[3]/div[5]"
                                               "/div/div/select[3]/option[5]")
search_birthday.click()

search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[2]/div[3]/div[5]"
                                               "/div/div/select[2]/option[3]")
search_birthday.click()

search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[2]/div[3]/div[5]"
                                               "/div/div/select[1]/option[7]")
search_birthday.click()


time.sleep(2)



# Third Passenger : -------------------------------------


   # First Name ...

search_origin =driver.find_element_by_id("persian-name-2")
search_origin.click()
search_origin.send_keys("تست")


   # Last Name ...

search_origin =driver.find_element_by_id("persian-lastname-2")
search_origin.click()
search_origin.send_keys("تستی سوم")

time.sleep(1)

   # Gender ...

select = Select(driver.find_element_by_id("gender-2"))
select.select_by_index(2)

   # National Code ...

search_origin =driver.find_element_by_id("national-id-2")
search_origin.click()
search_origin.send_keys("0064844900")

time.sleep(2)

   # Date of birth :



search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[3]/div[3]/div[5]"
                                               "/div/div/select[3]/option[14]")
search_birthday.click()

search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[3]/div[3]/div[5]"
                                               "/div/div/select[2]/option[7]")
search_birthday.click()

search_birthday = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[3]/div[3]/div[5]"
                                               "/div/div/select[1]/option[2]")
search_birthday.click()


time.sleep(2)

# Send Ticket To Other Person Via Email Or Phone Numner ---------------------------------------------------------------

search_origin =driver.find_element_by_xpath("//*[@for='receiver']")
search_origin.click()

search_origin =driver.find_element_by_id("receiver-phone")
search_origin.click()
search_origin.send_keys("09226451141")

search_origin =driver.find_element_by_id("receiver-email")
search_origin.click()
search_origin.send_keys("m.badiolzamani@alibaba.ir")

time.sleep(2)
   # Scroll Down ...
driver.execute_script("window.scrollTo(0, 1920)")

time.sleep(2)
# Accept rules ---------------------------------------------------------------------------------------------------------

# search_origin = driver.find_element_by_css_selector("input[id = 'train-rules-accepted']")
search_origin = driver.find_element_by_xpath("/html/body/div/div/div/main/div/div/div[3]/form/div[4]/div[2]/div/label")

action = action_chains.ActionChains(driver)
time.sleep(1)
action.move_to_element_with_offset(search_origin, 1, 1)
action.click()
action.perform()


# Submit Passenger Information -----------------------------------------------------------------------------------------


search_origin =driver.find_element_by_xpath("//*[@data-test='submitPassenger']")
search_origin.click()


# Login To Account -----------------------------------------------------------------------------------------------------

search_origin =driver.find_element_by_xpath("//*[@data-test='emailWay']")
search_origin.click()

time.sleep(1)

search_origin =driver.find_element_by_xpath("//*[@data-test='usernameInput']")
search_origin.click()
search_origin.send_keys("m.badiolzamani@alibaba.ir")

time.sleep(1)

search_origin =driver.find_element_by_xpath("//*[@data-test='submitButton']")
search_origin.click()

time.sleep(1)

search_origin =driver.find_element_by_xpath("//*[@data-test='passwordInput']")
search_origin.click()
search_origin.send_keys("qaz@123")

time.sleep(1)

search_origin =driver.find_element_by_xpath("//*[@data-test='submitButton']")
search_origin.click()



# Verify For Payment ---------------------------------------------------------------------------------------------------

time.sleep(7)

finalSubmit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='train-pay-by-bank']")))
finalSubmit.click()

# search_origin =driver.find_element_by_xpath("//*[@id='train-pay-by-bank']")
