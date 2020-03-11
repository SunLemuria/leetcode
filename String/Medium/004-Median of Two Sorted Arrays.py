class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = int((m + n) / 2)

        if (m + n) % 2 == 1:
            return self.find_k_th(nums1, 0, m - 1, nums2, n - 1, k + 1)
        else:
            return (self.find_k_th(nums1, 0, m - 1, nums2, 0, n - 1, k)
                    + self.find_k_th(nums1, 0, m - 1, nums2, 0, n - 1, k + 1)) / 2.0

    def find_k_th(self, nums1, l1, h1, nums2, l2, h2, k):
        m = h1 - l1 + 1
        n = h2 - l2 + 1
        if m > n:
            return self.find_k_th(nums2, l2, h2, nums1, l1, h1, k)
        if m == 0:
            return nums2[l2 + k - 1]

        if k == 1:
            return min(nums1[l1], nums2[l2])

        na = min(int(k / 2), m)
        nb = k - na
        va = nums1[l1 + na - 1]
        vb = nums2[l2 + nb - 1]
        if va == vb:
            return va
        elif va < vb:
            return self.find_k_th(nums1, l1 + na, h1, nums2, l2, l2 + nb - 1, k - na)
        else:
            return self.find_k_th(nums1, l1, l1 + na - 1, nums2, l2 + nb, h2, k - nb)
