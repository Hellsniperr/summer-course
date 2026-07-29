# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]
#     list2[0] = "hi"
#     list3 = "".join(list2)

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)

#1, 2
# hi, b, c
# hi, b, c, "doi-re-mi"


# Exercise 2

# What's the difference between sort and sorted?
# .sort() is used for a lists only and changes the original list
# sorted() changes the iterable and returns a new object without altering the original
# Which one is a list method and which one is a function that works on lists?

# Please explain



# Exercise 3

# Write a function that doubles the elements in a list.

# def doubl_list(my_list):
#     dbl_lst = []
#     for x in my_list:
#         dbl_lst.append(x * 2)
        
#     return dbl_lst


# list_orig = [1, 2, 3, 4]
# result = doubl_list(list_orig)

# print(result)

# Do you need to return anything here?



# Write a function that doubles the elements in a tuple.

def dbl_tuple(my_tuple):
    tuple1 = ()
    for x in my_tuple:
        tuple1 = tuple1 + (x * 2,)
        
    return tuple1
my_tup = (1, 2, 3, 4)
print(dbl_tuple(my_tup))
# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

def my_pop(in_list):
    new_val = in_list[index]
    del in_list[index]
    return new_val


def my_len(in_list):
    len = 0
    for elem in in_list:
        len += 1
    return len

def my_count(in_list, obj):
    count = 0
    
    
    
def my_extend(in_list, other_lst):
    for elem in other_lst:
        in_list.append(elem)
        
def my_reverse(in_list):
    reversed = []
    for elem in in_list[::-1]:
        reversed.append(elem)
    return reversed
# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

