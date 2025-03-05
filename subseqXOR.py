class Solution:
    def helper(self, arr, curInd, curXor, count, freqMap):
        if curInd == len(arr):
            if count > 0:
                freqMap[curXor] = freqMap.get(curXor, 0) + 1
            return
        # Include the current element
        self.helper(arr, curInd + 1, curXor ^ arr[curInd], count + 1, freqMap)
        # Exclude the current element
        self.helper(arr, curInd + 1, curXor, count, freqMap)

    def xorPair(self, arr):
        freqMap = {}
        self.helper(arr, 0, 0, 0, freqMap)

        MOD = 10**9 + 7
        ans = 0

        for count in freqMap.values():
            pairs = count * (count - 1) // 2
            ans = (ans + pairs % MOD) % MOD

        return ans

array = [1,2,3]
sol = Solution()

print(sol.xorPair(array))