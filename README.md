Sigue estos pasos antes de correr el programa

- En una terminal $python -m venv env
- Si estás en VSCode haz esto:
- Ctrl + Shift + P y busca por: "Python select interpreter"
- Añadirás una ruta (path) y le vas a poner ".\env\Scripts\python.exe"
- Ctrl + Ñ para abrir una terminal. Si te sale "(env) PS X:\\..." vas por buen camino
- Ahora en la misma terminal pegamos estos comandos de Python:

'''
python.exe -m pip install --upgrade pip
pip install googletrans==4.0.0rc1
pip install requests
'''

Ahora con Code Runner de VSCode ejecuta Python. Puedes crear un archivo JSON y ponerle la ruta absoluta del proyecto