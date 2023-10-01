from bs4 import BeautifulSoup
import requests


def free_proxies():
    response = requests.get("https://free-proxy-list.net/")
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("div", attrs={"class": "fpl-list"})
    proxy_rows = table.find_all("tr")

    proxies = []

    for row in proxy_rows:
        proxy_data = [col.text for col in row.find_all("td")]

        if len(proxy_data) == 0:
            continue

        proxy = {
            "ip": proxy_data[0],
            "port": proxy_data[1],
            "code": proxy_data[2],
            "country": proxy_data[3],
            "anonymity": proxy_data[4],
            "google": proxy_data[5],
            "https": proxy_data[6],
        }

        proxies.append(proxy)

    return proxies