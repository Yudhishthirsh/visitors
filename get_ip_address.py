from flask import Flask, request
import geoip2.database

app = Flask(__name__)

# Set up GeoIP2 reader
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

# Function to get company name from IP address
def get_company(ip_address):
    try:
        response = reader.city(ip_address)
        return response.traits.company
    except geoip2.errors.AddressNotFoundError:
        return None

# Route to handle website visits
@app.route('/')
def index():
    ip_address = request.remote_addr
    company_name = get_company(ip_address)
    return f'Hello, visitor from {company_name}!'

if __name__ == '__main__':
    app.run()