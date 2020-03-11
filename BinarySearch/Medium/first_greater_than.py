class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        first_greater_than = self.search_first_greater_than(nums, target, low, high)
        return first_greater_than

    def search_first_greater_than(self, nums, target, low, high):
        if low > high:
            return None
        middle = low + int((high - low) / 2)
        if nums[middle] > target and (middle == 0 or nums[middle - 1] <= target):
            return middle

        if nums[middle] >= target:
            return self.search_first_greater_than(nums, target, middle + 1, high)
        else:
            return self.search_first_greater_than(nums, target, low, middle - 1)


s = Solution()
nums = [5]
print(s.search(nums, 3))
