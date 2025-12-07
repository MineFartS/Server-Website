
' Create a new Shell Object
Set Shell = WScript.CreateObject("WScript.Shell")

Shell.CurrentDirectory = "E:\Website\API\"

Shell.run "python __Start.py", 0, 1