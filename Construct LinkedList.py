class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data,end="->")
        head = head.next
    print("None")

def construct():

    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head = first
    first.next=second
    second.next = third
    third.next = fourth

    return head

if __name__ == '__main__':

    head = construct()
    printList(head)

