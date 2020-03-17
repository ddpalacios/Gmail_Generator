import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


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

    try:

        next = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span")
        next.click()
        phone = driver.find_element_by_id("phoneNumberId")
        phone.send_keys("2247356291")
        next = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span")
        next.click()
        verify = driver.find_element_by_id("code")
        verification = str(input("Enter Verification Code:\n> "))
        verify.send_keys(verification)

        next = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[4]/div[1]/div[1]/span/span")
        next.click()

        month = driver.find_element_by_id("month")
        monthDrop = Select(month)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='month']//options[contains(.,'January')]")))
        monthDrop.select_by_visible_text('January')

        gen = driver.find_element_by_id("gender")
        genDrop = Select(gen)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='gender']//options[contains(.,'Male')]")))
        genDrop.select_by_visible_text('Male')
        driver.find_element_by_id("day").send_keys("26")
        driver.find_element("year").send_keys("1998")


    except:
        first_name.clear()
        last_name.clear()
        username.clear()
        passward.clear()
        confirm_pass.clear()
        fill_in_text(driver)


def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        print("false")
        return False
    return True


def Create(driver):
    # Retrieve elem:
    driver.implicitly_wait(5)
    create_account = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/span/span")
    try:
        create_account.click()
    except:
        Create(driver)

    if check_exists_by_xpath(driver, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div"):
        print("exists")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]/div[2]/div")
        print("clicking")
        try:
            elem.click()
        except:
            print("trying again")
            Create(driver)
    print("Fill text")
    try:
        fill_in_text(driver)
    except:
        Create(driver)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://gmail.com") # Fix routing. Add path to .exe file to open
    Create(driver)



