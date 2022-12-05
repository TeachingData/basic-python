import ProcessMonitor

# just a quick test of each function in the class (outside of the GUI for testing)

pm = ProcessMonitor.ProcessMonitor("test.log")
print(f"Getting total processes of {pm.totalprocesses()}")
print(f"Getting total files of %n: {pm.totalfiles()}")
print("And for processes having p in their ps line:\n")
print(*pm.findprocess("p"), sep="\n")
print()

print(pm.findbigfiles())
print()
