# -*- mode: python -*-

import os
import sys
from pathlib import Path

from blobbackup._version import __version__ as APP_VERSION

SRC_DIR = os.path.join(os.getcwd(), 'src', 'blobbackup')

a = Analysis([os.path.join(SRC_DIR, '__main__.py')],
             pathex=[SRC_DIR],
             binaries=[],
             datas=[
                (os.path.join(SRC_DIR, 'img/*'), 'img'),
                (os.path.join(SRC_DIR, 'bin/*'), 'bin'),
                (os.path.join(SRC_DIR, 'misc/*'), 'misc'),
             ],
             hiddenimports=[
                 'blobbackup.keyring.darwin',
                 'pkg_resources.py2_warn',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=f"blobbackup-{sys.platform}",
          icon='logo.ico',
          bootloader_ignore_signals=True,
          console=False,
          debug=False,
          strip=False,
          uac_admin=True,
          upx=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               debug=False,
               strip=False,
               upx=False,
               name='blobbackup')

app = BUNDLE(coll,
             name='Blobbackup.app',
             icon='icon.icns',
             bundle_identifier=None,
             info_plist={
                 'CFBundleName': 'Blobbackup',
                 'CFBundleDisplayName': 'Blobbackup',
                 'CFBundleIdentifier': 'com.blobbackup.client.macos',
                 'NSHighResolutionCapable': 'True',
                 'LSAppNapIsDisabled': 'True',
                 'NSRequiresAquaSystemAppearance': 'False',
                 'LSUIElement': '1',
                 'LSMinimumSystemVersion': '10.15',
                 'CFBundleShortVersionString': APP_VERSION,
                 'CFBundleVersion': APP_VERSION,
                 'NSSystemAdministrationUsageDescription': 'Blobbackup requires full disk access to work.',
                 'LSEnvironment': {
                             'LC_CTYPE': 'en_US.UTF-8',
                             'PATH': '/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin'
                         }
             })