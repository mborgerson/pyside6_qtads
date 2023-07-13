# PySide6-QtAds
[![Latest Release](https://img.shields.io/pypi/v/Pyside6-QtAds.svg)](https://pypi.python.org/pypi/Pyside6-QtAds/)
[![License](https://img.shields.io/pypi/l/PySide6-QtAds)](https://github.com/mborgerson/pyside6_qtads/blob/main/LICENSE)
![Monthly Downloads](https://img.shields.io/pypi/dm/PySide6-QtAds)

Python/PySide6 bindings to the [Qt Advanced Docking System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System) library.

Pre-built wheels are available for Windows, macOS, and Linux. You can install with:

```
pip install PySide6-QtAds
```

You may also build from source. Example build from source on Ubuntu 22.04:

```bash
# Install Qt (for example, using aqtinstall)
pip install aqtinstall
aqt install-qt linux desktop 6.5.1 --outputdir qt

# Build PySide6-QtAds
LD_LIBRARY_PATH=$PWD/qt/6.5.1/gcc_64/lib \
CMAKE_PREFIX_PATH=$PWD/qt/6.5.1/gcc_64/lib/cmake/ \
PIP_EXTRA_INDEX_URL=https://download.qt.io/official_releases/QtForPython/ \
pip install -v .
```

Note: `shiboken6-generator` is required when building from source, and currently only available via Qt's package index.

# Examples
https://github.com/mborgerson/Qt-Advanced-Docking-System/tree/pyside6

# Credits
- Original PySide6 binding work by CJ Niemira via https://github.com/cniemira/pyside6_qtads
- With bindings.xml improvements via https://github.com/metgem/PySide2Ads
