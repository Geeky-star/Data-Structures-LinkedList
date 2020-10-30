
def insert(root,item):

    temp=Node(item)
    if not root:
        return temp

    else:
        ptr=root
        while ptr.next!=None:
            ptr=ptr.next

        ptr.next=temp
        
    return root
    
def removeDuplicates(head):
    s=[]
    s.append(head.data)
    while head and head.next:
        if head.next.data in s:
            head.next=head.next.next
           
        else:
            s.append(head.next.data)
            head=head.next
            
    root=None
    for i in s:
        root=insert(root,i)
        
    return root

