class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_dict_a = {}
        hash_dict_b = {}
        for i, j in zip(s, t):
            if i not in hash_dict_a:
                hash_dict_a[i] = j
            elif hash_dict_a[i] != j:
                return False
            if j not in hash_dict_b:
                hash_dict_b[j] = i
            elif hash_dict_b[j] != i:
                return False

        return True


# ANOTHER SOLUTION --


def isIsomorphic(self, s: str, t: str) -> bool:
    zipped_set = set(zip(s, t))
    return len(zipped_set) == len(set(s)) == len(set(t))


print(Solution().isIsomorphic("badc", "baba"))
