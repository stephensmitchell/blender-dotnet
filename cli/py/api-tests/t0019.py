import clr
clr.AddReference("System.Collections")  # Add reference to the System.Collections assembly
from System.Collections import Stack
# Create a Stack
stack = Stack()
# Push elements onto the Stack
stack.Push("First")
stack.Push("Second")
stack.Push("Third")
# Pop elements from the Stack and print them
print("Popped elements from the Stack:")
while stack.Count > 0:
    print(stack.Pop())
