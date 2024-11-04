import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver_fx():
    fx_driver = webdriver.Firefox()
    yield fx_driver
    fx_driver.quit()


@pytest.fixture
def driver_eg():
    eg_driver = webdriver.Edge()
    yield eg_driver
    eg_driver.quit()
