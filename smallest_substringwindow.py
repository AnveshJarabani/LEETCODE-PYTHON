arr = ["x", "y", "z"]
str = "xyyzyzyx"


class Solution:
    def min_window(self, arr, str):
        if not str:
            return ""
        count_map = {}
        for i in arr:
            count_map[i] = 1 + count_map.get(i, 0)
        s_map = {}
        have, need = 0, len(count_map)
        l = 0
        res_len = float("infinity")
        for r in range(len(str)):
            char = str[r]
            s_map[char] = 1 + count_map(char, 0)
            if char in count_map and s_map[char] == count_map[char]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                s_map[str[l]] -= 1
                if str[l] in count_map and s_map[char] < count_map[char]:
                    have = -1
                l += 1

        return str[res[0], res[1] + 1] if res_len != float("infinity") else ""


print(Solution().min_window(arr, str))
