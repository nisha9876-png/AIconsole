# API_key = "PKTX29I21BWGYRA6HFVY"
# API_SECRET = "GUhCEmLUJFedMrj9pcUr4wOe6MoLmVafifTSdXfV"




#URL = "https://paper-api.alpaca.markets/v2" 

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('PKTX29I21BWGYRA6HFVY', 'GUhCEmLUJFedMrj9pcUr4wOe6MoLmVafifTSdXfV', paper=True)
print(trading_client)

account = trading_client.get_account()
print(account.status)

symbol = input ("Enter the name of the stock you want to buy ")
qty =float(input("Enter the quantity"))



#preparing market order
market_order_data = MarketOrderRequest(
                    symbol=symbol,
                    qty=qty,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

print(market_order.status)


