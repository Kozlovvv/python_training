from model.contact import Contact


def test_del_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="Contact from deleting"))
    app.contact.delete_first_contact()
