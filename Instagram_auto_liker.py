from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from pprint import pprint
import time
import sys

def main():
    id = '__USER__'
    passd = '__PASSWORD__'
    try:
        url = 'https://www.instagram.com'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)

        driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')
        driver.get(url)
        driver.maximize_window()

        assert "Instagram" in driver.title

        time.sleep(5)

        username = driver.find_element_by_name('username')
        username.send_keys(id)

        password = driver.find_element_by_name('password')
        password.send_keys(passd)

        password.send_keys(Keys.ENTER)

        time.sleep(3)

        NotSave = driver.find_elements_by_class_name("sqdOP")
        NotSave[1].click()

        time.sleep(5)

        # Like Loop
        pos = 0
        while True:
            # Get all svgs in this page
            time.sleep(1)
            imgs = driver.find_elements_by_tag_name("svg")
            
            for i in imgs:
                try:
                    # Go to svg
                    if pos > i.location['y']-54:
                        continue
                    if pos != i.location['y']-54:
                        pos = i.location['y']-54 
                        driver.execute_script("window.scrollTo(0, {})".format(pos))
                        time.sleep(1)
                    if i.get_attribute("aria-label") == "Like" and i.get_attribute("width") == "24":
                        # btn = i.parent.parent.parent
                        btn = i.find_element_by_xpath("../../../..")
                        btn.click()
                        print("Like")
                        time.sleep(1)
                except WebDriverException as w:
                     print("error", str(w))

        # Close the tab/browser when done

        driver.close()
    except WebDriverException as w:
        print("error", str(w))

main()
