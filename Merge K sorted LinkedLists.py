def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def insert(root,item):
            if not root:
                return ListNode(item)
            
            temp=ListNode(item)
            ptr = root
            while ptr.next!=None:
                ptr=ptr.next
                
            ptr.next=temp
            return root

        root=None
        a = []
    
        for i in range(len(lists)):
            head = lists[i]
            while head:
                a.append(head.val)
                head=head.next
            
        a = sorted(a)
        for i in a:
            root = insert(root,i)
        
        return root
