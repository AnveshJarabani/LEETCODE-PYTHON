def calc_drone_min_energy(route):
    if len(route) == 1:
        return 0
    z = []
    # O(n)
    for i in route:
        z.append(i[2])

    kWh = 0
    min_egy = float("inf")
    # O(n)
    for i in range(1, len(z)):
        kWh += z[i - 1] - z[i]
        min_egy = min(min_egy, kWh)
    return -min_egy if min_egy < 0 else 0


def absSort(arr):
    arr.sort(key=lambda x: abs(x))
    for r in range(1, len(arr)):
        if arr[r - 1] > arr[r] and arr[r - 1] + arr[r] == 0:
            arr[r - 1], arr[r] = arr[r], arr[r - 1]
    return arr


arr = [2, -7, -2, -2, 0]
print(absSort(arr))
