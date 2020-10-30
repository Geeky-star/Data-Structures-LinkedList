def getNthfromEnd(head,n):
    
    a = []
    
    while head:
        a.append(head.data)
        head=head.next
        
    if n>len(a):
        return -1
        
    else:
        return a[len(a)-n]
