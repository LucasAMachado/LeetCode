
# Solution 1 -> Time Complexity : O(log n), Space Complexity : O(n)
class TimeMap:

    def __init__(self):
        self.storage = {}  # key : List of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # return's [] if key not found in storage
        values = self.storage.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:  # valid search for closer value
                result = values[m][0]  # index 0 is the value
                l = m + 1  # see if we can find better
            else:
                # invalid timestamp
                r = m - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
