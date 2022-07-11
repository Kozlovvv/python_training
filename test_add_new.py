from applicationnew import Application
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Vladimir", midlename="Vladimirovich", lastname="Kozlov", mobile="1234567890"))
    app.logout()


def test_add_emty_new(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", midlename="", lastname="",
                                mobile=""))
    app.logout()

