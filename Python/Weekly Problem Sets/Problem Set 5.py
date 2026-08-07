# Problem 1

def recursive_squares(n):

    if n == 0:
        return []

    else:
        return recursive_squares(n - 1) + [n ** 2] #[n ** 2] is for the current call AND trip the base case; (n - 1) sets up the next call to the function

n = int(input("Enter a non-negative integer: "))
print(recursive_squares(n))


def palindrome_checker(s):

    