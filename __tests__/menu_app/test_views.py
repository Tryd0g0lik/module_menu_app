"""
__tests__/menu_app/test_views.py

"""

import urllib.request as request

import pytest

from menu_app import views


def test_page_views_exists():
    """
    Test function to check the existsion of 'page_views' function.
    First - We check that the page 'views.py' has a function 'page_views'
    Second - We check that function the 'views.page_veiws' is exists.
    :return:
    """
    # https://docs.python.org/3.10/library/functions.html#hasattr
    assert hasattr(views, 'page_views')
    assert callable(views.page_views)

@pytest.fixture
def mock_env_app(monkeypatch: pytest.MonkeyPatch):
    """
    https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch
    :param monkeypatch:
    :return:
    """
    monkeypatch.setenv(
        "SECRET_KEY_DJ",
        "django-insecure-u(z84ocgmtrt31cg5ce)#5%kl2=@1&2ahim*=gy^m=0p#fmg@@")
    monkeypatch.setenv("POSTGRES_DB", "manuapp")
    monkeypatch.setenv("POSTGRES_PASSWORD", "123")
    monkeypatch.setenv("POSTGRES_USER", "postgres")
    monkeypatch.setenv("POSTGRES_HOST", "127.0.0.1")
    monkeypatch.setenv("POSTGRES_PORT", "5432")


@pytest.mark.django_db
def test_page_views_mock_request(mock_env_app):
    """"
    Testing the 'page_views' function with Mock request object. Method GET.
    https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
    https://docs.python.org/3/library/unittest.mock.html#the-mock-class
    """

    response_request = request.Request(url='http://127.0.0.1:8080/about/')
    response = views.page_views(response_request)
    # logging.info(f"Response Search the context: {response}")
    # logging.info(f"Status code: {response.status_code}")
    assert response.status_code == 200
