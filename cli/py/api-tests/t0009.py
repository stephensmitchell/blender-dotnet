import os
import clr
# Add reference to the System.IO namespace
clr.AddReference("System.IO")
# Import the System.IO namespace
from System.IO import Directory, File
# Get the current working directory
current_directory = os.getcwd()
# Create a directory in the current working directory
directory_path = os.path.join(current_directory, "Temp")
Directory.CreateDirectory(directory_path)
# Create a file in the directory
file_path = os.path.join(directory_path, "test.txt")
File.WriteAllText(file_path, "Hello, .NET from Python!")
# Get files in the directory
files = Directory.GetFiles(directory_path)
# Print the files
for file in files:
    print(file)
# Delete the file
#File.Delete(file_path)
# Delete the directory
#Directory.Delete(directory_path)
