class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        filas = len(text1)
        columnas = len(text2)

        dp = []

        for _ in range(filas + 1):
            dp.append([0] * (columnas + 1))

        for i in range(1, filas + 1):
            for j in range(1, columnas + 1):

                letra1 = text1[i - 1]
                letra2 = text2[j - 1]

                if letra1 == letra2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    arriba = dp[i - 1][j]
                    izquierda = dp[i][j - 1]
                    dp[i][j] = max(arriba, izquierda)

        return dp[filas][columnas]