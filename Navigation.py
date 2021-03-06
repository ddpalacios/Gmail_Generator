from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Navigation_Window:
    def __init__(self, url, browser):
        self.double_click = 2
        self.curser = self._browser_choice(browser)
        self.curser.get(url)
        self.CREATE_ACCOUNT_PATH = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/span/span"
        self.OPTION_POPUP_PATH = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div"
        self.PERSONAL_PATH = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]/div[2]/div"
        self.USER_INFO_NEXT_PATH = "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span"
        self.PHONE_NEXT_PATH = "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span"
        self.VERIFICATION_NEXT_PATH = "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[4]/div[1]/div[1]/span/span"

    def _browser_choice(self, browser="firefox"):
        if browser is 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif browser is 'chrome':
            driver = webdriver.Chrome()
            return driver

    def find_elem_(self, path, type_):
        if type_ is "id":
            return self.curser.find_element_by_id(path)

        if type_ is "name":
            return self.curser.find_element_by_name(path)

        if type_ is "xpath":
            return self.curser.find_element_by_xpath(path)

    def Click_(self, element):
        return element.click()

    def Create_account(self, first=None, last=None, user_=None, pass_=None, phone_=None):
        # Retrieve elem:
        self.curser.implicitly_wait(5)
        try:
            for every_click in range(self.double_click):
                create_account_btn, personal_use_btn = self.find_elem_(self.CREATE_ACCOUNT_PATH, "xpath"), \
                                                       self.find_elem_(self.PERSONAL_PATH, "xpath")
                for each_button in [create_account_btn, personal_use_btn]:
                    
                    self.Click_(each_button)
              

        except:
            self.Create_account(first, last, user_, pass_)

        self.fill_in_text_(first, last, user_, pass_, phone_)

    def fill_in_text_(self, first, last, user_, pass_, phone_):
        first_name = self.find_elem_("firstName", "id")
        first_name.send_keys(first)

        last_name = self.find_elem_("lastName", "id")
        last_name.send_keys(last)

        username = self.find_elem_("username", "id")
        username.send_keys(user_)

        password = self.find_elem_("Passwd", "name")
        password.send_keys(pass_)

        confirm_pass = self.find_elem_("ConfirmPasswd", "name")
        confirm_pass.send_keys(pass_)
        elements = [first_name, last_name, username, password, confirm_pass]
        try:

            for each_click in range(self.double_click):
                self.Click_(self.find_elem_(self.USER_INFO_NEXT_PATH, "xpath"))
                print("click")

        except:
            for each_elem in elements:
                each_elem.clear()
            print("clear")
            self.fill_in_text_(first, last, user_, pass_, phone_)

        self.verification_(phone_)

    def verification_(self, phone_):
        self.find_elem_("phoneNumberId", "id").send_keys(phone_)
        self.find_elem_(self.PHONE_NEXT_PATH,
                        "xpath").click()

        verify = self.find_elem_("code", "id")
        verification = str(input("Enter Verification Code:\n> "))
        verify.send_keys(verification)

        for each_click in range(self.double_click):
            self.find_elem_(self.VERIFICATION_NEXT_PATH,
                            "xpath").click()

        self.confirm_bday_()

    def confirm_bday_(self):
        month = self.find_elem_("month", "id")
        monthDrop = Select(month)
        WebDriverWait(self.curser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='month']//options[contains(.,'January')]")))
        monthDrop.select_by_visible_text('January')

        gen = self.find_elem_("gender", "id")
        genDrop = Select(gen)
        WebDriverWait(self.curser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='gender']//options[contains(.,'Male')]")))
        genDrop.select_by_visible_text('Male')
        self.find_elem_("day", 'id').send_keys("26")
        self.find_elem_("year", 'id').send_keys("1998")
