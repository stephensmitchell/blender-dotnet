import clr
clr.AddReference("System.Collections")  # Add reference to the System.Collections assembly
from System.Collections import Queue
# Create a Queue
queue = Queue()
# Enqueue elements into the Queue
queue.Enqueue("Apple")
queue.Enqueue("Banana")
queue.Enqueue("Orange")
# Dequeue elements from the Queue and print them
print("Dequeued elements from the Queue:")
while queue.Count > 0:
    print(queue.Dequeue())
