# Antiafk
Antiafk is a CLI built in Python. The intention was to create a package that allows users the option to trigger keyboard events on specified intervals, for a specified duration of time via the Python REPL.

# Installation

## Windows
To install antiafk on Windows, you will need to install Python via the Windows installer provided by the [Python Organization](https://python.org) under downloads, and then Windows. 

Once installed, run whatever version PowerShell you have installed as __root__, and execute the following commands:
- python -V && pip -V

If python -V returns the version of Python you just installed (3.6 or higher), your Python installation has been successful. In the event that the version does not match what you installed, try python3 -V to make sure an a new alias has not been created for that specific version. If pip -V returns the executable path of pip, then we can move forward with the next step. 

After you've run both of those commands and see that you have pip installed as well as a Python 3 interpreter, in your PowerShell session run:
- pip install antiafk

Test your installation by running: 
- antiafk or antiafk --help

At this point, if you have not gotten a command not found, then antiafk has been installed successfully. 

## MacOS
To install antiafk on MacOS, make sure you at least have Python 3.6 on your OS as this uses the new f-string formatting started in Python 3.6 and up. To install Python 3.6 along side any current installations, either download the latest release provided by the [Python Organization](https://python.org) under downloads (which will make an alt install), or use brew to install a specific version. With MacOS, you will NOT need to run this as __root__, unless you're running from a path with limited access.

Once installed, make sure your version of python was successfully installed by running:
- python -V
- python3 -V
- python3.6 -V
  
If one of those installatons returns Python 3.6 or higher, locate the pip executable that should have been installed along with it. You can check by running the command:
- pip -V
- pip3 -V
- pip3.6 -V

If you can't location your pip executable that was installed along side your Python installation, go to: 
- /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pip (or whatever version 3.6 or higher you have installed)

You can either execute pipe by declaring the path directly, or by exporting a variable to your path, such as:
- export pip36=/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pip
- $pip36 install package

Once you have successfully installed Python 3.6 or higher, and have pip wokring as well, proceed with installing antiafk which whatever pip alias you need to use. For me, it would be:
- pip3 install antiafk

Once installed, test your installation by running:
- antiafk or antiafk --help

If no command cannot be found has been returned, then antiafk has successfully installed. 

# Usage
Once installed, to run antiafk with the default key press interval and stop execution time, run the following command:
- antiafk \<key>
- Example:
    - antiafk space

To view what keys are supported, run:
- antiafk --help

To run antiafk with your own interval and stop executon time, run the folling:
- antiafk \<key> -i \<interval> -s \<how long before program exit>
- Example:
  - antiafk space -i 5 Minutes -s 1 Hour
  - __Note: there are no need for single or double quotation marks__