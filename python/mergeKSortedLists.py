import sys
sys.setrecursionlimit(1000000)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while list1 or list2:
            if not list1 or not list2:
                if not list1:
                    res.append(list2.val)
                    list2 = list2.next
                else:
                    res.append(list1.val)
                    list1 = list1.next
            else:
                if list1.val < list2.val:
                    res.append(list1.val)
                    list1 = list1.next
                else:
                    res.append(list2.val)
                    list2 = list2.next
        ans = None
        while res:
            ans = ListNode(res[-1], ans)
            res.pop()
        return ans
            
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        twoLists, finalLists = [], []
        while lists:
            twoLists.append(lists[-1])
            lists.pop()
            if len(twoLists) == 2:
                finalLists.append(self.mergeTwoLists(twoLists[0], twoLists[1]))
                twoLists = []
        if twoLists:
            finalLists.append(twoLists[0])
        return finalLists[0] if len(finalLists) == 1 else self.mergeKLists(finalLists)

        
