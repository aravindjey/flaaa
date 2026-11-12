# flaaa

CLI tool and reference repository for 10 Flutter lab experiments.

## Installation

### From PyPI (once published)
```bash
pip install flaaa
```

### Directly from GitHub
```bash
pip install git+https://github.com/aravindjey/flaaa.git
```

### For local development
```bash
git clone https://github.com/aravindjey/flaaa.git
cd flaaa
pip install -e .
```

---

## Usage

Simply run `flaaa` in any terminal:

```bash
# List all 10 experiments
flaaa

# View code for a specific experiment (e.g. Experiment 1)
flaaa 1
# or
flaaa show 1

# Export an experiment file to current directory
flaaa save 1

# Export all 10 experiment files to current directory
flaaa save all
```

---

## Experiment Index

| # | Title | Description | File |
|---|---|---|---|
| 1 | Basic Flutter App | Welcome screen with Icon, Text, and ElevatedButton | `exp1.txt` |
| 2 | Responsive UI | LayoutBuilder adapting UI to screen dimensions | `exp2.txt` |
| 3 | User Input | TextField, TextEditingController, and SnackBar | `exp3.txt` |
| 4 | Image Asset App | Image.asset rendering and pubspec.yaml asset setup | `exp4.txt` |
| 5 | Multi-Screen Navigation | Navigator.push and MaterialPageRoute | `exp5.txt` |
| 6 | Animation | AnimatedContainer transitions | `exp6.txt` |
| 7 | State Management | Counter application with StatefulWidget and setState | `exp7.txt` |
| 8 | SQLite Database | Local database storage using sqflite and path | `exp8.txt` |
| 9 | HTTP REST API | API calls using http package and JSONPlaceholder | `exp9.txt` |
| 10 | Flutter CLI & Build | Essential terminal commands (create, run, build apk) | `exp10.txt` |

---

## Publishing to PyPI

To make `pip install flaaa` work directly worldwide:

1. Install build tools:
   ```bash
   pip install --upgrade build twine
   ```
2. Build the distribution:
   ```bash
   python -m build
   ```
3. Upload to PyPI (requires a [PyPI account](https://pypi.org/account/register/)):
   ```bash
   python -m twine upload dist/*
   ```
