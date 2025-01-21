from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_filter_brand_single(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        filter_container = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div/button')
            )
        )

        filter_container.click()
        time.sleep(1)

        brand_container = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[4]/div[1]/div/div[2]/div[2]/div/div'))
        )

        brands = brand_container[0].find_elements(By.XPATH, './div')

        for brand in brands:
            checkbox = brand.find_element(By.XPATH, './/div[@class="tw-relative"]')

            # Scroll to the checkbox element
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)

            checkbox.click()
            time.sleep(1)

            # get name of brand
            brand_name = checkbox.find_element(By.XPATH, './/input[@type="checkbox"]').get_attribute("id").casefold()
            
            # get product container
            product_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
            )

            # get products list
            children = product_container.find_elements(By.XPATH, './div')
            for child in children:
                product_header = child.find_element(By.XPATH, './/div[contains(@class, "bu-grid") and contains(@class, "bu-gap-y-2")]')
                # print(product_header.text)
                assert brand_name in product_header.text.casefold(), "Product does not belong in this brand filter."
            
            checkbox.click()
            time.sleep(1)

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def check_filter_brand_multiple(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        filter_container = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div/button')
            )
        )

        filter_container.click()
        time.sleep(1)

        brand_container = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[4]/div[1]/div/div[2]/div[2]/div/div'))
        )

        brands = brand_container[0].find_elements(By.XPATH, './div')
        brand_names = []

        for brand in brands:
            checkbox = brand.find_element(By.XPATH, './/div[@class="tw-relative"]')

            # Scroll to the checkbox element
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)

            checkbox.click()
            time.sleep(1)

            # get name of brand
            brand_names.append(checkbox.find_element(By.XPATH, './/input[@type="checkbox"]').get_attribute("id").casefold())
            
            # get product container
            product_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
            )

            # get products list
            children = product_container.find_elements(By.XPATH, './div')
            for child in children:
                product_header = child.find_element(By.XPATH, './/div[contains(@class, "bu-grid") and contains(@class, "bu-gap-y-2")]')
                assert any(bn in product_header.text.casefold() for bn in brand_names), "Product does not belong in this brand filter."

            time.sleep(1)

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_filter_brand(setup_browser):
    check_filter_brand_single(setup_browser)
    setup_browser.refresh()
    check_filter_brand_multiple(setup_browser)