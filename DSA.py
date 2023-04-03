#Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs
arr = [2, 4, 5, 7, 8, 9]
target_sum = 12
pairs = find_pairs(arr, target_sum)
print(pairs)
#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)
#3) Write a program to check if two strings are a rotation of each other?
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if str2 in temp:
        return True
    else:
        return False
str1 = "abcde"
str2 = "cdeab"
if are_rotations(str1, str2):
    print("The two strings are rotations of each other")
else:
    print("The two strings are not rotations of each other")
#4)Write a program to print the first non-repeated character from a string?
def first_non_repeated_char(string):
    char_count = {}
    
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    
    for char in string:
        if char_count[char] == 1:
            return char
    
    
    return None
string = "hello world"
result = first_non_repeated_char(string)
if result:
    print(f"The first non-repeated character in '{string}' is '{result}'")
else:
    print(f"There is no non-repeated character in '{string}'")

#5)Read about the Tower of Hanoi algorithm. Write a program to implement it.
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)
n = 3  
tower_of_hanoi(n, 'A', 'B', 'C')
#6) Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def postfix_to_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
    
    return stack.pop()

expression = "23+5*"
prefix_expression = postfix_to_prefix(expression)
print("Prefix expression:", prefix_expression)
#7)Write a program to convert prefix expression to infix expression.
def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
   
    for char in reversed(expression):
        if char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append('({} {} {})'.format(operand1, char, operand2))
        else:
            stack.append(char)
    
    return stack.pop()

expression = "+ * 2 3 5"
infix_expression = prefix_to_infix(expression)
print("Infix expression:", infix_expression)

#8)Write a program to check if all the brackets are closed in a given code snippet.
def check_brackets(code):
    stack = []
    opening_brackets = set(['(', '{', '['])
    closing_brackets = set([')', '}', ']'])
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if brackets_map[char] != stack.pop():
                return False
    
    return not stack

code_snippet = "{ for(int i = 0; i < n; i++) { printf(""); } }"
if check_brackets(code_snippet):
    print("All brackets are closed.")
else:
    print("Some brackets are not closed.")

#9)Write a program to reverse a stack.
def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top)

stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)

reverse_stack(stack)
print("Reversed stack:", stack)

#10)Write a program to find the smallest number using a stack.
class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.items:
            return None
        item = self.items.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(4)
stack.push(1)

print("Smallest number in the stack:", stack.get_min())

    


