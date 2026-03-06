
' Create a new Shell Object
Set Shell = WScript.CreateObject("WScript.Shell")

Shell.CurrentDirectory = "E:\Website"

' Run the command
Shell.run "python -m API.__Start.py", 0, 0