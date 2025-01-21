from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_infinite_scrolling(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        product_container, total_products = WebDriverWait(driver, 10).until(
            lambda driver: (
                # EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
                driver.find_element(By.CSS_SELECTOR, '.product-list'),
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[4]/div[2]/div[1]/div/span')
            )
        )

        total_products = int(('').join(total_products.text.split()[1].split(',')))
        children = product_container.find_elements(By.XPATH, './div')
        initial_items = len(children)

        # Scroll down the page to trigger loading of new content
        for _ in range(5):  # Scroll down 5 times
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # Wait for new content to load

            driver.execute_script("window.scrollBy(0, -300);")
            time.sleep(2)

            # Check for new content after scrolling
            product_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
            )
            children = product_container.find_elements(By.XPATH, './div')
            new_items = len(children)

            if new_items == total_products:
                assert True
                break

            # Assert that the number of items increases after scrolling
            assert new_items > initial_items, f"Expected more items after scroll. Initial: {initial_items}, New: {new_items}"

            initial_items = new_items  # Update the initial count for next iteration

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_scrolling_n_populate(setup_browser):
    check_infinite_scrolling(setup_browser)