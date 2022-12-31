_Follow these steps before running the program_

- In a terminal [ Windows or Linux ]
``` powershell
python -m venv ${env}
```
- If you are in VSCode do this:
- Ctrl + Shift + P and search for: "Python select interpreter"
- Now add this route ` .\${env}\Scripts\python.exe `
- ``` Ctrl + Shift + ` ``` to open a terminal
- Now in the same terminal we paste these Python commands:

> __Note__
If you get ` (env) PS X:\\... ` you are on the right track

Another way is activating it by yourself:

- Windows:
``` powershell
.\env\bin\Activate.ps1
```
- Linux:
``` bash
source ./env/bin/activate
```

``` powershell
python3 -m pip install --update pip
pip install googletrans==4.0.0rc1
pip installation requests
```

Once you had enabled the Virtual Enviroment can run your code by typing
```
python3 setup.py
```
Or use the plugin of VSCode ` Code Runner `
