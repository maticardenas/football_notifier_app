import pytest


@pytest.fixture(autouse=True)
def db(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()