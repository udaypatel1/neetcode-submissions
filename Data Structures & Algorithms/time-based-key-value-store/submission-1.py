from collections import defaultdict

class TimeMap:

    def __init__(self):

        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        values_arr = self.m[key]

        # now we binary search in this sorted array

        l = 0
        r = len(values_arr) - 1

        result = ""

        while l <= r:

            mid = (l + r) // 2

            value, ts = values_arr[mid]

            if timestamp == ts:
                return value
            
            if ts <= timestamp:

                # update result if condition is satisfied
                result = value

                l = mid + 1
            else:
                r = mid - 1
        
        return result

        
