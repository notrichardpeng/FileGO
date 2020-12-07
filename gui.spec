# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

import os
import sys

backend_name = os.environ.get('PYSTRAY_BACKEND', None)
if backend_name:
    modules = ['pystray._' + backend_name]
elif sys.platform == 'darwin':
    modules = ['pystray._darwin']
elif sys.platform == 'win32':
    modules = ['pystray._win32']
else:
    modules = ['pystray._appindicator', 'pystray._gtk', 'pystray._xorg']

a = Analysis(['gui.py'],
             pathex=['C:\\Users\\notri\\Desktop\\Programming\\Python\\FileMover'],
             binaries=[],
             datas=[],
             hiddenimports=modules,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('icon.ico', 'C:\\Users\\notri\\Desktop\\Programming\\Python\\FileMover\\icon.ico', 'Data')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
