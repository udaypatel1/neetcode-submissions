class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = collections.defaultdict(list)

        for word in strs:

            key = hash(frozenset(collections.Counter(word).items()))

            mapping[key].append(word)

        return list(mapping.values())