from model.contact import Contact


def test_edit_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New firstname"))
    app.session.logout()


def test_edit_contact_midlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(midlename="New midlename"))
    app.session.logout()


def test_edit_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(lastname="New lastname"))
    app.session.logout()


def test_edit_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(mobile="88005354242"))
    app.session.logout()

