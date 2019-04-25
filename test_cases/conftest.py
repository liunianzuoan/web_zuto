import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.index import IndexPage
from pages.invest import InvestPage

@pytest.fixture
def init_driver():
    print("begin driver")
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.get()

    yield (driver,login_page)

    print("quit driver")
    driver.quit()

@pytest.fixture('class')
def my_set_class():
    print('begin driver')
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    login_page.get()

    yield (driver,login_page,index_page)

    print("quit driver")
    driver.quit()


@pytest.fixture('class')
def invest_set_class():
    print("begin driver")
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    login_page.get()
    index_page = IndexPage(driver)
    invest_page = InvestPage(driver)
    login_page.submit_userinfo('18684720553','python')



    yield (driver,login_page,index_page,invest_page)

    print("quit driver")
    driver.quit()


