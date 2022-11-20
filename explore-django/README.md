# Django Setup

Python
Install Python.

Check the version by typing this in the command prompt:
```
py --version
```

PIP
Check if pip is installed:

```
pip help
```
If it runs, pip is installed, else, it will bring up an error.

To install pip:
```
pip install pip
```

To check the current version of pip:
```
pip --version
```

To upgrade PIP:
```
pip install -U  --upgrade pip
```

To downgrade pip:
```
python -m pip install pip==versionnumber
```

Virtual Environment
Setting up a virtual environment:
```
py -m venv project-name
```

Creating a virtual environment:
```
virtualenv name
```

Each time you start a new command prompt, you’ll need to activate the environment again.
To activate the virtual environment:
```
project-name\Scripts\activate.bat
```

Django
In the command prompt, ensure your virtual environment is active, and execute the following command to install django:
```
py -m pip install Django
```

To verify your Django installation execute the following in the command prompt:
```
django-admin --version
```

To install mysqlclient:
```
pip install mysqlclient
```

After setting up and activating the virtual environment, run the following command:
```
$ python -m pip install -e django/
```



