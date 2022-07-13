from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname= "Vladimir", midlename= "Vladimirovich", lastname= "Kozlov", mobile= "1234567890"))
    app.session.logout()


def test_add_emty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", midlename="", lastname="", mobile=""))
    app.session.logout()

