from time import time
import numpy as np
import heapq
arr=np.random.randint(0,1000,10000000)
def timeit(func):
    def wrapper(*args, **kwargs):
        start=time()
        result = func(*args, **kwargs)
        print(f'{round(time()-start,2)} seconds - {func.__name__}') 
        return result
    return wrapper
class Solution:
    def freq_mapper(self,arr):
        count_map={}
        for i in arr:
            count_map[i]=1+count_map.get(i,0)
        return count_map
    @timeit
    def k_freq_by_count(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        result=list(set(arr))
        result.sort(key=lambda x:count_map[x],reverse=True)
        return 
    @timeit
    def k_freq_by_count_heap_max(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        heapq.nlargest(k,count_map.keys(),count_map.get)
        return 
    @timeit
    def k_freq_by_count_heap_min(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        min_heap=[]
        for num,count in count_map.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result = [i for _,i in min_heap]
        return 
    @timeit
    def k_freq_bucket_sort(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        bucket_map={i:[] for i in range(len(arr)+1)}
        for num,count in count_map.items():
            bucket_map[count].append(num)
        result=[]
        for i in range(len(arr),0,-1):
            for num in  bucket_map[i]:
                result.append(num)
                if len(result)==k:
                    return
        return

Solution().k_freq_by_count(arr)
Solution().k_freq_by_count_heap_max(arr)
Solution().k_freq_by_count_heap_min(arr)
Solution().k_freq_bucket_sort(arr)