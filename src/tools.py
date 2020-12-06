from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

class urls:
    login = 'https://account.ikonpass.com/en/login'
    add_reservations = 'https://account.ikonpass.com/en/myaccount/add-reservations/'

class IkonBot:
    def __init__(self, user):
        self.user = user
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.actions = ActionChains(self.driver)

    def login(self, user='', password='', delay=2):
        self.driver.get(urls.login)
        time.sleep(delay)
        user_elem = self.driver.find_element_by_id('email')
        user_elem.send_keys(user.name)
        pass_elem = self.driver.find_element_by_id('sign-in-password')
        pass_elem.send_keys(user.password)
        submit_button = self.driver.find_element_by_class_name('submit')
        submit_button.click()
        time.sleep(delay)

    def get_reservation_page(self):
        self.driver.get(urls.add_reservations)

    def choose_resort(self):
        mountain_link = self.driver.find_element_by_id(self.user.resort)
        self.actions.move_to_element(mountain_link).click().perform()

    def press_continue_button(self):
        continue_button = self.driver.find_elements_by_class_name('sc-AxjAm')[1]
        continue_button.click()

    def right_month(self):
        right_button = self.driver.find_element_by_class_name('icon-chevron-right')
        right_button.click()

    def pick_day(self):
        days_list = self.driver.find_elements_by_class_name('DayPicker-Day')
        chosen_day = next((x for x in days_list if x.get_attribute('aria-label') == self.user.day), None)
        chosen_day.click()

    def is_there_a_dismiss_button(self):
        unavailable_messages = self.driver.find_elements_by_class_name('sc-pdihw')
        if unavailable_messages:
            if unavailable_messages[0].is_displayed():
                print('unavailable message')
                return False
        else:
            print('going for it')
            self.save_and_review()
            return True

    def save_and_review(self):
        save_button = self.driver.find_element_by_class_name('jxPclZ')
        save_button.click()
        review_reservations_button = self.driver.find_element_by_class_name('jxPclZ')
        review_reservations_button.click()
        check_box = self.driver.find_element_by_class_name('input')
        check_box.click()
        confirm_reservations_button = self.driver.find_element_by_class_name('jxPclZ')
        confirm_reservations_button.click()
