class Node:

    def __init__(self,data=None,next=None):

        self.data=data
        self.next=None

def deleteNode(head,key):

    while head:
        if head.data==key:
            break
        else:
            prev=head
            head = head.next

    prev.next = head.next
    head=None

    return head

def construct():
    first = Node(1)
    second = Node(14)
    third = Node(15)
    fourth = Node(16)
    fifth = Node(17)
    sixth = Node(18)

    head = first
    first.next =second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    return head

def printList(head):

    while head:
        print(head.data,end=" ")
        head=head.next

head = construct()
print("list before\n")
printList(head)
print("\n")
deleteNode(head,14)
print("after deletion")
printList(head)
