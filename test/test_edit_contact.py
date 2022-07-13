from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="New firstname"))


def test_edit_contact_midlename(app):
    app.contact.edit_first_contact(Contact(midlename="New midlename"))


def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="New lastname"))


def test_edit_contact_mobile(app):
    app.contact.edit_first_contact(Contact(mobile="88005354242"))
