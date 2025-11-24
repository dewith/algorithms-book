# 4.1 Write code to sum a list of numbers using recursion.

def rsum(array: list[int]) -> int:
    if not len(array):
        return 0 
    return array[0] + rsum(array[1:])


if __name__ == '__main__':
    array = [4, 3, 2, 1]
    print(f"Sum({array}) -> {rsum(array)}")
