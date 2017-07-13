from pyquery import PyQuery as pq
from lxml import etree
import urllib

# Load libraries
try:
	libraries = open("userdata/libraries.txt")
except Exception as e:
	print("No libraries found. Please run add_library.py first")
	print e

while True:
	# Grab query, then escape it
	query = raw_input("Search for: ")

	for library in libraries:
		print("Searching library", library)
		result = pq(url="https://{library}.overdrive.com/search?query={query}")
