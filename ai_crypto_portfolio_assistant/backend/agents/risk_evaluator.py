from backend.services.coingecko import get_current_prices as get_prices

class RiskEvaluatorAgent:
    def evaluate(self, portfolio, prices):
        result = ""
        for coin, amount in portfolio.items():
            price = prices.get(coin.lower(), {}).get("usd", 0)
            risk = self._classify_risk(price)
            result += f"- {coin.upper()}: {risk} (${price:.2f})\n"
        return result

    def get_risk_tier(self, coin, price_data):
        price = price_data.get(coin.lower(), {}).get("usd", 0)
        return self._classify_risk(price, return_tier=True)

    def _classify_risk(self, price, return_tier=False):
        if price > 50000:
            return "🟢 Very Low Risk" if not return_tier else "very_low"
        elif price > 1000:
            return "🟢 Low Risk" if not return_tier else "low"
        elif price > 100:
            return "🟠 Medium Risk" if not return_tier else "medium"
        elif price > 1:
            return "🔴 Mid-High Risk" if not return_tier else "mid_high"
        else:
            return "🔴 High Risk" if not return_tier else "high"
