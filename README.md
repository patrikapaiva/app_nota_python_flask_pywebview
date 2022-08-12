# app_nota_python_flask_pywebview
Programa de Notas com Python Flask Pywebview que cria banco de dados e automatico 

Versão do Python usada: v3.6.8
OS: windows 10

Requisito windows 10 : MicrosoftEdgeWebView2RuntimeInstallerX64.exe
https://developer.microsoft.com/pt-br/microsoft-edge/webview2/#download-section 

Instalação passo a passo 

1 - Abra o cmd na pasta do projeto 

2 - pip install virtualenv

3 - python -m venv venv

4 - .\venv\Scripts\activate

5 - pip install to-requirements.txt

6 - python app.py

comando para gerar exe

pyinstaller --noconfirm --onefile --windowed --add-data "templates;templates" --add-data "static;static"  "app.py"
