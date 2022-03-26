# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getnum(ll):
    if ll.next == None:
        return ll.val
    return (getnum(ll.next) * 10) + ll.val

def numtolist(n):
    return [int(i) for i in list(str(n))]
    
def createll(lin, ind, acc):
    if len(lin)-ind == 0:
        return acc
    return createll(lin, ind+1, ListNode(lin[ind], acc))
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return createll(numtolist(getnum(l1) + getnum(l2)), 0, None)
