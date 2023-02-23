"""
Question (9-10)
Imported Restaurant: Using your latest Restaurant class, store it in a mod￾ule. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant's methods to show that the import statement is working properly.
"""
from Restaurant import Restaurant1

rest = Restaurant1('Patoosh','Chinese')
rest.number_served   # 0
rest.number_served = 8
rest.describe_restaurant()
rest.set_number_served(50)
rest.describe_restaurant()
rest.increment_number_served(7)
rest.describe_restaurant()