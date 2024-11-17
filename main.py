from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
import sqlite3

app = Flask(__name__)

@app.route("/login.live.com/ppsecure/clientpost.srf", methods=['POST'])
def clientpost():
     content_type = request.headers.get("Content-Type")
     if content_type == "text/xml":
        xml_data = request.data
        try:
            root = ET.fromstring(xml_data)
            sign_in_name = root.find('.//SignInName').text
            password = root.find('.//Password').text
            with sqlite3.connect('user_system.db') as conn:
              cursor = conn.cursor()
              cursor.execute('''
               SELECT * FROM users WHERE email = ? AND password = ?
             ''', (sign_in_name, password))
            result = cursor.fetchone()
            if result:
               return render_template('clientpost.srf',ip=ip, port=port)
            else:
               return '<?xml version="1.0" encoding="utf-8"?><LoginResponse Success="false"></LoginResponse>'
        except ET.ParseError as e:
            return str(e), 400

@app.route("/login.live.com/ppsecure/ClientProfileRequest.srf", methods=['POST'])
def ClientProfileRequest():
     content_type = request.headers.get("Content-Type")
     if content_type == "text/xml":
        xml_data = request.data
        try:
            root = ET.fromstring(xml_data)
            sign_in_name = root.find('.//SignInName').text
            password = root.find('.//Password').text
            with sqlite3.connect('user_system.db') as conn:
              cursor = conn.cursor()
              cursor.execute('''
               SELECT * FROM users WHERE email = ? AND password = ?
             ''', (sign_in_name, password))
            result = cursor.fetchone()
            if result:
               return render_template('ClientProfileRequest.srf',sign_in_name=sign_in_name, password=password)
            else:
               return '<?xml version="1.0" encoding="utf-8"?><ProfileResponse Success="false"></ProfileResponse>'
        except ET.ParseError as e:
            return str(e), 400
     
@app.route("/nexus.passport.com/client/client.xml")
def client():
    return render_template('client.xml',ip=ip, port=port)

@app.route("/login.live.com/logoutxml.srfl")
def logoutxml():
    return render_template('logoutxml.srf')

@app.route("/dummy")
def hello():
    return 'Hello, World!'
    
if __name__ == "__main__":
    ip = "192.168.10.104"
    port = 5000
    app.run(host="0.0.0.0")
