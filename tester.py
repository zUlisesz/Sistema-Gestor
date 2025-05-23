from controllers.admin_controller import AdminController

adm = AdminController()

members = adm.get_all()

for element in members:
    print(element)