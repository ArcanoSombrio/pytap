import pytest

from lib.runner.execute.interact.interact import Interact


# Exemplo de implementação dos datilhos do Pytest


@pytest.hookimpl()
def pytest_sessionstart(session):
    Interact.stop_allure_serve()


def pytest_sessionfinish(session):
    Interact.start_allure_serve()


def pytest_runtest_setup(item):
    pass


def pytest_runtest_call(item):
    item.module._session = Interact.open_session()


def pytest_runtest_teardown(item, nextitem):
    pass
