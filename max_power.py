def max_power(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    r = n % 3
    k = n // 3
    if r == 0:
        return 3 ** k
    elif r == 1:
        return 3 ** (k - 1) * 4
    else:  # r == 2
        return (3 ** k) * 2


if __name__ == "__main__":
    n = int(input())
    print(max_power(n))
