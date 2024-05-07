import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
import System.Windows.Forms as WinForms
import System.Drawing as Drawing
# Create a simple form
form = WinForms.Form()
form.Text = "Hello, WinForms from Python!"
# Set the size of the form
form.Size = Drawing.Size(300, 200)
# Add a button
button = WinForms.Button()
button.Text = "Click Me!"
button.Location = Drawing.Point(50, 50)
# Define button click event handler
def button_click(sender, e):
    WinForms.MessageBox.Show("Button clicked!")
button.Click += button_click
# Add button to the form
form.Controls.Add(button)
# Show the form
WinForms.Application.Run(form)
