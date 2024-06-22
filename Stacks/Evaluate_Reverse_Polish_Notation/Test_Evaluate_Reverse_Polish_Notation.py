from Evaluate_Reverse_Polish_Notation import Solution


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()


def test_1():
    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    assert sol.evalRPN(tokens) == 9


def test_2():
    sol = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    assert sol.evalRPN(tokens) == 22


def test_3():
    sol = Solution()
    tokens = ["4", "13", "5", "/", "+"]
    assert sol.evalRPN(tokens) == 6


def test_4():
    sol = Solution()
    tokens = ["2", "3", "+", "5", "/"]
    assert sol.evalRPN(tokens) == 1


def test_5():
    sol = Solution()
    tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    assert sol.evalRPN(tokens) == 14


def test_6():
    sol = Solution()
    tokens = ["3", "4", "+", "2", "*", "7", "/"]
    assert sol.evalRPN(tokens) == 2


def test_7():
    sol = Solution()
    tokens = ["3", "11", "+", "5", "-"]
    assert sol.evalRPN(tokens) == 9


def test_8():
    sol = Solution()
    tokens = ["10", "3", "/", "3", "+"]
    assert sol.evalRPN(tokens) == 6


if __name__ == "__main__":
    main()
