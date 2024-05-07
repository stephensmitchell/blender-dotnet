import clr
clr.AddReference("System.IO")  # Add reference to the System.IO assembly
from System.IO import File
# Check if a file exists
file_path = "t0000.py"
if File.Exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
