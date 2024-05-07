import clr
clr.AddReference("System")  # Add reference to the System assembly
from System import Math
# Use built-in Math functions
print("Square root of 25:", Math.Sqrt(25))
print("Absolute value of -10:", Math.Abs(-10))
print("Sin(π/2):", Math.Sin(Math.PI / 2))
print("Cos(0):", Math.Cos(0))
from System import DateTime
# Use built-in DateTime methods
current_time = DateTime.Now
print("Current date and time:", current_time)
print("Year:", current_time.Year)
print("Month:", current_time.Month)
print("Day:", current_time.Day)
print("Hour:", current_time.Hour)
print("Minute:", current_time.Minute)
print("Second:", current_time.Second)
name = "adsf"
age = 9
print(f"Hello, {name}! You are {age} years old.")
import clr
clr.AddReference("System")  # Add reference to the System assembly
from System import Math
# Use built-in Math constants
print("Pi value:", Math.PI)
print("Euler's number:", Math.E)
#print("Infinity:", Math.Infinity)
#print("Negative Infinity:", Math.NegativeInfinity)
from System import String
# Use built-in String methods
str1 = String("Hello, world!")
print("Original string:", str1)
print("Length of string:", str1.Length)
print("Uppercase string:", str1.ToUpper())
print("Lowercase string:", str1.ToLower())
print("Substring from index 7:", str1.Substring(7))
print("Index of 'world':", str1.IndexOf("world"))
print("Replace 'world' with 'Python':", str1.Replace("world", "Python"))
