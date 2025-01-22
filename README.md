# CodePython
Mis codigos hechos para python
Voy a agregar algo

PARA CORRER ESTOS CODIGOS HAY QUE AGREAGAR UN ENTORNO VIRTUAL AQUI YA ESTA CREADO


macbookair@MacBook-Air-de-Edwin-Donovan CodePython % source venv/bin/activate
# AQUI LO ACTIVAMOS 

(venv) macbookair@MacBook-Air-de-Edwin-Donovan CodePython % pip list
Package         Version
--------------- -----------
contourpy       1.3.1
cycler          0.12.1
fonttools       4.55.3
kiwisolver      1.4.8
matplotlib      3.10.0
numpy           2.2.1
opencv-python   4.10.0.84
packaging       24.2
pillow          11.1.0
pip             24.3.1
pyparsing       3.2.1
python-dateutil 2.9.0.post0
six             1.17.0
# VERIFICAMOS SI ESTA INSTALADO OPENCV SI NO INSTALAMOS
(venv) macbookair@MacBook-Air-de-Edwin-Donovan CodePython % pip install opencv-contrib-python

Collecting opencv-contrib-python
  Downloading opencv_contrib_python-4.11.0.86-cp37-abi3-macosx_13_0_arm64.whl.metadata (20 kB)
Requirement already satisfied: numpy>=1.21.2 in ./venv/lib/python3.13/site-packages (from opencv-contrib-python) (2.2.1)
Downloading opencv_contrib_python-4.11.0.86-cp37-abi3-macosx_13_0_arm64.whl (46.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.3/46.3 MB 40.1 MB/s eta 0:00:00
Installing collected packages: opencv-contrib-python
Successfully installed opencv-contrib-python-4.11.0.86

# CORREMOS PARA QUE FUNCIONE Y LISTO ASI SE CORREN
(venv) macbookair@MacBook-Air-de-Edwin-Donovan CodePython % python3 ReconocimientoFacial.py

2025-01-22 13:32:56.937 Python[64695:1902788] +[IMKClient subclass]: chose IMKClient_Modern
2025-01-22 13:32:56.937 Python[64695:1902788] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Video guardado en: faces_and_eyes.avi
(venv) macbookair@MacBook-Air-de-Edwin-Donovan CodePython %    

Agregue Cambios