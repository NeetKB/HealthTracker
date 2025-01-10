import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from playwright.sync_api import expect, Page

CHROMEDRIVER_PATH = "C:\\Users\\amani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe" 

# Screen sizes to test
screen_sizes = [
    (1920, 1080),  # Desktop
    (1366, 768),   # Laptop
    (768, 1024),   # Tablet
    (375, 667)     # Mobile
]

url = "http://127.0.0.1:5000" 

@pytest.fixture
def driver():
    options = Options()
    #Headless  - the browser operates in the background without opening a visible window on your screen
    options.add_argument("--headless")
    driver_service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("width, height", screen_sizes)
def test_responsiveness(driver, width, height): 
    driver.get(url)
    driver.set_window_size(width, height)
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
    assert sign_in_button.is_displayed(), f"'Register' button is not visible at {width}x{height}"

    
