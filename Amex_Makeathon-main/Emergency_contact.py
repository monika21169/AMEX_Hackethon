from twilio.rest import Client
import requests

def get_lat_long(address):
    # Your Google Maps API key
    api_key = ''

    # Google Maps Geocoding API endpoint
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    try:
        # Send request to Google Maps API
        response = requests.get(url)
        data = response.json()

        # Parse response to get latitude and longitude
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            print("Unable to fetch location. Please check the address or API key.")
            return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage:
address = "New Delhi, India"  # Provide the address for which you want to get the latitude and longitude
latitude, longitude = get_lat_long(address)
if latitude is not None and longitude is not None:
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Failed to fetch latitude and longitude.")


# Twilio API credentials
account_sid = 'ACc3bfa1584c739d0a5670b7cf235fea56'
auth_token = '5840ab74b62dd5b191b94f26ee021778'
twilio_phone_number = ''  # Your Twilio phone number
recipient_phone_number = ''  # The recipient's phone number

## we will use if conditions to change the recipent_phone_number based on the emergency

# User's location (latitude and longitude)
latitude = 28.547017443934433
longitude = 77.27464187725289

# Generate Google Maps URL
maps_url = f'https://www.google.com/maps?q={latitude},{longitude}'
#print(maps_url)

# Custom text message
message_body = f'Hey there! Check out my location on Google Maps: {maps_url}'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS
try:
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("SMS sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
