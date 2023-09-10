def calc_drone_min_energy(route):
    if len(route) == 1:
        return 0
    fuel = 0
    min_egy = float("inf")
    for i in range(1, len(route)):
        fuel += route[i - 1][2] - route[i][2]
        min_egy = min(min_egy, fuel)
    return -min_egy if min_egy < 0 else 0


def absSort(arr):
    arr.sort(key=lambda x: (abs(x), -x))
    for r in range(1, len(arr)):
        if arr[r - 1] > arr[r] and arr[r - 1] + arr[r] == 0:
            arr[r - 1], arr[r] = arr[r], arr[r - 1]
    return arr


arr = [2, -7, -2, -2, 0]
print(absSort(arr))
