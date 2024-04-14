#for py3board 5 leds , 5 push buttons , 1 potentiometer and 3 slots:lcd,i2c,spi
# *****.pythonanywhere.com acount with sam.txt file to store variables to control
# py3board , with flask_app for mobile interface user https://******.pythonanywhere.com

import network
import urequests
import socket
import machine
from machine import Pin, ADC
from time import sleep
#import for callmebot whatsapp
import esp
esp.osdebug(None)
import gc
gc.collect()


#onboard blue led to indicate wifi connection
blueled = Pin(2, Pin.OUT)
blueled.off()
#setting outputs and inputs gpio pin
led1= Pin(32, Pin.OUT)
led2= Pin(33, Pin.OUT)
led3= Pin(25, Pin.OUT)
led4= Pin(26, Pin.OUT)
sw1 = Pin(34, Pin.IN)

#Your phone number in international format for callmebot whatsapp
phone_number = '+9613******'
#Your callmebot API key
api_key = '*******'

# PythonAnywhere account details
username = "******"
api_token = "cb76ea0a0f27937aeb********************"

# URL for PythonAnywhere API
api_url = "https://www.pythonanywhere.com/api/v0/user/{username}/files/path/home/{username}/sam.txt".format(
    username=username)




def connect_to_internet():
    # enter wi-fi creds
    WIFI_NETWORK='Rassi_Net'
    WIFI_PASSWORD='********************'

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_NETWORK, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    # will print network configuration when connected and turn onboard led on
    blueled.on()
    print('network config:', sta_if.ifconfig())





# Function to fetch the content of sam.txt using PythonAnywhere API
def fetch_sam_txt():
    try:
        # Send GET request to fetch the content of the file
        response = urequests.get(api_url, headers={'Authorization': 'Token {token}'.format(token=api_token)})
        
        if response.status_code == 200:
            return response.text.splitlines()  # Return a list of lines from the file
        else:
            print("Failed to fetch file. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None


# function to write to first and second line to sam.txt (value1 and value2)
def http_get(url):    
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
    


# fonction to send whatsapp message callmebot
def send_message(phone_number, api_key, message):
  #set your host URL
  url2 = 'https://api.callmebot.com/whatsapp.php?phone='+phone_number+'&text='+message+'&apikey='+api_key

  #make the request
  response = urequests.get(url2)
  #check if it was successful
  if response.status_code == 200:
    print('connected')
  else:
    print('Error')
    print(response.text)




# Main function





#ADC on Pin 33 Variable = pot
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB) #full range:3.3v


#initiate value1 and value2
value1=0
value2=0

    
# connect to internet:
connect_to_internet()

while True:
    
    try:
    
        oldvalue1=value1
        oldvalue2=value2
        
        # Fetch content of sam.txt from PythonAnywhere using API and turn on and off
        # leds depending on content of sam.txt file (line3 to line6)
        lines = fetch_sam_txt()
        print (lines)
        
        print("number of line in sam.txt = ",len(lines))
        if (len(lines)) != 7 : #to avoid error, if nmbr of lines in sam.txt != 7 reboot
            print ("connection problems... Rebooting ... please wait ...")
            blueled.off()
            sleep(5)
            machine.reset()
            
        print("line(3)=",lines[3])
        print("line(4)=",lines[4])
        print("line(5)=",lines[5])
        print("line(6)=",lines[6])
        
        if lines[3] == "1":
            led1.on()  # Turn the LED1 on
        elif lines[3] == "0":
            led1.off()  # Turn the LED1 off

        if lines[4] == "1":
            led2.on()  # Turn the LED2 on
        elif lines[4] == "0":
            led2.off()  # Turn the LED2 off
        
        if lines[5] == "1":
            led3.on()  # Turn the LED3 on
        elif lines[5] == "0":
            led3.off()  # Turn the LED3 off
        
        if lines[6] == "1":
            led4.on()  # Turn the LED4 on
        elif lines[6] == "0":
            led4.off()  # Turn the LED4 off

        # give to value2 0 or 1 depending on the status of onboard push button5 
        value2=sw1.value()
        # give to value1 the value of onboard potentiometer
        value1 = int((pot.read()/4095)*100)
        
        print("value1=", value1)
        print("value2=", value2)
        
        # Send message to WhatsApp "onboard button pushed" if onboard button is pushed
        if sw1.value()==1 :
            message = 'onboard%20button%20pushed' #YOUR MESSAGE HERE (URL ENCODED)https://www.urlencoder.io/ 
            send_message(phone_number, api_key, message)
            print("message sent")
            blueled.off()
            sleep(0.5)
            blueled.on()
            sleep(0.5)
            blueled.off()
            sleep(0.5)
            blueled.on()
            sleep(0.5)
            blueled.off()
            # Reset the ESP32
            machine.reset()

        # write value1 and value2 in sam.txt if there is changes
        
        
        if (abs(oldvalue1 - value1 )) > 5 : #if the change is more than 5 unit then update sam.txt
            url="https//******.pythonanywhere.com/sensor1?value1="+str(value1)
            print ("updating value1",value1)
            http_get(url)

        if oldvalue2 != value2 :
            url="https//******.pythonanywhere.com/sensor2?value2="+str(value2)
            print ("updating value2",value2)
            http_get(url)


        sleep(1.5)

    except Exception as e:
        print("anknown error occurred. Rebooting ESP32.....................")
        blueled.off()
        sleep(0.5)
        blueled.on()
        sleep(0.5)
        blueled.off()
        sleep(0.5)
        blueled.on()
        sleep(0.5)
        blueled.off()
        machine.reset()
        
