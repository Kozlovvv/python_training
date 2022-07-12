from model.contact import Contact


def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="editVladimir", midlename="editVladimirovich", lastname="Kozlov", mobile="111111111"))
    app.session.logout()