def insert(root,item):
    
    if not root:
        return Node(item)
    
    node = Node(item)
    curr = root
    while curr.next!=None:
        curr = curr.next
        
    curr.next = node
    
    return root
    

def addOne(head):
    
    num=""
    
    while head:
        num+=str(head.data)
        head=head.next
        
    num = int(num)+1    
    l = str(num).split()
    
    root=None
    for i in l:
        root=insert(root,i)
        
    return root
    
