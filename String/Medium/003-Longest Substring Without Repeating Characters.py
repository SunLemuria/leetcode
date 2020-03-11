class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = dict()
        max_len = 0
        i = 0
        for j in range(len(s)):
            if s[j] in hash_map:
                i = max(i, hash_map[s[j]] + 1)

            hash_map[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len

    def lengthOfLongestSubstring_set(self, s: str) -> int:
        char_set = set()
        max_len = 0
        i = 0
        for ch in s:
            while ch in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(ch)
            max_len = max(max_len, len(char_set))

        return max_len
