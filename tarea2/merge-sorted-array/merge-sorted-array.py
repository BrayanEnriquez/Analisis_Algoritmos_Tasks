class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        arr = nums1[:m]
        arr += nums2[:n]

        for i in range(len(arr)):
            for j in range(len(arr)-i-1):

                if arr[j] > arr[j+1]:

                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        for i in range(len(arr)):
            nums1[i] = arr[i]

        