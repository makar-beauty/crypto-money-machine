for item in data.get("result", {}).get("list", []):
    symbol = item.get("symbol", "")

    if not symbol.endswith("USDT"):
        continue

    try:
        markets[symbol] = {
            "price": float(item["lastPrice"]),
            "funding": float(item.get("fundingRate") or 0),
            "volume": float(item.get("turnover24h") or 0),
            "open_interest": float(item.get("openInterest") or 0),
        }
    except (KeyError, ValueError):
        continue

return markets
