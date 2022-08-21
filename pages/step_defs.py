import allure
from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозитория {repository}')
def search_for_repository(repository):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repository)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repository}')
def go_to_repository(repository):
    s(by.link_text(repository)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с названием {issue_value}')
def should_see_issue_with_name(issue_value):
    s(by.partial_text(issue_value)).click()
