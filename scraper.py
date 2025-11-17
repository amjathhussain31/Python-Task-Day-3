import requests
from bs4 import BeautifulSoup

# 1. Fetch HTML from website
def fetch_html(url):
    headers = {"User-Agent": "NewsScraper/1.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

# 2. Extract headlines from <h1>, <h2>, <h3>
def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

# 3. Save headlines to a text file
def save_to_file(headlines):
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")

# 4. Main
if __name__ == "__main__":
    url = "https://www.bbc.com/news"   # you can change this site
    html = fetch_html(url)
    headlines = extract_headlines(html)
    save_to_file(headlines)
    print("Scraping completed! Check headlines.txt")
