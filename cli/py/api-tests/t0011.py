import clr
import System.Diagnostics as Diagnostics
# Start a process (e.g., Notepad)
process_info = Diagnostics.ProcessStartInfo("notepad.exe")
process = Diagnostics.Process.Start(process_info)
process.WaitForExit()
