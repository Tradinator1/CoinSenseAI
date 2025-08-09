def analyze_market():
    return "📈 Market Summary:\n\nThe market is currently experiencing mixed signals with varying risk appetites among investors."


def analyze_trends(prices):
    trends = {}
    for symbol, price in prices.items():
        if price > 1000:
            trends[symbol] = "Bearish"
        elif price > 100:
            trends[symbol] = "Sideways"
        else:
            trends[symbol] = "Bullish"
    return trends
