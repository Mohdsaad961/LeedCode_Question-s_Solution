class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        largest = nums[0]

        sec_large = nums[1]

        product = (largest - 1) * (sec_large - 1)

        return product   