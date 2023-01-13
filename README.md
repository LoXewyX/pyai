_Follow these steps before running the program_

> :warning: If the command **python3** does not work for you try only **python**

- In a Windows or Linux terminal, where "myenv" can be written as desired.

``` powershell
python3 -m venv myenv
```

> **If you are in VSCode** try this:
- Ctrl + Shift + P and search for: "Python select interpreter"
- Now add this route ` .\myenv\Scripts\python.exe `
- ``` Ctrl + Shift + ` ``` to open a terminal
- Now in the same terminal we paste these Python commands:

> __Note__ If you get ` (env) PS X:\\... `, you are on the right track!
> **Otherwise** you can do it manually:
- **Windows**
``` powershell
.\env\bin\Activate.ps1
```
- **Linux**
``` bash
source ./env/bin/activate
```
``` powershell
python3 -m pip install --update pip
pip install requirements.txt
```
> :warning: In case the **requirements.txt** file is not working `pip install googletrans==4.0.0rc1 requests`

Once you had enabled the Virtual Enviroment can run your code by typing
```
python3 setup.py
```
Or use the plugin of VSCode ` Code Runner `
