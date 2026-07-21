import os
import yfinance as yf
from datetime import datetime

def fetch_market_data(ticker="BTC-USD", period="1mo", interval="1d"):
    print(f"🤖 [Data Agent] Fetching market data for {ticker}...")
    
    # Download data from Yahoo Finance
    df = yf.download(ticker, period=period, interval=interval)
    
    if df.empty:
        print("⚠️ [Data Agent] No data retrieved. Check the ticker symbol.")
        return
        
    # Define save path in the 'data' directory
    save_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(save_dir, exist_ok=True)
    
    file_path = os.path.join(save_dir, f"{ticker}_data.csv")
    df.to_csv(file_path)
    print(f"✅ [Data Agent] Data successfully saved to {file_path}")

if __name__ == "__main__":
    # Test fetch for Bitcoin
    fetch_market_data(ticker="BTC-USD", period="1mo")
