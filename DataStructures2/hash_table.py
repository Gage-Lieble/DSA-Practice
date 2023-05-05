# HASH TABLE DATA STRUCTURE
'''
- A data structure that stores data in a KEY & VALUE pair
- Applications:
    1. Constant time lookup and insertion
    2. Cryptography (Cyber security)
    3. Storing indexed data
'''

hash_table = [[],] * 10 #[[], [], [], [], [], [], [], [], [], []]

def check_prime(n):
    if n == 1 or n == 0:
        return 0
    
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def get_prime(n): # Uses prime numbers to avoid collision 
    if n % 2 == 0:
        n += 1

    while not check_prime(n):
        n += 2
    
    return n

def hash_function(key):
    capacity = get_prime(10)
    return key % capacity

def insert_data(key, data):
    index = hash_function(key)
    hash_table[index] = [key, data]

def remove_data(key):
    index = hash_function(key)
    hash_table[index] = 0


insert_data(123, "apple")
insert_data(432, "mango")
insert_data(213, "banana")
insert_data(654, "guava")

print(hash_table)

remove_data(123)

print(hash_table)