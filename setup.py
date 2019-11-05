import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Fil\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Fil\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

executables = [cx_Freeze.Executable(script="main.py", icon=r"sprites\img\icon.ico", base="Win32GUI", targetName="Project.exe")]
excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'json', 'tkinter', 'multiprocessing', 'pydoc_data', 'ctypes', 'lib2to3', 'test']
zip_include_packages = ['collections', 'encodings', 'importlib']
include_files = ["sprites", "modules", "game.py"]

cx_Freeze.setup(
    name='MyProject',
    options={"build_exe": {"packages": ["pygame", "random"], "include_files": include_files, 'excludes': excludes, 'zip_include_packages': zip_include_packages}},

    version="1.0",
    description="Игра для проекта",
    author='AlexDev',

    executables=executables,
)

# python setup.py bdist_msi
# python setup.py build
