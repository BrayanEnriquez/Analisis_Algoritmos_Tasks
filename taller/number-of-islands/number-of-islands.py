class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        filas = len(grid)
        columnas = len(grid[0])

        islas = 0

        for fila in range(filas):
            for columna in range(columnas):

                if grid[fila][columna] == "1":

                    islas += 1

                    cola = deque([(fila, columna)])

                    while cola:

                        f, c = cola.popleft()

                        if (
                            f < 0
                            or f >= filas
                            or c < 0
                            or c >= columnas
                            or grid[f][c] == "0"
                        ):
                            continue

                        grid[f][c] = "0"

                        cola.append((f + 1, c))
                        cola.append((f - 1, c))
                        cola.append((f, c + 1))
                        cola.append((f, c - 1))

        return islas