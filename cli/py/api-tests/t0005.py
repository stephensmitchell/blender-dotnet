import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
# Now you can use the classes from WinForms
form = WinForms.Form()
form.Text = "Hello, WinForms!"
form.ShowDialog()
