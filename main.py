from TraidingBot import TradingBot

if __name__ == "__main__":
    bot = TradingBot(name="AdvancedBot", strategy="moving_average_crossover")
    bot.activate()

    historical_prices = [100, 110, 105, 110, 120, 150, 160, 155, 180, 190]
    for price in historical_prices:
        bot.record_price(price)

    bot.make_trade_decision()

    bot.deactivate()

