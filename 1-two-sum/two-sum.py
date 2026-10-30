class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        output = []
        for i in range(len(nums)):
                goal = target - nums[i]
                if goal in seen:
                    output.append(seen[goal])
                    output.append(i)
                    return output
                seen[nums[i]] = i
            

                                              