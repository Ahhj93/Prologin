from typing import List


def ordre(k: int, n: int, tailles: List[int]) -> None:
    # Triez la liste initiale
    sorted_tailles: List[int] = sorted(tailles)

    # Vérifiez si la liste triée est obtenue en effectuant des échanges avec un écart de k
    for i in range(n):
        if abs(tailles.index(sorted_tailles[i]) - i) % k != 0:
            print("NON")
            return

    print("OUI")


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    ordre(k, n, tailles)
