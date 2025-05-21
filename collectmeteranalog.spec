# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.win32.versioninfo import FixedFileInfo, VSVersionInfo, StringFileInfo, StringTable, StringStruct
from collectmeteranalog.__version__ import __version__

def make_fixed_file_info(version_str):
    parts = list(map(int, version_str.split(".")))
    while len(parts) < 4:
        parts.append(0)
    return FixedFileInfo(
        filevers=tuple(parts),
        prodvers=tuple(parts),
        mask=0x3F,
        flags=0x0,
        OS=0x40004,          # Windows NT
        fileType=0x1,        # Application
        subtype=0x0,
        date=(0, 0)
    )

# Reads application version from 'collectmeteranalog/__version__.py' and injects to VersionInfo struct
ffi = make_fixed_file_info(__version__)

version_file = VSVersionInfo(
    ffi=ffi,
    kids=[
        StringFileInfo([
            StringTable(
                '040904B0',
                [
                    StringStruct('CompanyName', ''),
                    StringStruct('FileDescription', 'Analog Meter Collector'),
                    StringStruct('FileVersion', __version__),
                    StringStruct('InternalName', 'collectmeteranalog'),
                    StringStruct('OriginalFilename', 'collectmeteranalog.exe'),
                    StringStruct('ProductName', 'CollectMeterAnalog'),
                    StringStruct('ProductVersion', __version__),
                ]
            )
        ])
    ]
)


block_cipher = None


a = Analysis(
    ['run.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=['requests'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='collectmeteranalog',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version=version_file,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='collectmeteranalog',
)
