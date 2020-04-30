import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name ")

@pytest.fixture()
def test_setup(request):
    # from selenium import webdriver
    # browser = request.config.getoption("--browser")
    # if browser == "chrome":
    driver = webdriver.Chrome(executable_path="C:/Users/Saurav/PycharmProjects/DemoBlazePytest/driver/chromedriver.exe")

    # elif browser == "firefox":
    #     driver = webdriver.Firefox(executable_path="C:/Users/Saurav/PycharmProjects/DemoBlazePytest/driver/geckodriver.exe")
    # driver.get("https://www.demoblaze.com/index.html")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    driver.quit()