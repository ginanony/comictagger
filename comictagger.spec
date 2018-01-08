# -*- mode: python -*-

block_cipher = None


a = Analysis(['comictagger.py'],
             binaries=[('./unrar/libunrar.so', './')],
             datas=[('comictaggerlib/ui/*.ui', 'ui'), ('comictaggerlib/graphics', 'graphics')],
             hiddenimports=['PIL'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='comictagger',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='comictagger')

app = BUNDLE(coll,
            name='ComicTagger.app',
            icon='mac/app.icns',
            info_plist={
                'NSHighResolutionCapable': 'True'
            },
            bundle_identifier=None)