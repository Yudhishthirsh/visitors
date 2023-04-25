from flask import Flask, render_template, request
#import geoip2.database
import os
# Get the absolute path of the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Join the path of the database file with the current directory
#database_path = os.path.join(current_dir, 'GeoLite2-City.mmdb')


#app = Flask(__name__)
#geoip_reader = geoip2.database.Reader(database_path)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's name and email from the form data
    name = request.form['name']
    email = request.form['email']

    # Get the user's IP address
    ip_address = request.remote_addr

    # Use GeoIP to get the user's location information
    try:
        geoip_result = geoip_reader.city(ip_address)
        city = geoip_result.city.name
        country = geoip_result.country.name
    except:
        city = "Unknown"
        country = "Unknown"

    # Log the user's name, email, IP address, and location to a file
    with open('form_submissions.txt', 'a') as f:
        f.write(f'{name} {email} {ip_address} {city} {country}\n')

    # Return a simple message to the user
    return 'Thanks for submitting your details!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)