import pytest
from Score_of_a_String import Solution


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()


def test_1():
    sol = Solution()
    s = "hello"
    assert sol.scoreOfString(s) == 13


def test_2():
    sol = Solution()
    s = "zaz"
    assert sol.scoreOfString(s) == 50


def test_3():
    sol = Solution()
    s = "abc"
    assert sol.scoreOfString(s) == 2


def test_4():
    sol = Solution()
    s = "aaa"
    assert sol.scoreOfString(s) == 0


def test_5():
    sol = Solution()
    s = "az"
    assert sol.scoreOfString(s) == 25


def test_6():
    sol = Solution()
    s = "programming"
    assert sol.scoreOfString(s) == 69


if __name__ == "__main__":
    pytest.main()
