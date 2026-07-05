class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        first = strs[0]
        result = ""

        for i in range(len(first)):
            match = True

            for word in strs:
                if i >= len(word):
                    match = False
                    break

                if first[i] != word[i]:
                    match = False
                    break

            if match:
                result += first[i]
            else:
                break

        return result