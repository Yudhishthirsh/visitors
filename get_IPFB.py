import csv
from flask import Flask, request, render_template

app = Flask(__name__)
ip_addresses = []

@app.route('/')
def index():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip_address not in ip_addresses:
        ip_addresses.append(ip_address)
        with open('ip_addresses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ip_address])
    return render_template('index3.html', ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)