"""Problem Set 5 — Recursion & HTTP / APIs"""


# ── Problem 1 ─────────────────────────────────────────────────────────────────
def recursive_squares(num: int) -> list[int]:
    # base cases
    if num == 0:
        return []
    if num == 1:
        return [1]

    # recursive step
    childs_list = recursive_squares(num - 1)
    
    # add our number to child's
    square = num ** 2
    childs_list.append(square)

    return childs_list

def palindrome_checker(value: str) -> bool:
    value = value.lower()
    # base cases
    if len(value) == 0:
        return True
    if len(value) == 1:
        return True
    if len(value) == 2 and value[0] == value[-1]:
        return True
    if value[0] != value[-1]:
        return False

    # recursive step
    result = palindrome_checker(value[1:-1])
    return result

def length(input_list: list) -> int:
    # base case
    if input_list == []:
        return 0
    
    # recursive step
    child_depth = length(input_list[1:])

    return 1 + child_depth


## Challenge Problem
def flatten(input_list: list) -> list:
    # base case
    if input_list == []:
        return []

    # work / recurse
    if isinstance(input_list[0], list):
        first_element = flatten(input_list[0])
    else:
        first_element = [input_list[0]]
    
    # recurse remaining elements
    remaining_elements = flatten(input_list[1:])

    result = first_element.extend(remaining_elements)
    return result


# ── Problem 2 ─────────────────────────────────────────────────────────────────
