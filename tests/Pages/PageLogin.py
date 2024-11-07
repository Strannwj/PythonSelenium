from selenium.webdriver.common.by import By


def login_admin(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()