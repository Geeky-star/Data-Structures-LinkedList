

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length=0
        root = head
        while head:
            length+=1
            head=head.next
            
        i=0
        while root and i!=length//2:
            i+=1
            root=root.next
            
        
        return root
        
