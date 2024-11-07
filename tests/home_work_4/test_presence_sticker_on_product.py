from selenium.webdriver.common.by import By
from lib.conftest import driver


def check_sticker_on_product_in_block(driver, block_id, product_name):
    try:
        product_element = driver.find_element(
            By.XPATH,
            f"//div[@id='{block_id}']//div[contains(@class, 'name') and text()='{product_name}']"
        )
        product_container = product_element.find_element(By.XPATH, "./parent::a")
        sticker_element = product_container.find_element(
            By.XPATH, ".//div[contains(@class, 'sticker') and (contains(@class, 'new') or contains(@class, 'sale'))]"
        )
        assert sticker_element, \
            f"Стикер 'sticker new' или 'sticker sale' отсутствует у продукта '{product_name}' в блоке '{block_id}'"
    except Exception as e:
        print(f"Продукт '{product_name}' не найден в блоке '{block_id}'.")


def test_presence_sticker_on_products_in_blocks(driver):
    driver.get("http://localhost/litecart/en/")

    product_names = ["Red Duck", "Green Duck", "Purple Duck", "Blue Duck", "Yellow Duck"]

    block_ids = ["box-most-popular", "box-campaigns", "box-latest-products"]

    for block_id in block_ids:
        for product_name in product_names:
            check_sticker_on_product_in_block(driver, block_id, product_name)
