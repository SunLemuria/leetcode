def findMedianSortedArrays(nums1, nums2):
    total_length = len(nums1) + len(nums2)
    is_odd = total_length % 2
    split_location = int(total_length / 2) + 1
    i = j = 0
    merged_array = list()
    while len(merged_array) < split_location:
        if i < len(nums1):
            if j < len(nums2):
                if nums1[i] <= nums2[j]:
                    merged_array.append(nums1[i])
                    i += 1
                else:
                    merged_array.append(nums2[j])
                    j += 1
            else:
                merged_array.append(nums1[i])
                i += 1
        else:
            if j < len(nums2):
                merged_array.append(nums2[j])
                j += 1
            else:
                break

    return merged_array[-1] if is_odd else (merged_array[-1] + merged_array[-2]) / 2


print(findMedianSortedArrays([1, 2], [2, 3, 5, 6]))
