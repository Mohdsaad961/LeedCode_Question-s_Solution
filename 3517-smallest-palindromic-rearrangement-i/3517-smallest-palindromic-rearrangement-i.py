class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = ""
        middle = ""

        for i in range(26):
            left += (chr(i + ord('a'))) * (freq[i] // 2)
            if freq[i] % 2 != 0:
                middle += chr(i + ord('a'))

        return left + middle + left[::-1]