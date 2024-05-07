import clr
clr.AddReference("System")  # Add reference to the System assembly
from System import String
# Create a string
str1 = String("Hello, ")
str2 = String("world!")
# Concatenate strings
result = String.Concat(str1, str2)
print("Concatenated string:", result)
# Get length of string
#print("Length of string:", result.Length)
# Access characters by index
print("Character at index 7:", result[7])
# Convert string to uppercase
# upper_str = result.ToUpper()
# print("Uppercase string:", upper_str)
# Convert string to lowercase
# lower_str = result.ToLower()
# print("Lowercase string:", lower_str)
# Check if string starts with a specific substring
# print("Starts with 'Hello':", result.StartsWith("Hello"))
# Check if string ends with a specific substring
# print("Ends with 'world!':", result.EndsWith("world!"))
# Create a string
sentence = String("This is a sentence.")
# Split the string by space
words = sentence.Split(' ')
# Print each word
print("Words in the sentence:")
for word in words:
    print(word)
# Join the words with a different separator
new_sentence = String.Join('-', words)
print("Joined sentence with '-':", new_sentence)
# Create two strings
str1 = String("Hello")
str2 = String("hello")
# Check if strings are equal ignoring case
# print("Strings are equal (ignore case):", str1.Equals(str2, StringComparison.OrdinalIgnoreCase))
# Check if strings are equal with case sensitivity
print("Strings are equal (case sensitive):", str1.Equals(str2))