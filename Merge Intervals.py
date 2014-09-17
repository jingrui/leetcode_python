# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0: return []
        ret = [intervals[0]]
        del intervals[0]
        insert = False
        for itv in intervals:
            indx = 0
            while indx < len(ret):
                existing = ret[indx]
                itv1 = self.overlap(existing, itv)
                if itv1 != None:
                    itv = itv1
                    del ret[indx]
                else:
                    indx += 1

            ret.append(itv)

        for indx, ele in enumerate(ret):
            ret[indx] = [ele.start, ele.end]
        return ret
                
    
    def overlap(self, itv1, itv2):
        if self.include(itv1, itv2):
            return itv1
        elif self.include(itv2, itv1):
            return itv2
        elif itv2.start <= itv1.start <= itv2.end or itv2.start <= itv1.end <= itv2.end:
            itv1.start = min(itv1.start, itv2.start)
            itv1.end = max(itv1.end, itv2.end)
            return itv1
        else:
            return None
            
    def include(self, itv1, itv2):
        if itv1.start <= itv2.start and itv2.end <= itv1.end:
            return True
        else:
            return False

def listtoInt(l):
    for indx,itv in enumerate(l):
        l[indx] = Interval(itv[0], itv[1])
    return l

a = Solution()
l = [[2,3],[4,5],[6,7],[8,9],[1,10]]
l = listtoInt(l)
print a.merge(l)