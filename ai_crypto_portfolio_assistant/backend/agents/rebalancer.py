from backend.services.coingecko import get_current_prices as get_price
from backend.agents.risk_evaluator import RiskEvaluatorAgent
from backend.agents.market_analyst import MarketAnalystAgent

def suggest_rebalance(portfolio, risk_data, trend_data, prices):
    total_usd = sum(asset['usd'] for asset in portfolio.values())

    tier_weights = {
        "Very Low Risk": 1.0,
        "Low Risk": 1.0,
        "Medium Risk": 0.8,
        "Mid-High Risk": 0.6,
        "High Risk": 0.5
    }

    weighted_assets = []
    for symbol, asset in portfolio.items():
        risk = risk_data.get(symbol, {}).get("tier", "Medium Risk")
        trend = trend_data.get(symbol, "Sideways")
        price = prices.get(symbol, 0)

        base_weight = tier_weights.get(risk, 0.8)
        if trend == "Bullish":
            base_weight += 0.1
        elif trend == "Bearish":
            base_weight -= 0.1

        base_weight = max(0, base_weight)
        weighted_assets.append((symbol, base_weight))  # Make sure this is only 2 elements

    # ✅ This will now work without unpack error
    total_weight = sum(weight for _, weight in weighted_assets)

    if total_weight == 0:
        return {}

    target_distribution = {
        symbol: (weight / total_weight) * total_usd
        for symbol, weight in weighted_assets
    }

    rebalance_plan = {}

    for symbol, target_usd in target_distribution.items():
        current_usd = portfolio[symbol]["usd"]
        current_qty = portfolio[symbol]["qty"]
        price = prices.get(symbol, 0)
        if price == 0:
            continue

        target_qty = target_usd / price
        difference = round(target_qty - current_qty, 6)
        action = "✅ Already balanced."

        if abs(difference) > 0.00001:
            action = f"➡️ {'Buy' if difference > 0 else 'Sell'} {abs(difference):.4f} {symbol} to reach ${target_usd:.2f} target."

        rebalance_plan[symbol] = {
            "current_qty": current_qty,
            "current_usd": current_usd,
            "target_qty": target_qty,
            "target_usd": target_usd,
            "action": action
        }

    return rebalance_plan


def suggest_additional_assets(portfolio, risk_data, trend_data, prices):
    tier_counts = {
        "Very Low Risk": 0,
        "Low Risk": 0,
        "Medium Risk": 0,
        "Mid-High Risk": 0,
        "High Risk": 0
    }

    for data in risk_data.values():
        tier = data.get("tier", "Medium Risk")
        if tier in tier_counts:
            tier_counts[tier] += 1

    # pick the least present tier (to balance portfolio)
    most_needed_tier = min(tier_counts, key=tier_counts.get)

    analyst = MarketAnalystAgent(prices)
    all_risks = RiskEvaluatorAgent().evaluate(prices)
    all_trends = analyst.analyze_trends(prices)

    recommended = []
    for symbol, data in all_risks.items():
        if symbol in portfolio:
            continue
        if data["tier"] == most_needed_tier and all_trends.get(symbol) == "Bullish":
            recommended.append(symbol)

    return recommended[:3]


def suggest_reallocation(portfolio):
    # Placeholder for future intelligent reallocation logic
    return {}
