from bs4 import BeautifulSoup
import requests

area_code = ["hb", "db", "hd", "hz", "hn", "xb", "xn"]

url_prefix = "http://weather.com.cn/textFC/"


def url_generate(code):
    return url_prefix + code + ".shtml"


def parse_row(row):
    city = row[0].a.text
    status = row[1].text
    wind_direction = row[2].select("span")[0].text
    wind_level = row[2].select("span")[1].text
    max_temperature = row[3].text + "度"
    min_temperature = row[-2].text + "度"
    return f"{city} {status} {wind_direction} {wind_level} 最高气温:{max_temperature} 最低气温:{min_temperature}"


def otto():
    with open("forecast.txt", "w", encoding="utf-8") as f:
        for code in area_code:
            req = requests.get(url_generate(code))
            content = req.content.decode("utf-8")
            soup = BeautifulSoup(content, "lxml")
            for a in soup.select(".hanml > div:nth-of-type(2) > .conMidtab2"):
                for t in a.select("tr")[2:]:
                    if len(t) == 19:
                        f.write(parse_row(t.select("td")[1:]) + "\n")
                    else:
                        f.write(parse_row(t.select("td")) + "\n")


otto()
