from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}
test = "https://www.google.com/search?channel=fenc&client=firefox-b-1-d&q=After+Dark+Mr.+Kitty#cobssid=s"

payload = {
    "action": "query",
    "format": "json",
    "prop": "revisions",
    "titles": "cowboys_from_hell",
    "formatversion": "2",
    "rvprop": "content",
    "rvslots": "*",
}

results = requests.get(test, headers=headers)

soup = BeautifulSoup(
    results.content, "html5lib", from_encoding="utf-8"
)  # If this line causes an error, run 'pip install html5lib' or install html5lib

table = soup.find("table", attrs={"class": "infobox vevent haudio"})
keys = [x.text for x in table.find_all("th", attrs={"class": "infobox-label"})]
values = [x.text for x in table.find_all("td", attrs={"class": "infobox-data"})]
result = dict(zip(keys, values))

for x, y in result.items():
    print(x, y)

# print(result["Label"])
# print(result["Producer"])
