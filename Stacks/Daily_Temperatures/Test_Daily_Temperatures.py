from Daily_Temperatures import Solution


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed!")


def test_1():
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert sol.dailyTemperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_2():
    sol = Solution()
    temperatures = [30, 40, 50, 60]
    assert sol.dailyTemperatures(temperatures) == [1, 1, 1, 0]


def test_3():
    sol = Solution()
    temperatures = [30, 60, 90]
    assert sol.dailyTemperatures(temperatures) == [1, 1, 0]


def test_4():
    sol = Solution()
    temperatures = [90, 80, 70, 60, 50]
    assert sol.dailyTemperatures(temperatures) == [0, 0, 0, 0, 0]


def test_5():
    sol = Solution()
    temperatures = [70, 70, 70, 70, 71]
    assert sol.dailyTemperatures(temperatures) == [4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()
