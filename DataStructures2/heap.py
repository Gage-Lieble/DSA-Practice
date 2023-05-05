# HEAP DATA STRUCTURE
'''
- A Binary Tree that satifies either Max Heap (largest to smallest) or Min Heap (smallest to largest)
- Applications:
    1. Priority Queue
    2. Dijkstra's Algorithm (finds shortest path between 2 nodes)
    3. Heap Sort (organization on the fly)
'''

def heapify(arr, size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < size and arr[i] < arr[i]:
        largest = l
    if r < size and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, size, largest)

def insert(arr, num):
    size = len(arr)
    if size == 0:
        arr.append(num)
    else:
        arr.append(num)
        for i in range((size//2) -1, -1, -1):
            heapify(arr, size, i)

def delete(arr, num):
    size = len(arr)
    i = 0
    for i in range(0, size):
        if num == arr[i]:
            break
    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(num)

    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr, len(arr), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

delete(arr, 4)
print("After deleting an element: " + str(arr))