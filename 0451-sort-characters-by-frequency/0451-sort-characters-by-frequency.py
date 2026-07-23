class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        ans = ""
        for ch , count in sorted(freq.items(),key = lambda x:x[1] ,reverse = True):
            ans += ch * count
        return ans    
         
        