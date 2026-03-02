class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        def kth(k):
            i = j = 0

            while True:
                # se uno dei due array è finito
                if i == len(nums1):
                    return nums2[j + k - 1]
                if j == len(nums2):
                    return nums1[i + k - 1]

                if k == 1:
                    return min(nums1[i], nums2[j])

                half = k // 2

                new_i = min(i + half, len(nums1)) - 1
                new_j = min(j + half, len(nums2)) - 1

                if nums1[new_i] <= nums2[new_j]:
                    k -= (new_i - i + 1)
                    i = new_i + 1
                else:
                    k -= (new_j - j + 1)
                    j = new_j + 1

        total = len(nums1) + len(nums2)

        if total % 2:
            return kth(total // 2 + 1)
        else:
            return (
                kth(total // 2) +
                kth(total // 2 + 1)
            ) / 2