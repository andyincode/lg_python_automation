import subprocess

result = subprocess.call('pyinstaller --onefile --icon temp.ico --clean lec_pyqt5.py')