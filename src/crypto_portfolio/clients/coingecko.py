import requests

# This is the public API endpoint for CoinGecko
API_BASE_URL = "https://api.coingecko.com/api/v3"

def get_top_coins(num_coins: int = 20) -> list[dict]:
    """
    Fetches the top N coins by market cap from CoinGecko.

    Args:
        num_coins: The number of coins to fetch (e.g., 20).

    Returns:
        A list of dictionaries, where each dict contains
        the coin's 'id' (e.g., 'bitcoin') and 'symbol' (e.g., 'btc').
    """
    print(f"Fetching top {num_coins} coins from CoinGecko...")
    
    endpoint = "/coins/markets"
    url = API_BASE_URL + endpoint
    
    # Parameters for the API request
    params = {
        "vs_currency": "usd",       # Get market cap in USD
        "order": "market_cap_desc", # Sort by market cap
        "per_page": num_coins,      # Number of coins to return
        "page": 1,                  # Get the first page
        "sparkline": "false",
    }
    
    try:
        response = requests.get(url, params=params)
        
        # This will raise an error if the request failed (e.g., 404, 500)
        response.raise_for_status() 
        
        data = response.json()
        
        # We only care about the id and symbol for the next step
        # This creates a clean list: [{'id': 'bitcoin', 'symbol': 'btc'}, ...]
        coin_list = [
            {"id": coin["id"], "symbol": coin["symbol"]}
            for coin in data
        ]
        
        print(f"Successfully fetched {len(coin_list)} coins.")
        return coin_list
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return []

# --- To test this file ---
# You can run this file directly from your terminal to 
# check if it's working.
if __name__ == "__main__":
    top_coins = get_top_coins(num_coins=20)
    if top_coins:
        print("\n--- Top 20 Coins ---")
        for i, coin in enumerate(top_coins):
            print(f"{i+1:2}. {coin['id']:<20} ({coin['symbol'].upper()})")