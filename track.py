import requests
import datetime
import time
import SMS

def check_availability(api_key, product_sku):
    url = f"https://api.bestbuy.com/v1/products/{product_sku}.json"
    params = {
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def main():
    api_key = 'API_KEY' # Replace with your API key
    product_sku = 'SKU' # Replace with your product SKU

    while True:
        try:
            product_info = check_availability(api_key, product_sku)
            online_availability = product_info.get('onlineAvailability')
            if online_availability:
                print("Available at " + str(datetime.datetime.now()))
                SMS.send("Best Buy: Product " + product_sku + " available at " + str(datetime.datetime.now()))
        except Exception as e:
            print("An error occurred with the request:", e)
        time.sleep(30) # Waits for 30 seconds before checking again

if __name__ == "__main__":
    main()
