# what it has -> attributes
# what is does -> methods


# from  turtle import Turtle,Screen


# timmy = Turtle()
# timmy.shape("turtle")
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()


# print(timmy)

from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ['Name', 'City']
table.add_row(['John', 'Lucena City'])
table.add_row(['Amari', 'Quezon City'])
table.add_row(['Reyshel', 'Makati City'])


print(table)
print(table.get_string())