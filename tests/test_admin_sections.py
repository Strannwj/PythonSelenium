from selenium.webdriver.common.by import By
from lib.conftest import driver
from tests.Pages.PageLogin import login_admin


def check_h1_presence(driver):
    assert driver.find_element(By.TAG_NAME, "h1"), "Элемент с тегом <h1> не найден"


def navigate_and_check(driver, section_name, subsections):
    driver.find_element(By.XPATH, f"//span[contains(text(), '{section_name}')]").click()
    check_h1_presence(driver)

    for subsection_id in subsections:
        driver.find_element(By.ID, subsection_id).click()
        check_h1_presence(driver)


def test_admin_sections(driver):
    login_admin(driver)

    sections = {
        "Appearence": ["doc-template", "doc-logotype"],
        "Catalog": ["doc-catalog", "doc-product_groups", "doc-option_groups", "doc-manufacturers",
                    "doc-suppliers", "doc-delivery_statuses", "doc-sold_out_statuses", "doc-csv"],
        "Countries": [],
        "Currencies": [],
        "Customers": ["doc-customers", "doc-csv", "doc-newsletter"],
        "Geo Zones": [],
        "Languages": ["doc-languages", "doc-storage_encoding"],
        "Modules": ["doc-jobs", "doc-customer", "doc-shipping", "doc-payment",
                    "doc-order_total", "doc-order_success", "doc-order_action"],
        "Orders": ["doc-orders", "doc-order_statuses"],
        "Pages": [],
        "Reports": ["doc-monthly_sales", "doc-most_sold_products", "doc-most_shopping_customers"],
        "Settings": ["doc-store_info", "doc-defaults", "doc-general", "doc-listings", "doc-images",
                     "doc-checkout", "doc-advanced", "doc-security"],
        "Slides": [],
        "Tax": ["doc-tax_classes", "doc-tax_rates"],
        "Translations": ["doc-search", "doc-scan", "doc-csv"],
        "Users": [],
        "vQmods": []
    }

    for section, subsections in sections.items():
        navigate_and_check(driver, section, subsections)
