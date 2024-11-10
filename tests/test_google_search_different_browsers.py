from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.conftest import driver_fx, driver_eg


GOOGLE = 'https://www.google.com/'
SEARCH_BOX = (By.NAME, 'q')
SEARCH_PHRASE = 'Selenium'


def test_google_search_fx(driver_fx):
    driver_fx.get(GOOGLE)
    search_box = driver_fx.find_element(*SEARCH_BOX)
    search_box.send_keys(SEARCH_PHRASE)
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver_fx, 10).until(EC.title_contains("Selenium"))

    assert "Selenium" in driver_fx.title


def test_google_search_eg(driver_eg):
    driver_eg.get(GOOGLE)
    search_box = driver_eg.find_element(*SEARCH_BOX)
    search_box.send_keys(SEARCH_PHRASE)
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver_eg, 10).until(EC.title_contains("Selenium"))

    assert "Selenium" in driver_eg.title
