# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui.py'],
             pathex=['C:\\Users\\notri\\Desktop\\Programming\\Python\\FileMover'],
             binaries=[],
             datas=[],
             hiddenimports=['plyer.platforms.win.notification'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('icon.ico', 'C:\\Users\\notri\\Desktop\\Programming\\Python\\FileMover\\icon.ico', 'Data')]

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
          console=True , icon='icon.ico')
