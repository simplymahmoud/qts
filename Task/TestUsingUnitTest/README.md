# Framework architecture and design:
* Using layered architecture with configurable OOP (Python) framework which include the required test methods and utilities to run the backend tests with documented steps and simple time stamped logging mechanism.


# Files and Folders:
--------------------
* config.cfg: The test-suite configuration file.
* requirements: The test-suite python packages requirements file.
* testsuite: The test-suite folder holding test cases files and test-framework.
* testsuite/test_get.py: The test case file for the task.
* testframework: The test-framework folder for base test case class and utilities.
* testframework/base.py: The test framework base file for test case classes and utilities.
* logs: The test-suite logging folder will be created during operations containing the log file.


# Requirements:
* If you don't have python 2.7 use this link: https://www.python.org/download/releases/2.7/


Install Python Packages:
------------------------
Windows
```
C:\Users\a.ali\Repos\TestUsingUnitTest>c:\Python27\Scripts\pip.exe install requirements
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
C:\Users\a.ali\Repos\TestUsingUnitTest>c:\Python27\Scripts\nosetests.exe -v testsuite --tc-file config.ini
```

Linux
```
python$> cd TestUsingUnitTest
python$> nosetests -v testsuite --tc-file=config.ini --with-xunitmp
```

See test logs open file logs/api_testsuite.log
