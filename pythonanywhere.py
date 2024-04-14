#copy this file to pythonanywhere drive *****/mysite/flask_app  and rename to flask_app
# to write value1 and value2 to sam.txt :
# ******.pythonanywhere.com/sensor1?value1=123
# ******.pythonanywhere.com/sensor2?value2=456

"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sam!'
"""
from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Function to find an available port
def find_available_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))  # Bind to localhost and let the OS assign an available port
    port = sock.getsockname()[1]  # Get the assigned port
    sock.close()
    return port

# Route to serve the HTML page
@app.route('/')
def index():
    # Read the content of sam.txt and print it to the console
    with open('sam.txt', 'r') as file:
        file_content = file.readlines()

    # Pass the values from sam.txt to the HTML template
    value1 = file_content[0].strip()
    value2 = file_content[1].strip()
    value3 = file_content[2].strip()
    button1 = int(file_content[3].strip())
    button2 = int(file_content[4].strip())
    button3 = int(file_content[5].strip())
    button4 = int(file_content[6].strip())

    return render_template('index.html', value1=value1, value2=value2, value3=value3, button1=button1, button2=button2, button3=button3, button4=button4)

# Route to handle updating the sam.txt file
@app.route('/update_sam', methods=['POST'])
def update_sam():
    content = request.form.get('content')
    with open('sam.txt', 'w') as file:
        file.write(content)
    return 'File updated successfully'



@app.route('/sensor1')#/sensor1?value1=123
def sensores():
    tempo1 = str(request.args.get('value1'))

    # Read existing content from data.txt
    with open("/home/******/sam.txt", "r") as file:
        lines = file.readlines()

    # Modify only the first line with the new tempo value
    lines[0] = tempo1 + '\n'

    # Write the modified content back to data.txt
    with open("/home/******/sam.txt", "w") as file:
        file.writelines(lines)

    return "Data 1 received"


@app.route('/sensor2')#/sensor2?value2=123
def sensores2():
    tempo2 = str(request.args.get('value2'))

    # Read existing content from data.txt
    with open("/home/******/sam.txt", "r") as file:
        lines = file.readlines()

    # Modify only the first line with the new tempo value
    lines[1] = tempo2 + '\n'

    # Write the modified content back to data.txt
    with open("/home/******/sam.txt", "w") as file:
        file.writelines(lines)

    return "Data 2 received"



if __name__ == '__main__':
    port = find_available_port()
    app.run(debug=True, port=port)
