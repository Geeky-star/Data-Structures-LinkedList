# Can be optimized

def insert(root,item):
    node=Node(item)
    if not root:
        return node
        
    ptr = root
    while ptr.next!=None:
        ptr=ptr.next
        
    ptr.next=node
    
    return root

def segregate(head):
    
    arr = []
    
    while head:
        arr.append(head.data)
        head=head.next
        
    arr=sorted(arr)
    root = None   
    for i in arr:
        root = insert(root,i)
        
    return root
