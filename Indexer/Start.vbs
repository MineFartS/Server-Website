
' Create a new Shell Object
Set Shell = WScript.CreateObject("WScript.Shell")

Shell.CurrentDirectory = "E:\Website\Indexer\"

Shell.run "python __Start.py", 0, 1