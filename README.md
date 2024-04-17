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

then create on pythonanywhere/***** a new directory called mysite where we put the
flask_app.py file and inside mysite create also a new directory called templates where
we put the index.html file

upload index.html file to template dir and pythonanywhere.py to mysite directory


https://*****.pythonanywhere.com  to access the sever

then goto web tab in pythonanywere and create new app inside *****/mysite
chose python3.8 and flask app
then rename pythonanywhere.py to flask_app.py

https://******.pythonanywhere.com  to access the sever

then goto web tab in pythonanywere and create new app inside ******/mysite

the main.py is a micropython script to run on esp32 . the esp32 is connected to 4 leds 
to reflect the status of values in sam.txt and conected to a push button and potentiometer
to put there values in the sam.txt

explication of sam.txt:
first line      value label 1       vars: value1
second line     value label 2        vars: value2
3rd line        value input field    vars: value3
4th line to 7line : button1 to button7 vars ( 1 pushed and 0 not pushed)
