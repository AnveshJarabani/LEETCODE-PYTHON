# merge k sorted --
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def merge(lst1, lst2):
            dummy = ListNode()
            cur_node = dummy
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    cur_node.next = lst1
                    lst1, cur_node = lst1.next, cur_node.next
                else:
                    cur_node.next = lst2
                    lst2, cur_node = lst2.next, cur_node.next
            if lst1:
                cur_node.next = lst1
            else:
                cur_node.next = lst2
            return dummy.next

        result = lists[0]
        for i in lists[1:]:
            result = merge(result, i)
        return result


# combination sum
class Solution:
    def combinationSum(self, lst: List[int], target: int) -> List[List[int]]:
        def back_tracker(i=0, cur=[], sum=0):
            if sum == target:
                result.append(cur[:])
                return
            elif sum > target or i >= len(lst):
                return
            cur.append(lst[i])
            back_tracker(i, cur, sum + lst[i])
            cur.pop()
            back_tracker(i + 1, cur, sum)

        result = []
        back_tracker()
        return result
