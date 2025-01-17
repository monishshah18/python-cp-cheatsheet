
# Space/Time O(n), O(nLogn)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return

        # sort intervals
        intervals.sort(key = lambda x:x[0])

        # start merged list and go through intervals
        merged = [intervals[0]]
        
        for i in intervals:
            ms, me = merged[-1]
            s, e = i
            
            if s <= me:
                merged[-1] = (ms, max(me, e))
            else:
                merged.append(i)
                
        return merged
        