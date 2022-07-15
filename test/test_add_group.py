from model.group import Group


def test_add_group(app):
    app.group.create_g(Group(name="hgfgfd", header="jhgfre", footer="xcvb"))


def test_add_empty_group(app):
    app.group.create_g(Group(name="", header="", footer=""))
