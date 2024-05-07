import clr
clr.AddReference("System.Collections")  # Add reference to the System.Collections assembly
from System.Collections.Generic import Dictionary
# Create a dictionary
dictionary = Dictionary[str, int]()
# Add key-value pairs to the dictionary
dictionary["apple"] = 5
dictionary["banana"] = 3
dictionary["orange"] = 7
# Get the number of key-value pairs in the dictionary
print("Number of items in the dictionary:", dictionary.Count)
# Check if a key exists in the dictionary
print("Key 'apple' exists:", dictionary.ContainsKey("apple"))
# Check if a value exists in the dictionary
print("Value 3 exists:", dictionary.ContainsValue(3))
# Clear all key-value pairs from the dictionary
dictionary.Clear()
# Print number of items in the dictionary after clearing
print("Number of items in the dictionary after clearing:", dictionary.Count)
