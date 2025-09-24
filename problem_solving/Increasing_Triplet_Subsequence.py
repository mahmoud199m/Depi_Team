class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for i,n in enumerate(nums):
            if i < len(nums) -1 :
                if nums[i] < nums[i+1]:
                    s += 1
                else: s = 0
                if s == 2:
                    return True
        return False
