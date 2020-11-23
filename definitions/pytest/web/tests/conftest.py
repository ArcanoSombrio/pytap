import pytest

from lib.utils.reports.allure_serve import stop_serve, open_serve


# Exemplo de implementação dos datilhos do Pytest


@pytest.hookimpl()
def pytest_sessionstart(session):
    stop_serve()


def pytest_sessionfinish(session):
    open_serve()


def pytest_runtest_setup(item):
    pass


def pytest_runtest_call(item):
    pass


def pytest_runtest_teardown(item, nextitem):
    pass
