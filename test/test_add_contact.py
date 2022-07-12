from python_training.fixture.application_contact import Application
from python_training.model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Vladimir", midlename="Vladimirovich", lastname="Kozlov", mobile="1234567890"))
    app.logout()


def test_add_emty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", midlename="", lastname="",
                                mobile=""))
    app.logout()

