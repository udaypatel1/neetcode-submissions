from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_map = defaultdict(list)

        for word in strs:

            counter = Counter(word)
            word_hash = frozenset(counter.items())

            grouped_map[word_hash].append(word)

        return list(grouped_map.values())