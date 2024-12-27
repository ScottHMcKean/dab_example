from src.scraper import fetch_stock_data
from src.transform import prepare_stock_data
from datetime import datetime, timedelta

# Fetch data for Apple stock
apple_data = fetch_stock_data("AAPL")

# Transform the data
processed_data = prepare_stock_data(apple_data)

# Preview the data
print(processed_data.head())

# Save as Delta table
processed_data.write.format("delta").mode("overwrite").saveAsTable("stock_prices")
