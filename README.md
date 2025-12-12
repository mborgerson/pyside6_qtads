# PySide6-QtAds
[![Latest Release](https://img.shields.io/pypi/v/Pyside6-QtAds.svg)](https://pypi.python.org/pypi/Pyside6-QtAds/)
![Monthly Downloads](https://img.shields.io/pypi/dm/PySide6-QtAds)

Python/PySide6 bindings to the [Qt Advanced Docking System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System) library.

Install with:

```bash
pip install PySide6-QtAds
```

You may also build from source. Example build from source on Ubuntu 24.04:

```bash
# Install Qt (for example, using aqtinstall)
pip install aqtinstall
aqt install-qt linux desktop 6.10.1 --outputdir qt

# Build PySide6-QtAds
LD_LIBRARY_PATH=$PWD/qt/6.10.1/gcc_64/lib \
CMAKE_PREFIX_PATH=$PWD/qt/6.10.1/gcc_64/lib/cmake/ \
pip install -v .
```

# Examples
https://github.com/mborgerson/Qt-Advanced-Docking-System/tree/pyside6

# Credits
- Original PySide6 binding work by CJ Niemira via https://github.com/cniemira/pyside6_qtads
- With bindings.xml improvements via https://github.com/metgem/PySide2Ads
