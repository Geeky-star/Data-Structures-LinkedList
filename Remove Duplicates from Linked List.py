class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

def construct():

    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(2)
    fifth = Node(5)

    head = first
    first.next=second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    return head

def removeDuplicates(head):

    l = []
    while head:
        prev=head
        head=head.next
        if head.data in l:
            prev.next=head.next
            head=None
           
        else:
            l.append(head.data)
            head=head.next

    return head

def printList(head):
    while head:
        print(head.data,end=" ")
        head=head.next


head = construct()
printList(head)
print("\n")
removeDuplicates(head)
printList(head)

