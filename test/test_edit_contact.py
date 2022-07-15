from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="Contact from edit firstname"))
    app.contact.edit_first_contact(Contact(firstname="New firstname"))


def test_edit_contact_midlename(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="Contact from edit midlename"))
    app.contact.edit_first_contact(Contact(midlename="New midlename"))


def test_edit_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="Contact from edit lastname"))
    app.contact.edit_first_contact(Contact(lastname="New lastname"))


def test_edit_contact_mobile(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="Contact from edit mobile"))
    app.contact.edit_first_contact(Contact(mobile="88005354242"))
