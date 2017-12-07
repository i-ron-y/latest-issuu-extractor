# Latest ISSUU Extractor

Extracts the URL and cover image of the latest issue from any [ISSUU](https://issuu.com/) account's page.

Currently only prints the links to console.

Two versions:
- `latest-issuu-extractor-selenium.py` uses Selenium WebDriver to extract the latest issue's URL and cover image from the specified ISSUU user page.
- `latest-issuu-extractor-rss.py` extracts the latest issue's URL and cover image from the ISSUU user page's RSS feed without having to use Selenium WebDriver.

## Usage

Install Python.

**For latest-issuu-extractor-selenium.py:**

Install the required packages:

````
pip install selenium
pip install BeautifulSoup4
````

Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases), and add it to PATH.

Go to the directory where `latest-issuu-extractor-selenium.py` is located.

Run:

````
python latest-issuu-extractor-selenium.py YourIssuuNameHere
````

**For latest-issuu-extractor-rss.py:**

Install the required packages:

````
pip install requests
pip install BeautifulSoup4
pip install lxml
````

Go to the directory where `latest-issuu-extractor-rss.py` is located.

Run:

````
python latest-issuu-extractor-rss.py YourIssuuNameHere
````
