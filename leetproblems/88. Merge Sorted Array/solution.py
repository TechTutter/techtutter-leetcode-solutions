class Solution:
    """
    p1 = m - 1, p2 = n - 1, p = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1--
        else:
            nums1[p] = nums2[p2]
            p2--
        p--
    """
    def merge(self, nums1, m, nums2, n) -> None:
        i = m - 1
        j = n - 1
        
        for k in reversed(range(m+n)):
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1