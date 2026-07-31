# recursion is a self-actioning loop that HAS TO HAVE A STOP POINT

# def factorial(n):
#     if n == 1 or n == 0:   ## This is the break, when n reaches 1 or 0
#         print("Reached Base Case")
#         return 1           ## it triggers this 'return' to "break" the loop
#     return n * factorial(n-1)


# Recursion causes a computer to hang onto previous function calls outputs in memory because
# it doesn't know what the next instance output is until it executes. It then won't complete
# all the final actions until each step it done (all aclculations of a Factorial), reaching 
# back into the stored outputs in memory. If there isn't enough memory, the system crashes.

# def palindrome(input_str):
#     if input_str == "":
#         return True
#     if len(input_str) == 1:
#         return True
    
#     if input_str[0] != input_str[-1]:
#         return False
    
#     print(f"Computing {input[1:-1]}")
#     result = palindrome(input_str[1:-1])
#     print(f"received {result} for {input_str[1:-1]}")
#     return result


# print(palindrome('level'))
# print(palindrome("3335"))




# calculate the sum of a list of numbers using recursion

def sum_list(input_list):
    if len(input_list) == 0:
        return 0
    
    print(f"evalusting {input_list}")
    result = sum_list(input_list[:-1] + )


# what is the base case?

# base case is when instance == len(list)

def list_sum(input_list):
    
    if len(input_list) == 0:
        return "End"

#what is(are) the recursive steps?
    return input_list[0] + list_sum(input_list[1:])
# [0:]



# Fibonacci Sequence

# f(5) = f(4) + f(3)
# f(4) = f(3) + f(2)
# f(3) = f(2) + f(1)
# f(2) = f(1) + f(0)
# f(1) = 1
# f(0) = 1