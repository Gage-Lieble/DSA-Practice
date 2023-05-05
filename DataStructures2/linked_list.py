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
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, new_data):
        new_node = Node(new_data) # creates node

        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev, new_data):

        if prev is None:
            print("That node doesn't exist")
            return
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node
    
    def insertEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        
        last.next = new_node
    
    def delete(self, posistion):

        if self.head is None:
            return
        
        temp = self.head

        if posistion == 0:
            self.head = temp.next
            temp = None
            return     
        
        for i in range(posistion-1): # traversal
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def sortList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    
                    index = index.next
                current = current.next

    def printList(self):
        temp = self.head
        while(temp):
            print(f"{str(temp.data)} ")
            temp = temp.next

if __name__ == '__main__':
    
    # linked_list = LinkedList()

    # linked_list.head = Node(1) # this becomes head
    # sec = Node(2)
    # thr = Node(3)

    # linked_list.head.next = sec # sets next after head to sec
    # sec.next = thr # secs next to thr

    # while linked_list.head != None: # While head is not at end
    #     print(linked_list.head.item)
        
    #     linked_list.head = linked_list.head.next # Updates head location



    llist = LinkedList()
    llist.insertEnd(1)
    llist.insertStart(2)
    llist.insertStart(3)
    llist.insertEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.delete(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortList(llist.head)
    print("Sorted List: ")
    llist.printList()