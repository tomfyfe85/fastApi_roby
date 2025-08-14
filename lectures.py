# def percentage_calculator(initial, item_cost, tax):
#     full_price = item_cost + (tax/100 * item_cost)
#     return initial - full_price

# print(percentage_calculator(50, 15, 3))


# first_name = "tom"
# last_name = "fyfe"

# greet = "hi {} {}"
# print(greet.format(first_name, last_name))
# days = input("how many days? : ")
# print(f"it's approx {round(int(days)/7, 2)} weeks to your birthday")

"""
Sets and Tuples
"""
# my_set = {1,2,3,4,5,1,2}
# print(my_set)

# for x in my_set:
#     print(x)

# sets are unorderd in memory, this means we can't print a set item by index
# print(my_set[0]) - throws a TypyError

# to remove an element from set, use .discard - Below will remove the element with the value of 3
# my_set.discard(3)
# print(my_set)
# # .clear will remove all element from the set
# my_set.clear()
# print(my_set)
# # add elements with .add
# my_set.add(6)
# print(my_set)
# # add more than 1 element at a time using .update()
# my_set.update([10,11])
# print(my_set)

# list = []
# set = {}
# tuple = ()

# Tuples are unable to be modified


#Boolean and Operators


# comparison operators
#  ==
#  <, > , >= etc

# logical operators
# and  - both comparisons must be true to => true
# or - either comparison must be true to => true
# not - checks the reverse of the comparison ie not(1 == 1) - checking if 1==1 is not true. => False


#For and While Loops

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is equal to or larger than 5")

#continue skips that iteration of the loop and goes back to the beginning
#can use an else statement
#break means stop the loop completely
