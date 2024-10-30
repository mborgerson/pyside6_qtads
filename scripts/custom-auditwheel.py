#!/usr/bin/env python3
import pathlib
import tempfile
import json
from auditwheel.main import main
from auditwheel.policy import _POLICY_JSON_MAP as POLICY_JSON_MAP


if __name__ == "__main__":
    tmpdir = tempfile.TemporaryDirectory()
    tmppath = pathlib.Path(tmpdir.name)
    for libc in POLICY_JSON_MAP:
        policies = json.loads(POLICY_JSON_MAP[libc].read_text())
        for p in policies:
            p['lib_whitelist'].extend([
                'libpyside6.abi3.so.6.8',
                'libpyside6.abi3.so.6.7',
                'libpyside6.abi3.so.6.6',
                'libpyside6.abi3.so.6.5',
                'libpyside6.abi3.so.6.4',
                'libpyside6.abi3.so.6.3',
                'libshiboken6.abi3.so.6.8',
                'libshiboken6.abi3.so.6.7',
                'libshiboken6.abi3.so.6.6',
                'libshiboken6.abi3.so.6.5',
                'libshiboken6.abi3.so.6.4',
                'libshiboken6.abi3.so.6.3',
                'libQt6Widgets.so.6',
                'libQt6Gui.so.6',
                'libpyside6qml.abi3.so.6.8',
                'libpyside6qml.abi3.so.6.7',
                'libpyside6qml.abi3.so.6.6',
                'libpyside6qml.abi3.so.6.5',
                'libpyside6qml.abi3.so.6.4',
                'libpyside6qml.abi3.so.6.3',
                'libGLX.so.0',
                'libOpenGL.so.0',
                'libQt6Core.so.6',
                'libxcb.so.1',
            ])
        fname = tmppath / (libc.name + "-policy.json")
        with open(fname, "w") as f:
            json.dump(policies, f)
        POLICY_JSON_MAP[libc] = fname
    
    main()
    tmpdir.cleanup()
