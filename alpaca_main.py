from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
from dotenv import load_dotenv
import os
import config

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

if not ALPACA_API_KEY or not ALPACA_SECRET_KEY:
    raise ValueError("API keys are not set. Please set the environment variables.")

client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
account = dict(client.get_account())
for k,v in account.items():
    print(f"{k:30}{v}")

order_details = MarketOrderRequest(
    symbol= "SPY",
    qty = .30,#Dont work if more than 1
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY
    #extended_hours=True
) 

order = client.submit_order(order_details)
print(f"Order submitted: {order}")

assets = [asset for asset in client.get_all_positions()]
positions = [(asset.symbol, asset.qty, asset.current_price) for asset in assets]
print("Positions")
print(f"{'Symbol':9}{'Qty':>4}{'Value':>15}")
print("-" * 28)
for position in positions:
    print(f"{position[0]:9}{position[1]:>4}{float(position[1]) * float(position[2]):>15.2f}")

client.close_all_positions(cancel_orders=True)
