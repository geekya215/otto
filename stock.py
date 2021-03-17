import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}


def generate_url(page):
    return f"https://xueqiu.com/service/v5/stock/screener/quote/list?page={page}&size=90&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1615999061810"


with open("stock.txt", "w", encoding="utf-8") as f:
    for page in range(1, 45):
        stocks = requests.get(generate_url(page), headers=headers).json()["data"]["list"]
        for s in stocks:
            symbol = s["symbol"]
            name = s["name"]
            current = str(s["current"])
            chg = "+" + str(s["chg"])
            percent = "+" + str(s["percent"]) + "%"
            market_capital = str(round(s["market_capital"] / pow(10, 8), 2)) + "亿"
            f.write("{0}\n".format(" ".join([symbol, name, current, chg, percent, market_capital])))
