# Latest ISSUU Extractor

Extracts the URL and cover image of the latest issue from any [ISSUU](https://issuu.com/) account's page.

Currently only prints the links to console.

## Usage

Install Python.

Install the required packages:

````
pip install selenium
pip install BeautifulSoup4
````

Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases), and add it to PATH.

Go to the directory where `latest-issuu-extractor.py` is located.

Run:

````
python ubyssey-latest-issuu-extractor.py YourIssuuNameHere
````

The argument (which I've denoted with 'YourIssuuNameHere') should be the username of the ISSUU account whose latest issue you wish to extract.