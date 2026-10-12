"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.end)
        res = 0
        while intervals:
            prevEnd = intervals[0].end
            newSchedule = []
            for interval in intervals[1:]:
                if interval.start >= prevEnd:
                    prevEnd = interval.end
                else:
                    newSchedule.append(interval)
            res +=1
            intervals = newSchedule
        return res 
