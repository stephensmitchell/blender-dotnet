import clr
clr.AddReference("System")  # Add reference to the System assembly
from System import DateTime
# Create a DateTime object
current_time = DateTime.Now
# Print current date and time
print("Current date and time:", current_time)
