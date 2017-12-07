import sys
import re
import requests
from bs4 import BeautifulSoup

# Extracts the latest issue's URL and cover image from the specified ISSUU user page's RSS feed.

# 1 argument: a valid ISSUU username
if len(sys.argv) == 2:

	# Check that the ISSUU username entered as an argument is valid
	usernamePattern = "^[a-z0-9\_\.\-]+$"
	usernameIsRightLength = (len(sys.argv[1]) >= 4) and (len(sys.argv[1]) <= 30)

	if not (usernameIsRightLength and re.match(usernamePattern, sys.argv[1])):
		print('A valid username has between 4 and 30 of only these characters: a-z 0-9 _ . -')
		exit()

	url = 'http://search.issuu.com/' + sys.argv[1] + '/docs/recent.rss'

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'xml')


	# Check if the page exists
	if not soup.find('rss'):
		print('Sorry, it looks like the page you\'ve requested doesn\'t exist!')
		exit()

	
	allIssues = soup.findAll('item')
	
	# Check if there are any issues at all on this ISSUU account's page
	if not allIssues:
		print('Sorry, it looks like this ISSUU page doesn\'t have any issues at all!')
		exit()

	else:
		latestIssue = allIssues[0]


	issueUrl = latestIssue.find('link').get_text()
	print(issueUrl)

	coverImage = latestIssue.find('media:content').get('url')
	print(coverImage)

else:

	print('Usage: python latest-issuu-extractor-rss.py url\n')
	print('Please input only the username of the ISSUU account whose latest issue you wish to extract.\n')
	print('e.g. python latest-issuu-extractor-rss.py YourIssuuNameHere')