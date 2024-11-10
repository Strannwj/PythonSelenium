from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.conftest import driver


GOOGLE = 'https://www.google.com/'
SEARCH_BOX = (By.NAME, 'q')
SEARCH_PHRASE = 'Selenium'


def test_google_search(driver):
    driver.get(GOOGLE)
    search_box = driver.find_element(*SEARCH_BOX)
    search_box.send_keys(SEARCH_PHRASE)
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))

    assert "Selenium" in driver.title
