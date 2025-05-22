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



@pytest.fixture()
def add_users(request): # Фикстура для добавления юзеров в тест
    user_count = request.param # Принимаем кол-во юзеров из параметров теста
    drivers = [] # Создаем пустой список драйверов, туда будем класть новых юзеров
    for _ in range(user_count):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        drivers.append(driver) # Тут через цикл мы добавляем новые браузеры в список
    yield drivers # Переходим к тесту
    for driver in drivers: # После теста закрываем все драйверы, которые были созданы
        driver.quit()