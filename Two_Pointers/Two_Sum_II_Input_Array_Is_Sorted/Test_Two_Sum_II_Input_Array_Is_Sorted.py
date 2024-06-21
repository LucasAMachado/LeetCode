import pytest
from Two_Sum_II_Input_Array_Is_Sorted import Solution


def main():
    test_1()
    test_2()
    test_3()
    test_4()

def test_1():
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    assert sol.twoSum(numbers, target) == [1, 2]


def test_2():
    sol = Solution()
    numbers = [2, 3, 4]
    target = 6
    assert sol.twoSum(numbers, target) == [1, 3]


def test_3():
    sol = Solution()
    numbers = [-1, 0]
    target = -1
    assert sol.twoSum(numbers, target) == [1, 2]


def test_4():
    sol = Solution()
    numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    target = 8
    assert sol.twoSum(numbers, target) == [4, 5]


if __name__ == "__main__":
    main()
