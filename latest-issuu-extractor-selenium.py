import sys
import re
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Extracts the latest issue's URL and cover image from the specified ISSUU user page using Selenium WebDriver.

# 1 argument: a valid ISSUU username
if len(sys.argv) == 2:

	# Check that the ISSUU username entered as an argument is valid
	usernamePattern = "^[a-z0-9\_\.\-]+$"
	usernameIsRightLength = (len(sys.argv[1]) >= 4) and (len(sys.argv[1]) <= 30)

	if not (usernameIsRightLength and re.match(usernamePattern, sys.argv[1])):
		print('A valid username has between 4 and 30 of only these characters: a-z 0-9 _ . -')
		exit()


	url = 'https://issuu.com/' + sys.argv[1]

	with closing(Firefox()) as browser:
		browser.get(url)
		source = browser.page_source
		try:
			WebDriverWait(browser, timeout=10).until(
				# The page is dynamically loaded
				lambda x: source != x.page_source)
			source = browser.page_source
		except:
			# The page is static
			source = browser.page_source

	soup = BeautifulSoup(source, 'html.parser')


	# Check if the page exists
	pageNotFound = soup.find('title').get_text() == 'ISSUU - Page not found'

	if pageNotFound:
		print('Sorry, it looks like the page you\'ve requested doesn\'t exist!')
		exit()


	# Check if the page is an ISSUU account's page
	if not soup.find('meta', {'property': 'og:profile:username'}):
		print('Sorry, it looks like the page you\'ve requested isn\'t an ISSUU account\'s page!')
		exit()


	allIssues = soup.findAll('a', {'class': 'cover'})

	# Check if there are any issues at all on this ISSUU account's page
	if not allIssues:
		print('Sorry, it looks like this ISSUU page doesn\'t have any issues at all!')
		exit()

	else:
		latestIssue = allIssues[0]


	issueUrl = 'https://issuu.com' + latestIssue.get('href')
	print(issueUrl)

	coverImage = latestIssue.find('img').get('src')
	print(coverImage)

else:

	print('Usage: python latest-issuu-extractor.py url\n')
	print('Please input only the username of the ISSUU account whose latest issue you wish to extract.\n')
	print('e.g. python latest-issuu-extractor.py YourIssuuNameHere')