class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1



        while (numbers[i] + numbers[j] != target):
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
        l = []
        if (j<i):
            l.append(j+1)
            l.append(i+1)
        else:
            l.append(i+1)
            l.append(j+1)
        return l