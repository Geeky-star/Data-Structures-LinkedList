def addLists(first, second):
    
    num1=""
    num2=""

    while first:
        num1+=str(first.data)
        first=first.next

    while second:
        num2+=str(second.data)
        second=second.next
 
    num=int(num1)+int(num2)
    
    l=str(num).split()
    
    curr=Node(l[0])
    for i in l:
        curr.next = Node(i)
        curr=curr.next
    
    return curr
