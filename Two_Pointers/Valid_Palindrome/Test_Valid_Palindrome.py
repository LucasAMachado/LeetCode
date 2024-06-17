import pytest
from Valid_Palindrome import Solution


def main():
    test_1()
    test_2()
    test_3()
    test_4()


def test_1():
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    assert sol.isPalindrome(s) == True


def test_2():
    sol = Solution()
    s = "racecar"
    assert sol.isPalindrome(s) == True


def test_3():
    sol = Solution()
    s = "race a car"
    assert sol.isPalindrome(s) == False


def test_4():
    sol = Solution()
    s = " "
    assert sol.isPalindrome(s) == True


if __name__ == "__main__":
    main()
