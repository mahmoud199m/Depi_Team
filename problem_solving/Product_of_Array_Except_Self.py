class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        f = 1
        li = []
        for i,n in enumerate(nums):

            for i2,n2 in enumerate(nums):
                if i2 != i:
                    f *= n2
            li.append(f)
            f = 1
        return li
    


            