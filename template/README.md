This folder consists template files for the projects.

---

### TableOfContent
- PyQt5
	- `cpp`
	- `python`
- Web Dev
	- vanilla (`html`, `css` & `js`)

- Usage

#### PyQt5

##### Python

To run the `python` version of the `PyQt5`, makesure PyQt5 is installed. Makesure to create a virtual environment for the project.


```
python3 -m venv venv
source venv/bin/activate
pip install PyQt5
```

To run the template, you can do

```
python3 main.py
```

<details>
	<summary>code explaination</summary>

```python
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
```

Basic imports we need this use the modules.

```python
class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.show()
```

creating a `class` and the class is inherits `qtw.QMainWindow`.

</details>

##### Cpp

To run the `cpp` version of `PyQt5`, makesure Qt5 is installed.

```
sudo pacman -S qt5-base
```

[more information](https://wiki.archlinux.org/title/qt#Installation)



#### Usage

If you are using linux:

Run:
```
copy.sh <projecttype> <projectlocation>
```

The above script will copy template file of the particular type into the specified project location.

IF you are using windows:

```
python3 copy.py <projectype> <projectlocation>
python3 copy.py --help
```
