import pytest


# Exemplo de implementação dos datilhos do Pytest


@pytest.hookimpl()
def pytest_sessionstart(session):
    pass


def pytest_sessionfinish(session):
    pass


def pytest_runtest_setup(item):
    pass


def pytest_runtest_call(item):
    pass


def pytest_runtest_teardown(item, nextitem):
    pass