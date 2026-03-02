from node import Node
from singly_linked_list import Single_linked_list

# Insert Node from end of the list
def add_tail(linked_list, data):
    new_node = Node(data)
    temp = linked_list.head
    if linked_list.head is None:
        linked_list.head = new_node
        return  
    elif temp.next is None:
        temp.next = new_node
    else:
        while temp:
            if temp.next is None:
                temp.next = new_node
                break
            temp = temp.next 

# Insert Node form begening of the list
def add_start(linked_list, data):
    new_node = Node(data)
    if linked_list.head is None:
        linked_list.head = new_node
    else:
        if linked_list.head is not None:
            temp = linked_list.head
            linked_list.head = new_node
            linked_list.head.next = temp
            
# Add Node between Nodes
def insert_before(linked_list, target, data):
    new_node = Node(data)
    

# Printing list
def printList(linkedList):
    temp = linkedList.head
    while temp:
        print(temp.data, end="-->")
        temp = temp.next
    print("None")

ll = Single_linked_list()
add_tail(ll, 10)
add_tail(ll, 20)
add_tail(ll, 30)
add_tail(ll, 40)
add_start(ll, 00)
add_start(ll, "start")
printList(ll)
# print(ll.head.data)