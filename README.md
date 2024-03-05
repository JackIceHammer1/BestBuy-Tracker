# Best Buy Product Availability Tracker

This script periodically checks the availability of a product on Best Buy's website using their API. If the product is available, it sends an SMS notification using the Vonage API.

### Usage (Can be used without SMS capabilities, omit steps 3-5)
1. Sign up for a Best Buy API key and replace 'API_KEY' in track.py with your API key.
2. Replace 'SKU' in track.py with the SKU of the product you want to track.
3. Sign up for a Vonage account and replace 'API' in SMS.py with your API key and API secret.
4. Replace 'PHONE' in SMS.py with your Vonage phone number.
5. Replace 'PHONE' in SMS.py with the recipient's phone number.

To run the tracker, execute the following command:
python track.py

### Requirements
- Python 3
- vonage package (install via pip)
