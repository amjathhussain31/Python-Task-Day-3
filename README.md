# 📰 News Headlines Web Scraper
A simple Python project that scrapes top news headlines from any public news website and saves them into a `headlines.txt` file.  
This project uses **requests** and **BeautifulSoup** for web scraping.

---

## 📌 Objective
- Fetch HTML content from a public news website  
- Extract top headlines from `<h1>`, `<h2>`, and `<h3>` tags  
- Save the extracted headlines into a `.txt` file  
- Learn basic web scraping using Python

---

## 🛠️ Tools & Libraries Used
- Python  
- requests  
- BeautifulSoup (bs4)  
- VS Code (optional)

Install dependencies:
```bash
pip install requests beautifulsoup4
📂 Project Structure
bash
Copy code
news_scraper/
│
├── scraper.py        # Main scraper script
└── headlines.txt     # Output file (created automatically)
▶️ How to Run the Project
1. Clone or download this repository
bash
Copy code
git clone https://github.com/your-username/news-scraper.git
cd news-scraper
2. Install required packages
bash
Copy code
pip install requests beautifulsoup4
3. Run the script
bash
Copy code
python scraper.py
4. Check the output
A new file named headlines.txt will be created containing all the scraped headlines.

