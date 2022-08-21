import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

base_url = 'https://github.com'
repository_name = 'eroshenkoam/allure-example'
issue_value = 'С Новым Годом (2022)'


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open(base_url)

    with allure.step(f'Ищем репозиторий {repository_name}'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys(repository_name)
        s('.header-search-input').submit()

    with allure.step(f'Переходим по ссылке {repository_name}'):
        s(by.link_text(repository_name)).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step(f'Проверяем наличие Issue с названием {issue_value}'):
        s(by.partial_text(issue_value)).should(be.visible)
