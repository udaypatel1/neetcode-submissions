class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        def char_position(letter):
            return ord(letter) - 97

        def pos_to_char(pos):
            return chr(pos + 97)

        freq = [0] * 26

        for elem in s:
            freq[char_position(elem)] += 1

        for elem in t:
            freq[char_position(elem)] -=  1
        
        value = ''.join([str(x) for x in freq])
        return True if value.isdigit() and int(value) == 0 else False