# 4.1 Write code to sum a list of numbers using recursion.

def rsum(array: list[int], idx: int = 0) -> int:
    if idx >= len(array):
        return 0 
    return array[idx] + rsum(array, idx + 1)


if __name__ == '__main__':
    array = [int(x) for x in input("Input list to sum: ").split()]
    print(f"Sum({array}) -> {rsum(array)}")
