"""
Autograder tests for Problem Set 5 — Recursion & HTTP / APIs

Each test class tests either a custom class or a required function.
Tests run independently so students receive per-component feedback.

To run locally:
    pytest .github/python_tests/test_problem_set_5.py -v
"""

import copy
import os
import pytest
from conftest import load_student_module, assert_has_function
from random import randint


# ---------------------------------------------------------------------------
# Path to the student's submission (relative to the repo root)
# ---------------------------------------------------------------------------
_SOLUTION_MODE = os.environ.get("SOLUTION_MODE", "").lower() == "true"

STUDENT_FILE = (
    "Python/Weekly Problem Sets/Problem Set 5 solution.py"
    if _SOLUTION_MODE
    else "Python/Weekly Problem Sets/Problem Set 5 starter.py"
)


# ---------------------------------------------------------------------------
# Shared fixture — loads the student module once per test session
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def student():
    return load_student_module(STUDENT_FILE, "student_ps5")


class TestRecursiveSquares:
    """Tests for problem 1, recursive squares"""

    def test_recursive_squares_exists(self, student):
        assert_has_function(student, 'recursive_squares')

    def test_squares_empty_list(self, student):
        assert student.recursive_squares(0) == [], "When n = 0, the list should be empty"

    def test_squares_single(self, student):
        assert student.recursive_squares(1) == [1], "When n = 1, the list should be [1]"

    def test_squares_example(self, student):
        assert student.recursive_squares(5) == [1, 4, 9, 16, 25], "Failed the example of n=5"

    def test_squares_random(self, student):
        for i in range(5):
            n = randint(5, 15)
            ans = student.recursive_squares(n)
            assert len(ans) == n, f"Given n={n}, there should be {n} elements"
            assert ans[-1] == n ** 2, f"The last element for n={n} should be {n ** 2}"


class TestPalindromeChecker:
    """Tests for problem 1, palindrome checker"""
    def test_palindrome_checker_exists(self, student):
        assert_has_function(student, 'palindrome_checker')

    def test_palindrome_empty_string(self, student):
        assert student.palindrome_checker('') == True, "An empty string is a palindrome"

    def test_palindrome_examples(self, student):
        assert student.palindrome_checker('bacon') == False, "Bacon is not a palindrome"
        assert student.palindrome_checker('radar') == True, "Radar is a palindrome"

    def test_palindrome_even_length(self, student):
        for test_case, expected_result in {'leer': False, 'noon': True, 'deed': True, 'fear': False}.items():
            assert student.palindrome_checker(test_case) == expected_result, f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_odd_length(self, student):
        for test_case, expected_result in {'vader': False, 'radar': True, 'level': True, 'paper': False}.items():
            assert student.palindrome_checker(test_case) == expected_result, f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_sentences(self, student):
        cases = {
            'A man, a plan, a canal: Panama': False,
            'Able was I ere I saw Elba': True,
            'Eva, can I see bees in a cave?': False
        }
        for test_case, expected_result in {'leer': False, 'noon': True, 'deed': True, 'fear': False}.items():
            assert student.palindrome_checker(test_case) == expected_result, f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

