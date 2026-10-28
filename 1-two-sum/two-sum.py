class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(len(nums)):
                new_curr = nums[j]
                if len(output) < 2:
                    if j != i:
                        if curr + new_curr == target:
                            output.append(i)
                            output.append(j)
        
        return output

                                              