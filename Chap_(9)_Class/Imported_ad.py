"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa￾rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""


from Admin import Admin2

adminb = Admin2('Mahmud', 'Mahmud', 25, 'Kano State')
adminb.privileges.show_privileges()
#Output
'''
- can add participant',
- can remove participant',
- can switch to admin only
'''