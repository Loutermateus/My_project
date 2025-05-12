import pytest
from selenium import webdriver



@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://qa-windows-1.takeprofittech.com:8000")
    request.cls.driver = driver
    yield driver
    driver.quit()