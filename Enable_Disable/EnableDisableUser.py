import subprocess
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    subprocess.call('net user Guest /active:no', shell=True)
else:
	print ("You have no admin privileges. Goodbye!")
	# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)