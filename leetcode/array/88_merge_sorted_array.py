from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums_copy = nums1[:]
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums_copy[i] < nums2[j]:
                nums1[k] = nums_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = nums_copy[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

        return
