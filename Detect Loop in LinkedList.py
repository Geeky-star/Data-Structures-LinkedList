def detectLoop(head):
    
    a=set()
    temp=head
    while temp:
        if temp in a:
            return True
            
        else:
            a.add(temp)
            temp=temp.next
            
    return False
