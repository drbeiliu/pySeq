from distutils.core import setup
from py2exe.build_exe import py2exe
import sys,os

sys.argv.append('py2exe')

icon = os.path.join(os.path.dirname(sys.executable),'DLLs\py.ico')
setup(
      options = {'py2exe': {
                            'optimize' : 2,
                            'dist_dir' : 'dist',
                            'includes':'sip'
                            }},
      name = 'Sequence Match',
      windows = [
                 {
                  'script': 'main.py',
                  'icon_resources':[(0x0004,icon)]
                  }
                 ],
      description = "Find Sequence Pattern",
      version = "0.1",
      author = "Bei Liu"      
      )
