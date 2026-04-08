from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letters = Counter('abcdefghijklmnopqrstuvwxyz')

        

        wordMap = defaultdict(list)

        for word in strs:
            m = letters.copy()
            for char in word:
                m[char] += 1
            
            wordMap[str(m)].append(word)
        
        result = []
        for key, value in wordMap.items():
            result.append(value)

        return result





        



        