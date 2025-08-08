import requests
from bs4 import BeautifulSoup

def fetch_bbc_headlines():
    url = "https://www.bbc.co.uk/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    for h3 in soup.find_all("h3"):
        text = h3.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines[:10]  # Return top 10
