#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        cache, result = [], []
        words_len = len(''.join(words))

        for i in range(len(s)-words_len+1):
            substring = s[i:]

            # Quick checking using the cache
            if any((substring.startswith(c) for c in cache)):
                result.append(i)
                continue

            longest_substring = self.find_longest_substring(substring, words)
            if len(longest_substring) == words_len:
                # Add the matched substring into the cache for quick checking
                cache.append(longest_substring)
                result.append(i)

        return result

    def find_longest_substring(self, s: str, words: list[str]) -> bool:
        """Find the longest possible substring"""
        if len(words) == 0:
            return ""
        if len(s) < len(''.join(words)):
            return ""

        for word in words:
            if s.startswith(word):
                # New words list is created because parameter in python is passed by assignment
                new_words = words.copy()
                new_words.remove(word)
                return word + self.find_longest_substring(s[len(word):], new_words)

        return ""

# @lc code=end
