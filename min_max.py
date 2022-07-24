def minimum(arr):
    n = len(arr)
    min = arr[0]
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    return min


def maximum(arr):
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1, 3, 45, -5, 0, 345, -32]

print(minimum(arr))
print(maximum(arr))
