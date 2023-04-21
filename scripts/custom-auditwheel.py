#!/usr/bin/env python3
import sys

from auditwheel.main import main
from auditwheel.policy import _POLICIES as POLICIES


for p in POLICIES:
    p['lib_whitelist'].extend([
        'libpyside6.abi3.so.6.5',
        'libpyside6.abi3.so.6.4',
        'libpyside6.abi3.so.6.3',
        'libshiboken6.abi3.so.6.5',
        'libshiboken6.abi3.so.6.4',
        'libshiboken6.abi3.so.6.3',
        'libQt6Widgets.so.6',
        'libQt6Gui.so.6',
        'libpyside6qml.abi3.so.6.5',
        'libpyside6qml.abi3.so.6.4',
        'libpyside6qml.abi3.so.6.3',
        'libGLX.so.0',
        'libOpenGL.so.0',
        'libQt6Core.so.6',
        'libxcb.so.1',
    ])


if __name__ == "__main__":
    sys.exit(main())
