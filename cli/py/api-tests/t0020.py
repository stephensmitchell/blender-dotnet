import clr
clr.AddReference("System.Collections")  # Add reference to the System.Collections assembly
from System.Collections import Hashtable
# Create a Hashtable
hash_table = Hashtable()
# Add key-value pairs to the Hashtable
hash_table["Name"] = "John"
hash_table["Age"] = 30
hash_table["Country"] = "USA"
# Print key-value pairs in the Hashtable
print("Key-Value pairs in the Hashtable:")
for key in hash_table.Keys:
    print(f"{key}: {hash_table[key]}")
