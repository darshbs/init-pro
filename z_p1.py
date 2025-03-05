class Solution:
    def cardboards(self, arr):
        # code here
        
        appearences = {}
        s, p = 0, 0 
        
        for piece in arr:
            if piece in appearences:
                appearences[piece] += 1
            else:
                appearences[piece] = 1
        
        for piece in appearences.values():
            s += piece // 4
            p += (piece % 4) // 2
            
        rectangle = p // 2
        
        return abs(s - rectangle)
    

o = Solution()
print(o.cardboards([1, 2, 2, 3, 3, 4, 1, 2, 6, 6, 5, 4, 2]))

