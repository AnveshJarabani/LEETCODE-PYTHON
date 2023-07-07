def TwoSum(arr):
    recieved_arr=arr.copy()
    target=arr[0]
    arr.pop(0)
    arr.sort()
    x,y=0,len(arr)-1
    lst=[]
    while x<len(arr) and y>x:
        i,m=arr[x],arr[y]
        if target<i+m:
            y-=1
            continue
        elif target>i+m:
            x+=1
            continue
        else:
            if recieved_arr.index(i)<=recieved_arr.index(m):
                lst.append([i,m])
                x+=1
            else:
                lst.append([m,i])
                x+=1
    
    if str=="":
        return -1
    else:
        return str.strip()


print(TwoSum([17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]))



def split_array_evenly(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return None

    target_sum = total_sum // 2
    subset = []
    result = []

    def find_subsets_with_sum(index, current_sum):
        if current_sum == target_sum:
            result.append(subset[:])
        elif current_sum < target_sum and index < len(nums):
            num = nums[index]
            subset.append(num)
            find_subsets_with_sum(index + 1, current_sum + num)
            subset.pop()
            find_subsets_with_sum(index + 1, current_sum)

    find_subsets_with_sum(0, 0)
    return result

# Example usage
nums = [1, 5, 11, 5]
split_sets = split_array_evenly(nums)
if split_sets:
    print("Possible split:")
    print("Set 1:", split_sets[0])
    print("Set 2:", split_sets[1])
else:
    print("No even split possible.")