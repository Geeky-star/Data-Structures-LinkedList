def isCircular(head):
    if head==None:
        return "0"
        
    first = head.next
    
    while first is not head and first!=None:
        first=first.next
    
    return head==first
