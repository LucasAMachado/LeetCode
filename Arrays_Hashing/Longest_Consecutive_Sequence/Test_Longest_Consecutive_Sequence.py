from Longest_Consecutive_Sequence import Solution
import pytest


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    assert solution.longestConsecutive(nums) == 4


def test_2():
    solution = Solution()
    nums = [100, 22, 44, 913, 914, 1293, 123, 100, 101, 102, 103]
    assert solution.longestConsecutive(nums) == 4


def test_3():
    solution = Solution()
    nums = []
    assert solution.longestConsecutive(nums) == 0


def test_4():
    solution = Solution()
    nums = [1, 2, 3, 3, 1, 199, 321321, 4132, 123,
            4213, 444, 445, 446, 447, 448, 449]
    assert solution.longestConsecutive(nums) == 6


if __name__ == "__main__":
    pytest.main()
