import pytest
from typing import List
from Container_With_Most_Water import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49


def test_example_2(solution):
    height = [1, 1]
    assert solution.maxArea(height) == 1


def test_ascending_order(solution):
    height = [1, 2, 3, 4, 5]
    assert solution.maxArea(height) == 6


def test_descending_order(solution):
    height = [5, 4, 3, 2, 1]
    assert solution.maxArea(height) == 6


def test_all_same_height(solution):
    height = [3, 3, 3, 3, 3]
    assert solution.maxArea(height) == 12


def test_single_element(solution):
    height = [5]
    assert solution.maxArea(height) == 0


@pytest.mark.parametrize("n, expected", [
    (100, 2500),
    (1000, 250000),
    (10000, 25000000)
])
def test_large_input(solution, n, expected):
    height = list(range(1, n+1))
    assert solution.maxArea(height) == expected


if __name__ == "__main__":
    pytest.main([__file__])
