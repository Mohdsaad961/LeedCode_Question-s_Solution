class Solution:
    def minimumPushes(self, word: str) -> int:

        n = len(word)

        pushes = 0

        x = n // 8
        y = n % 8

        for i in range(x + 1):
            pushes += 8 * i

        pushes += y * (x + 1)

        return pushes
