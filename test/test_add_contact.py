from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Vladimir", midlename="Vladimirovich", lastname="Kozlov", mobile="1234567890"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", midlename="", lastname="", mobile=""))
