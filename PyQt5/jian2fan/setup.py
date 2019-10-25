import sys,os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY']="D:\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY']="D:\\Anaconda3\\tcl\\tk8.6"
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pyqt5","pyautogui","pyscreeze","pymsgbox"], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = 'Win32GUI' if sys.platform=='win32' else None

setup(  name = "web_assist",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("GetFanTiZi.py", base=base)])
