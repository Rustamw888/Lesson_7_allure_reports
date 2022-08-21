import allure
from allure_commons.types import Severity

from tests.test_steps import test_dynamic_steps
from tests.test_with_decorator import test_decorator_steps


def test_dynamic_labels():
    allure.dynamic.tag('Github web')
    allure.dynamic.label('owner', 'qaMilord')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Тестирование github')
    allure.dynamic.story('Поиск элементов')
    allure.dynamic.link('https://github.com', name='Testing')
    test_dynamic_steps()

@allure.tag('Github web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'qaMilord')
@allure.feature('Тестирование github')
@allure.story('Поиск элементов')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    test_decorator_steps()
