import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options_languages = Options()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: ru, de or en')


@pytest.fixture(scope='function')
def browser(request):
    browser_language = request.config.getoption('language')
    browser = None
    if browser_language == 'ru':
        print('\nstart browser in russian..')
        options_languages.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options_languages)
    elif browser_language == 'en':
        print('\nstart browser in english..')
        options_languages.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options_languages)
    elif browser_language == 'de':
        print('\nstart browser in german..')
        options_languages.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options_languages)
    else:
        raise pytest.UsageError('--language should be: russian, english or german')
    yield browser
    print('\nquit browser..')
    browser.quit()
