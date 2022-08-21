from pages.step_defs import open_main_page, search_for_repository, go_to_repository, open_issue_tab, \
    should_see_issue_with_name

base_url = 'https://github.com'
repository_name = 'eroshenkoam/allure-example'
issue_value = 'С Новым Годом (2022)'


def test_decorator_steps():
    open_main_page()
    search_for_repository(repository_name)
    go_to_repository(repository_name)
    open_issue_tab()
    should_see_issue_with_name(issue_value)
