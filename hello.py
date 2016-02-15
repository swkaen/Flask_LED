# coding:utf-8
from flask import Flask, jsonify, request, render_template
import os
import serial

port ="/dev/tty.usbmodem1421"
ser = serial.Serial(port, 9600)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('view.html')

@app.route('/a')
def aaa():
	print('a押したよ')
	os.system("say a")
#	ser.write(bytes([0+49])) #python 3
	ser.write("1") #python 2
	return render_template('view.html')

@app.route('/b')
def bbb():
	print('b押したよ')
	os.system("say b")
#	ser.write(bytes([1+49]))
	ser.write("2") #python 2
	return render_template('view.html')

@app.route('/c')
def ccc():
	print('c押したよ')
	os.system("say c")
#	ser.write(bytes([2+49]))
	ser.write("3") #python 2
	return render_template('view.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
