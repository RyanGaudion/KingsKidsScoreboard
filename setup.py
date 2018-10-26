import os
import PIL
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\rgaud\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\rgaud\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ['PIL'],
    excludes = [],
    include_files=[r'C:\Users\rgaud\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll', r'C:\Users\rgaud\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll', 'Kings-Kids.png']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('ScoreBoard2.py', base=base)
]

setup(name='editor',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
