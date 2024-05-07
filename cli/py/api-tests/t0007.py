import clr
clr.AddReference("System.Drawing")
from System.Drawing import Point
# Create an instance of Point class
point = Point(10, 20)
# Access properties of the point
print("X coordinate:", point.X)
print("Y coordinate:", point.Y)
