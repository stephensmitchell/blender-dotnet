import clr
clr.AddReference("System.Collections")  # Add reference to the System.Collections assembly
from System.Collections.Generic import Dictionary
# Create a dictionary
dictionary = Dictionary[int, str]()
# Add key-value pairs to the dictionary
dictionary[1] = "One"
dictionary[2] = "Two"
dictionary[3] = "Three"
# Print all key-value pairs in the dictionary
print("Key-Value pairs in the dictionary:")
for key, value in dictionary.items():
    print(f"{key}: {value}")
# Access value by key
print("Value for key 2:", dictionary[2])
# Modify value for existing key
dictionary[2] = "New Two"
# Check if a key exists in the dictionary
print("Key 4 exists:", 4 in dictionary)
# Remove a key-value pair from the dictionary
#del dictionary[3]
# Print updated dictionary
print("Updated dictionary after removal:")
for key, value in dictionary.items():
    print(f"{key}: {value}")
print("Updated dictionary after removal:")
for key in dictionary.Keys:
    print(f"{key}: {dictionary[key]}")
    # Print updated dictionary after removal
print("Updated dictionary after removal:")
for key in dictionary.Keys:
    print(f"{key}: {dictionary[key]}")
