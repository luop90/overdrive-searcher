from pyquery import PyQuery as pq
from lxml import etree
import urllib

# Load settings
try:
	settings = pq(filename="userdata/libraries.xml")
except Exception as e:
	print("No libraries found. Please run add_library.py first")
	print e

while True:
	query = raw_input("Search for: ")

	for library in settings("library"):
		print("Searching library", library.name)
		result = pq(url=library.url)
