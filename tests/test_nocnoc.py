import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.test_init_page import test_init_page
from src.test_seo_elements import test_seo_elements
from src.test_scrolling_n_populate import test_scrolling_n_populate
from src.test_sort_price_asc_n_desc import test_sort_price_asc_n_desc
from src.test_sort_new_arrival import test_sort_new_arrival
from src.test_sort_amount_sold import test_sort_amount_sold
from src.test_filter_brand import test_filter_brand
from src.test_filter_price import test_filter_price
from src.test_href import test_href
from src.test_language_change import test_language_change

# Pytest Fixture for Setup and Teardown
@pytest.fixture
def setup_browser():
    """Set up the Selenium WebDriver."""
    # Set up Chrome options
    options = Options()
    # options.add_argument("--disable-javascript")
    options.add_argument("--headless")  # Optional: Run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
