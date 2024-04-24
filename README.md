Advanced Crypto Trading Bot

Overview:
 This Python application implements a trading bot with an advanced trading strategy based on moving average crossover.<br />
The bot calculates short-term and long-term moving averages of cryptocurrency prices to make buy, sell, or hold decisions.<br />

Run the main.py file using Python to demonstrate the bot's functionality.

Functionality:

TradingBot class:<br />
The TradingBot class manages the bot's status, historical price data, and trade decisions based on different strategies.

Attributes:<br />
name: Name of the trading bot.<br />
active: Boolean indicating if the bot is active or not.<br />
strategy: Placeholder for the bot's trading strategy.<br />
prices: List to store historical prices of the cryptocurrency.

Methods:
activate(): Activates the bot.
deactivate(): Deactivates the bot.
record_price(price): Records the current price of the cryptocurrency.
calculate_moving_average(window_size): Calculates the moving average of historical prices.
make_trade_decision(short_window=5, long_window=10): Makes a trade decision based on the moving average crossover strategy.

Example Usage:
Instantiate the bot with the desired parameters and strategy.
Activate the bot.
Record historical prices using the record_price() method.
Make trade decisions using the make_trade_decision() method.
Deactivate the bot when not in use.
