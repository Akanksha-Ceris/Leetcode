class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans =[ intervals[0]]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            last_interval=ans[-1]
            last_end = last_interval[1]
            if start <= last_end:
                last_interval[1] = max(last_end,end)
            else:
                ans.append(interval)  
        return ans          
        