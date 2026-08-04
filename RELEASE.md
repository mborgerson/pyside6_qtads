# Release Process

Releases of [PySide6-QtAds](https://pypi.org/project/PySide6-QtAds/) are
automated: pushing a `v*` tag to
[mborgerson/pyside6_qtads](https://github.com/mborgerson/pyside6_qtads)
builds the sdist and all wheels and publishes them to PyPI. The manual work
is getting the versions right first.


## Version numbering

Package version `A.B.C.D[.dev0]`:

- `A.B.C` — version of the bundled
  [Qt ADS](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System)
  library.
- `D` — binding/packaging patch, reset to 0 for each new Qt ADS version.
- `.dev0` — appended on `main` between releases.

Example: `5.0.0` → `5.0.0.1.dev0` → `5.0.0.1` → `5.0.0.2.dev0` → ...


## Where versions live

| File | Contains | Changes |
| --- | --- | --- |
| `pyproject.toml` | Package version | Every release (release + `.dev0` commits) |
| `setup.py` `-DADS_VERSION` | Qt ADS version for CMake | Only on new Qt ADS release |
| `Qt-Advanced-Docking-System` submodule | Pinned Qt ADS commit | When picking up upstream changes |
| `.pyside-version` | PySide6 version wheels build and pin against | Auto-bumped via PR by `bump-pyside.yml` |

`ADS_VERSION` must match the pinned submodule's Qt ADS version, which must
match `A.B.C`. Do not edit `Qt-Advanced-Docking-System/pyproject.toml` — it
belongs to upstream. Wheels pin `PySide6-Essentials`/`shiboken6` to
`.pyside-version`, so merging a PySide bump PR usually warrants a patch
release.


## Releasing

### 1. If updating Qt ADS (new `A.B.C`) — otherwise skip

- Pin the submodule to the upstream release matching the new `A.B.C`:

  ```sh
  cd Qt-Advanced-Docking-System
  git fetch origin
  git checkout vA.B.C
  cd ..
  git add Qt-Advanced-Docking-System
  ```

- Update `-DADS_VERSION=A.B.C` in `setup.py` to match.
- Update `src/bindings.xml` / `src/bindings.h` / `CMakeLists.txt` for API
  changes (new classes need all three; new enums/methods usually only
  `bindings.xml`, often nothing — shiboken auto-exposes most additions).
- Build a wheel locally and smoke-test the new API.

See `ebd48ca` "Update bindings to Qt ADS 5.0.0" for a model commit.

### 2. Verify main is green

Every push already builds and tests all wheels, so a green
[CI run](https://github.com/mborgerson/pyside6_qtads/actions) on `main`
means the release build will almost certainly succeed.

### 3. Release commit

On `main`, drop `.dev0` in `pyproject.toml` (also advance the submodule here
if picking up upstream fixes within the same Qt ADS version):

```sh
git add pyproject.toml
git commit -m "v5.0.0.2"
```

### 4. Tag and push — the actual release

```sh
git tag -a v5.0.0.2 -m "v5.0.0.2"
git push origin main v5.0.0.2
```

CI builds the sdist and cp310 abi3 wheels for Windows (x86_64, arm64),
manylinux (x86_64, aarch64), and macOS (x86_64, arm64), tests each, then
publishes to PyPI (`upload_pypi` job, `PYPI_TOKEN` secret). Watch the run
and confirm the version on
[PyPI](https://pypi.org/project/PySide6-QtAds/).

### 5. Post-release commit

Bump `main` to the next dev version:

```sh
# pyproject.toml: version = "5.0.0.3.dev0"
git add pyproject.toml
git commit -m "v5.0.0.3.dev0"
git push origin main
```

### 6. Verify

```sh
pip install --upgrade PySide6-QtAds==5.0.0.2
python -c "import PySide6QtAds; print(PySide6QtAds.__version__)"
```


## If the release build fails

PyPI upload runs only after every wheel builds and tests, so a failure
publishes nothing. Fix `main` and re-release as `D+1`. Never reuse or
force-move a pushed tag.
