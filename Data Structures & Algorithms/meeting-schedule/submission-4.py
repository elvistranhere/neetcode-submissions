class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        totalInterval = Interval(intervals[0].start, intervals[0].end)
        for i in range(1, len(intervals)):
            if totalInterval.end > intervals[i].start:
                return False
            totalInterval.end = max(intervals[i].end, totalInterval.end)
            totalInterval.start = min(intervals[i].start, totalInterval.start)
        return True
