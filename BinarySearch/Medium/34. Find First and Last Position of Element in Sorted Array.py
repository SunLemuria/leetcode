class Solution:
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        lower_bound = self.search_lower_bound(nums, target, low, high)
        upper_bound = self.search_upper_bound(nums, target, low, high)
        return [lower_bound, upper_bound]

    def search_lower_bound(self, nums, target, low, high):
        if low > high:
            return -1
        middle = low + int((high - low) / 2)
        if nums[middle] == target and (middle == 0 or nums[middle - 1] < target):
            return middle

        if nums[middle] < target:
            return self.search_lower_bound(nums, target, middle + 1, high)
        else:
            return self.search_lower_bound(nums, target, low, middle - 1)

    def search_upper_bound(self, nums, target, low, high):
        if low > high:
            return -1
        middle = low + int((high - low) / 2)
        if nums[middle] == target and (middle == len(nums) - 1 or nums[middle + 1] > target):
            return middle

        if nums[middle] <= target:
            return self.search_upper_bound(nums, target, middle + 1, high)
        else:
            return self.search_upper_bound(nums, target, low, middle - 1)


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
print(s.searchRange(nums, 8))
