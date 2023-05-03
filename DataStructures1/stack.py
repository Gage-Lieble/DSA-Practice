# STACK DATA STRUCTURE
'''
-Like a stack of plates you can only remove the Last item that was put into the stack (the top item)
-Applications
    1. Reverse word
    2.Compilers use stack to calculate expressions
    3.Browsers user stack to recall previous pages by saving former URLS in a stack
'''

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, val):
    stack.append(val)
    print(f"{val} was added to {stack} AND New TOP is {len(stack)-1}")
    

def pop(stack):
    if len(stack) > 0:
        return stack.pop()
    else:
        return 'stack is empty!'

stack = create_stack()
push(stack, '1')
push(stack, '2')
push(stack, '3')
push(stack, '4')
print('')
print(f'Original stack: {stack}')
print(f'Popped item: {pop(stack)}')
print(f'New Stack after pop: {stack}')
