class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        eliminados = 0
        fin_actual = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < fin_actual:
                eliminados += 1
            else:
                fin_actual = intervals[i][1]

        return eliminados