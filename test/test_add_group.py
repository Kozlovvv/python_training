from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_g(Group(name="hgfgfd", header="jhgfre", footer="xcvb"))
    app.session.logout()


def test_add_emty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_g(Group(name="", header="", footer=""))
    app.session.logout()