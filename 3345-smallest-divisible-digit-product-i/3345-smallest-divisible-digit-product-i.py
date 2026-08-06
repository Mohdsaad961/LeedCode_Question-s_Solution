class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def digitProduct(x):
            product = 1
            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10
            return product

        x = n
        while True:
            if digitProduct(x) % t == 0:
                return x
            x += 1