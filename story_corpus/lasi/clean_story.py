from bs4 import BeautifulSoup as BS
def clean_story(file_name):

	print('Processing story ' + file_name)
	# extract the basic data out of html flags
	with open(file_name) as f:
		soup = BS(''.join(f.readlines()), 'html.parser')

	title = ''
	story = ''

	number_of_skips = 1

	for h1 in soup.find_all('h1'):
		title += h1.text

	title += ' '

	for h3 in soup.find_all('h3'):
		title += h3.text

	for par in soup.find_all('p'):
		if number_of_skips > 0:
			number_of_skips -= 1
		else:
			story += par.text


	return title, story