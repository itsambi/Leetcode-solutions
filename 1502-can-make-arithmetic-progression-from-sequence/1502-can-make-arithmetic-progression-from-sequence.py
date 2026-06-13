class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()  
        diff = arr[0] - arr[1] 
        x = 0 
        count = 0
        for x in range(len(arr)-1):
            if arr[x]-arr[x+1] == diff:
                count+=1 
            if count == len(arr)-1:
                return True 
        return False