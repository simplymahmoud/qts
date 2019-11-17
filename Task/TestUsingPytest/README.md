# Framework architecture and design:
Single script.

# Files and Folders:
--------------------
* config.cfg: The test-suite configuration file.
* requirements: The test-suite python packages requirements file.
* testsuite: The test-suite folder holding test cases files.
* testsuite/test_get.py: The test case file for the task.


# Requirements:
* If you don't have python 2.7 use this link: https://www.python.org/download/releases/2.7/


Install Python Packages:
------------------------
Windows
```
C:\Users\a.ali\Repos\TestUsingPytest>c:\Python27\Scripts\pip.exe install requirements
```

Linux
```
python$> sudo apt-get install python-pip
python$> pip install -r requirements
python$> sudo pip install --index-url=https://pypi.python.org/simple/ requirements
```
or use local packages
```
pip install -r wheelhouse/requirements --no-index --find-links wheelhouse

```
Run the tests:
--------------
Windows
```
C:\Users\a.ali\Repos\TestUsingPytest>c:\Python27\Scripts\nosetests.exe -v testsuite --tc-file config.ini
```

Linux
```
python$> cd TestUsingPytest
python$> nosetests -v testsuite --tc-file=config.ini --with-xunitmp
```
