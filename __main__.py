import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def fill_in_text(driver):
    first_name = driver.find_element_by_id("firstName")
    first_name.send_keys("Daniel ")
    last_name = driver.find_element_by_id("lastName")
    last_name.send_keys("Palacios")
    username = driver.find_element_by_id("username")
    username.send_keys("RanOOOOMMM12345dd")
    passward = driver.find_element_by_name("Passwd")
    passward.send_keys("C0D32222!!!!")
    confirm_pass = driver.find_element_by_name("ConfirmPasswd")
    confirm_pass.send_keys("C0D32222!!!!")
    next = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span")
    next.click()

    phone = driver.find_element_by_id("phoneNumberId")
    phone.send_keys("2247356291")
    next = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span")
    next.click()

    verify = driver.find_element_by_id("code")
    verification = str(input("Enter Verification Code:\n> "))
    verify.send_keys(verification)

    next = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[4]/div[1]/div[1]/span/span")
    next.click()

    driver.find_element_by_xpath("//select[@id='month']/option[text()= 'January']").click()
    driver.find_element_by_xpath("//select[@id='gender']/option[text()= 'Male']").click()
    driver.find_element_by_id("day").send_keys("26")
    driver.find_element("year").send_keys("1998")
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[5]/div[1]/div/span/span").click()
    scroll_elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/div[1]/span")
    driver.execute_script("return arguments[0].scrollIntoView();", scroll_elem)
    driver.execute_script("window.scrollBy(0,500)")
def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        print("false")
        return False
    return True

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://gmail.com") # Fix routing. Add path to .exe file to open


    # Retrieve elem:
    driver.implicitly_wait(5)
    create_account = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/span/span")
    create_account.click()

    if check_exists_by_xpath(driver, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]701594"):
        print("exists")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]701594")
        print("clicking")
        elem.click()


        # driver.implicitly_wait(15)
        # fill_in_text(driver)

    print("Fill text")
    fill_in_text(driver)
