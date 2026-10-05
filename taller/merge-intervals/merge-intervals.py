class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        resultado = [intervals[0]]

        for i in range(1, len(intervals)):
            if resultado[-1][1] >= intervals[i][0]:
                resultado[-1][1] = max(resultado[-1][1], intervals[i][1])
            else:
                resultado.append(intervals[i])

        return resultado