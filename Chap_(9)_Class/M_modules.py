from Admin_prv import Admin

adminb = Admin('Mahmud', 'Mahmud', 25, 'Kano State')
adminb.privileges.show_privileges()  # worked, output below
"""
This admin has the following privileges
-can add post
-can delete post
-can ban user
"""