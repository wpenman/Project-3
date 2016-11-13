# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import re
import requests 
from bs4 import BeautifulSoup


fopen = open('index.html', 'w')
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
a = requests.get(base_url)
bs = BeautifulSoup(a.text, 'lxml')

for word in bs.find_all(text=re.compile('student')):
	new = word.replace('student', 'AMAZING student')
	word.replace_with(new)

for img in bs.find_all('img'):
	if img['src'] == 'logo2.png':
	    img['src'] = 'media/logo.png'
	else:
	    img['src'] = 'media/hw3photo.jpg' 

updated = bs.prettify()
fopen.write(updated)