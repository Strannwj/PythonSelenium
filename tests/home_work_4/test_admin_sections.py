from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_sections(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Appearence')]").click()
    driver.find_element(By.ID, 'doc-template' ).click()
    driver.find_element(By.ID, 'doc-logotype' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Catalog')]").click()
    driver.find_element(By.ID, 'doc-catalog' ).click()
    driver.find_element(By.ID, 'doc-product_groups' ).click()
    driver.find_element(By.ID, 'doc-option_groups' ).click()
    driver.find_element(By.ID, 'doc-manufacturers' ).click()
    driver.find_element(By.ID, 'doc-suppliers' ).click()
    driver.find_element(By.ID, 'doc-delivery_statuses' ).click()
    driver.find_element(By.ID, 'doc-sold_out_statuses' ).click()
    driver.find_element(By.ID, 'doc-csv' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Countries')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Currencies')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Customers')]").click()
    driver.find_element(By.ID, 'doc-customers' ).click()
    driver.find_element(By.ID, 'doc-csv' ).click()
    driver.find_element(By.ID, 'doc-newsletter' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Geo Zones')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Languages')]").click()
    driver.find_element(By.ID, 'doc-languages' ).click()
    driver.find_element(By.ID, 'doc-storage_encoding' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Modules')]").click()
    driver.find_element(By.ID, 'doc-jobs' ).click()
    driver.find_element(By.ID, 'doc-customer' ).click()
    driver.find_element(By.ID, 'doc-shipping' ).click()
    driver.find_element(By.ID, 'doc-payment' ).click()
    driver.find_element(By.ID, 'doc-order_total' ).click()
    driver.find_element(By.ID, 'doc-order_success' ).click()
    driver.find_element(By.ID, 'doc-order_action' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Orders')]").click()
    driver.find_element(By.ID, 'doc-orders' ).click()
    driver.find_element(By.ID, 'doc-order_statuses' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Pages')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Reports')]").click()
    driver.find_element(By.ID, 'doc-monthly_sales' ).click()
    driver.find_element(By.ID, 'doc-most_sold_products' ).click()
    driver.find_element(By.ID, 'doc-most_shopping_customers' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Settings')]").click()
    driver.find_element(By.ID, 'doc-store_info' ).click()
    driver.find_element(By.ID, 'doc-defaults' ).click()
    driver.find_element(By.ID, 'doc-general' ).click()
    driver.find_element(By.ID, 'doc-listings' ).click()
    driver.find_element(By.ID, 'doc-images' ).click()
    driver.find_element(By.ID, 'doc-checkout' ).click()
    driver.find_element(By.ID, 'doc-advanced' ).click()
    driver.find_element(By.ID, 'doc-security' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Slides')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Tax')]").click()
    driver.find_element(By.ID, 'doc-tax_classes' ).click()
    driver.find_element(By.ID, 'doc-tax_rates' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Translations')]").click()
    driver.find_element(By.ID, 'doc-search' ).click()
    driver.find_element(By.ID, 'doc-scan' ).click()
    driver.find_element(By.ID, 'doc-csv' ).click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'Users')]").click()

    driver.find_element(By.XPATH, "//*[@class='name']//a[contains(text(), 'vQmods')]").click()


















