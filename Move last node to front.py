def addtofront(head):

    first=head

    while head and head.next!=None:
        prev=head
        head=head.next

    head.next=first
    prev.next=None
    
    
    return head
        


root = addtofront(head)

while root:
    print(root.data)
    root=root.next

