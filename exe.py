from cx_Freeze import setup, Executable
includefiles = ['icon.ico']
includes = ['numpy.core.fromnumeric._methods', 'numpy.lib.format']
packages = ['dateutil', 'matplotlib', 'datetime', 'numpy', 'wx', 'wx.xrc' 'functools',
    'detectorApp', 'detectorForm', 'detectorData' ]
setup(
    name = 'DetectorInfo',
    version = '1.0',
    description = "Lab1 script",
    options = {'build.exe': {'packages':packages, 'include_files':includefiles, 'includes':includes}},
    executables = [Executable('main.py', base = "Win32GUI", icon="icon.ico")]
    )