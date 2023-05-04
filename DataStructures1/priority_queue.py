# PRIORITY QUEUE DATA STRUCTURE
'''
- Works like regular queue except each node has a priority value of importance
- Applications:
    1. Dijkstra's algorithm (Finding shortest path between 2 nodes)
    2. Load balancing and interupt handling in OS
'''

def heapify(arr, size, i):
    largest = i # I is highest priorty index
    l = 2 * i + 1
    r = 2 * i + 2

    # print(i, '--', l, r, '---', arr, size)
    if l < size and arr[i] < arr[l]: # checks if follwing value is higher priority
        largest = l
    if r < size and arr[largest] < arr[r]: # Checks if follwing value after preivous is higher priorty
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swaps to make highest priority 0 index
        heapify(arr, size ,largest)

def insert(arr, new_num):
    size = len(arr)
    if size == 0:
        arr.append(new_num)
    else:
        arr.append(new_num)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size, i)

def delete(arr, num):
    size = len(arr)
    i = 0 
    for i in range(0, size):
        if num == arr[i]:
            break
    arr[i], arr[size-1] = arr[size-1], arr[i] # Switches desired value to end opf array to be deleted
    arr.remove(size - 1)
    for i in range((len(arr) // 2) - 1, -1,-1):
        heapify(arr, len(arr), i)


array = []

insert(array, 3)
insert(array, 4)
insert(array, 9)
insert(array, 5)
insert(array, 2)

print(f"Max-Heap: {str(array)}")

delete(array, 4)
print(f"New Queue after delete: {str(array)}")
