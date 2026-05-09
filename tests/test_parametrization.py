import pytest
from _pytest.fixtures import SubRequest



@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0



@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9), (-1, 1)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected



@pytest.mark.parametrize('os', ['macos', 'windows', 'linux'])
@pytest.mark.parametrize('browser', ['chrome', 'safari', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0



@pytest.fixture(
    params=['chrome', 'safari', 'firefox', 'webkit']
)
def browser(request):
    return request.param


def test_open_browser(browser: str):
    print(f'Open browser: {browser}')



@pytest.mark.parametrize('username', ['Helen', 'Julia'])
class TestOperations:
    @pytest.mark.parametrize('account', ['credit', 'debit'])
    def test_user_with_operations(self, username: str, account: str):
        print(f'User with operations {username}: {account}')

    def test_user_without_operations(self, username: str):
        print(f'User without operations: {username}')



users = {
    '+79999999999': 'user 1',
    '+78888888888': 'user 2',
    '+77777777777': 'user 3'
}



@pytest.mark.parametrize(
    'number',
    users.keys(),
    ids=lambda number: users[number]
)
def test_identifiers(number: str):
    ...
