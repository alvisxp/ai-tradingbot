from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
import credentials

BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY": credentials.API_KEY,
    "API_SECRET": credentials.API_SECRET,
    "PAPER": True            
    }

class BuyHold(Strategy):

    def initialize(self):
        self.sleeptime = "1D"
    
    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = "GOOGL"
            price = self.get_last_price(symbol)
            quantity = 2
            order = self.create_order(symbol, quantity, "buy")
            self.submit_order(order)

if __name__ == "__main__":
    trade = False

    if trade:
        broker = Alpaca(ALPACA_CREDS)
        strategy = BuyHold(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()

    else:
        start = datetime(2023,1,1)
        end = datetime(2023,5,5)
        BuyHold.backtest(YahooDataBacktesting, start, end)