# LINKED LIST DATA STRUCTURE
'''
- An array of nodes that contain data as well as a pointer to next node
- Applications:
    1. Dynamic memory allocation
    2. Hash tables, Graphs
    3. Undo functions
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    
    linked_list = LinkedList()

    linked_list.head = Node(1) # this becomes head
    sec = Node(2)
    thr = Node(3)

    linked_list.head.next = sec # sets next after head to sec
    sec.next = thr # secs next to thr

    while linked_list.head != None: # While head is not at end
        print(linked_list.head.item)
        
        linked_list.head = linked_list.head.next # Updates head location