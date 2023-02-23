from User import User2
class Admin(User2):
    '''An attempt to model an Admin, a special kind of User'''
    def __init__(self, first_name, last_name, age, address):
        super().__init__(first_name,last_name,age,address)
        self.privileges = ['can add participant','can remove participant','can switch to admin only']
    def show_privileges(self):
        '''Display the privileges an admin possesses'''
        print(f'\nThis admin has the following privileges')
        for item in self.privileges:
            print(f'-{item}')