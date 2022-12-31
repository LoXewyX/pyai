_Follow these steps before running the program_

- In a terminal [ Windows or Linux ]
``` powershell
python -m venv ${env}
```
- If you are in VSCode do this:
- Ctrl + Shift + P and search for: "Python select interpreter"
- You will add a route (path) `.\${env}\Scripts\python.exe`
- Ctrl + Ñ to open a terminal. If you get `(env) PS X:\\...` you are on the right track
- Now in the same terminal we paste these Python commands:

Another way is activating it by yourself:

- Windows:
``` powershell
./env/bin/Activate.ps1
```
- Linux:
``` bash
source ./env/bin/activate
```

``` powershell
python.exe -m pip install --update pip
pip install googletrans==4.0.0rc1
pip installation requests
```

Once you had enabled the Virtual Enviroment can run your code by typing 'python3 setup.py'
Or use on VSCode, Code Runner
