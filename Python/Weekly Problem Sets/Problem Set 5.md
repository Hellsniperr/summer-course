# Problem Set 5 — Recursion & HTTP / APIs

**Topics covered:** recursion, `requests` module, REST APIs, HTTP methods and requests

**Autograder note:** When using automated tests, it often requires exact function names, parameter lists, and return types. Do not rename functions or change parameter names/order; avoid extra print statements unless the instructions ask for them; prefer returning values over printing when specified. Wrap any demonstration or test code in an `if __name__ == "__main__":` block so autograders can import your functions cleanly.

Work on a new branch named `python/problem-set-5` for this problem set.  Your submitted script must be named `Problem Set 5 starter.py` or `Problem Set 5.py` for it to be picked up by the autograder.  Once you have passed all tests, you can merge your code back into main.

## Submitting Your Work
As stated above, you should create a new branch and checkout that branch for this problem set called `python/problem-set-5`.  The general flow is shown below.

1. Fork the `AFC-AI2C/summer-course` repo (you only need to do this once)
   - This will create your own personal repo at `<github-username>/summer-course`
   - You have full ownership of that repo
2. Clone your personal repo locally (you only need to do this once)
3. Create and switch to a new branch called `python/problem-set-5`
4. Perform your work in either `Problem Set 5 starter.py` or a new file called `Problem Set 5.py`
5. Commit your changes
6. Push your changes
7. Review the output in GitHub Actions.  You can click into each run separately to see feedback
8. Fix any issues and repeat steps 5-7.
9. Once complete for all problems, you can merge your work back into main.

---

## Problem 1 — Basic Recursion

**Your task:**
- **Create a squares list using recursion**
  - Given an integer `n`, return a list of squares from `1..n` using recursion
  - Name your function `recursive_squares`
  - For example, if `n=5` then the function returns `[1, 4, 9, 16, 25]`
  - You only need to create the list using recursion, not the squares

- **Palindrome checker**
  - Given a string, check if it is a palindrome using recursion.  That is, is the string the same forwards and backwards, case insensitive.
  - Name your function `palindrome_checker`
  - For example, the input string `bacon` would return `False` while the string `radar` would return `True`.
  - Note, for our purposes, an empty string is a palindrome.
  - Note, for our purposes, punctuation and white space should be included.

- **List length**
  - Given a list, determine the length of the list using recursion
  - Name your function `length`
  - For example, the input list `[1, 2, 3]` would return `3`

### Challenge

- **Flatten**
  - Given a list, flatten the list into a single list using recursion.
  - Name your function `flatten`
  - For example, given `[1, [2, 3], [4], 5]` return `[1, 2, 3, 4, 5]`

---

## Problem 2 — Multiple Recursion


### Challenge


---

## Problem 3 — Basic HTTP Requests


### Challenge


---

## Problem 4 — Using a REST API


### Challenge


---

## References

