import numpy as np


class TradingBot:
    def __init__(self, name, active=False, strategy=None):
        self.name = name
        self.active = active
        self.strategy = strategy
        self.prices = []  # List to store historical prices

    def activate(self):
        self.active = True
        print(f"{self.name} has been activated.")

    def deactivate(self):
        self.active = False
        print(f"{self.name} has been deactivated.")

    def record_price(self, price):
        self.prices.append(price)

    def calculate_moving_average(self, window_size):
        if len(self.prices) < window_size:
            return None
        else:
            return np.mean(self.prices[-window_size:])

    def make_trade_decision(self, short_window=5, long_window=10):
        if not self.active:
            print(f"{self.name} please activate the Bot")
            return

        if self.strategy == "moving_average_crossover":
            short_avg = self.calculate_moving_average(short_window)
            long_avg = self.calculate_moving_average(long_window)

            if short_avg is None or long_avg is None:
                print("Insufficient data to make a decision.")
                return "hold"

            if short_avg > long_avg:
                decision = "buy"
            elif short_avg < long_avg:
                decision = "sell"
            else:
                decision = "hold"

            print(f"{self.name} decision: {decision}")
            return decision
        else:
            print("Unsupported strategy.")
            return "hold"
