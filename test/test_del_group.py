from model.group import Group


def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create_g(Group(name="Group from deleting"))
    app.group.delete_first_group()

