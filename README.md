# pythonanywhere_esp32
how to store variables in micropython esp32 on pythonanywhere drive and acces them thru the esp32 and thru a web falsk app
replace ****** by your pythonanywere account name
we have 3 files to upload to pythonanywhere.com :
index.html witch contain form,buttons and labels and java script to link them
then index.html should be copied to ******/mysite/templates/ on pythonanywhere.com
the file pythonanywhere.py must be renamed to flask_app.py and copied to ******/mysite/
the difference between app,py and pythonanywhere.py is that app.py run locally
the pythonantwehre.py run on the server and search for available port
then the sam.txt witch contain variables must be copied to the root of pythonanywere.com
thats means into ******/

in pythonanywhere site:

then open console and make envirment called env3.9 and install python3.8 and flask console :
  mkvirtualenv --python=/usr/bin/python3.8 env3.9
  pip install flask

  then python flask_app.py

https://******.pythonanywhere.com  to access the sever

then goto web tab in pythonanywere and create new app inside ******/mysite

explication of sam.txt:
first line      value label 1       vars: value1
second line     value label 2        vars: value2
3rd line        value input field    vars: value3
4th line to 7line : button1 to button7 vars ( 1 pushed and 0 not pushed)
