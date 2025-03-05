class Solution:
    def canSort(self, arr, frozen):
        
        indices = []
        for i in range(len(arr)):
            if frozen[i] == 0:
                indices.append(i)

        values = []
        for i in indices:
            values.append(arr[i])

        values.sort()

        sorted_arr = arr[:]
        for i in range(len(indices)):
            sorted_arr[indices[i]] = values[i]

        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i] > sorted_arr[i + 1]:
                return False
        return True

solution = Solution()
print(solution.canSort([0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1]))  # True
print(solution.canSort([1, 0, 0], [0, 0, 1]))  # False
print(solution.canSort([1, 0, 1], [0, 0, 0]))  # True
print(solution.canSort([1, 0, 1], [1, 0, 0]))  # False