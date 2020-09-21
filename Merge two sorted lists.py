class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        L3= ListNode()
        prev = L3
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                prev.next=l1
                l1=l1.next
            else:
                prev.next=l2
                l2=l2.next

            prev=prev.next
        
        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next=l1

        return L3.next
