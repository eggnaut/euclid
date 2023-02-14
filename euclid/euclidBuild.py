import PyInstaller.__main__

PyInstaller.__main__.run([
    '../euclid/gui.py',
    '--onefile',
    '--noconsole',
    '--disable-windowed-traceback',
    '--clean',
    '-ilogo.png',
    '-neuclid-build-macOS',
])