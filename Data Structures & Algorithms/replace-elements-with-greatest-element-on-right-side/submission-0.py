class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for ptr in range(len(arr) - 1):

            arr[ptr] = max(arr[ptr + 1:])
        
        arr[-1] = -1
        return arr
        