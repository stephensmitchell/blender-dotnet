import clr
clr.AddReference("System")  # Add reference to the System assembly
from System import Math
# Use methods from the Math class
print("Square root of 25:", Math.Sqrt(25))
print("Pi value:", Math.PI)
