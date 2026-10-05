class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        soluciones = []

        def construir(indice, suma_actual, combinacion):

            if suma_actual == target:
                soluciones.append(combinacion.copy())
                return

            if suma_actual > target:
                return

            for posicion in range(indice, len(candidates)):

                numero = candidates[posicion]

                combinacion.append(numero)

                construir(
                    posicion,
                    suma_actual + numero,
                    combinacion
                )

                combinacion.pop()

        construir(0, 0, [])

        return soluciones