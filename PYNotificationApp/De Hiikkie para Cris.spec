# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['De Hiikkie para Cris.py'],
    pathex=['.venv/Lib/site-packages/plyer', '.venv/Lib/site-packages'],
    binaries=[],
    datas=[('.venv/Lib/site-packages/plyer', './plyer'),
           ('assets/img', './assets/img')],
    hiddenimports=['plyer.platforms.win.notification'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='De Hiikkie para Cris',
    icon='assets/img/dragon5.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='De Hiikkie para Cris',
)
