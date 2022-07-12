from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login_c(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Vladimir", midlename="Vladimirovich", lastname="Kozlov", mobile="1234567890"))
    app.session.logout()


def test_add_emty_contact(app):
    app.session.login_c(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", midlename="", lastname="",
                                mobile=""))
    app.session.logout()

