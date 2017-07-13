from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re

# Load libraries
try:
	libraries = open("userdata/libraries.txt", "r")
except Exception as e:
	print "No libraries found. Please run add_library.py first"
	print e

while True:
	# Grab query, then escape it
	query = raw_input("Search for: ")
	print query
	query = urllib.quote_plus(query)
	print query

	foundIn = []
	availableIn = []

	# Resets the "libraries" for-loop
	libraries = open("userdata/libraries.txt", "r")

	for library in libraries:
		# Remove \n
		library = library[:-1]

		print "Searching library", library
		result = pq(url="https://" + library + ".overdrive.com/search?query=" + query + "&format=audiobook-mp3&sortBy=relevance")

		if result("h1#noresults"):
			continue
		else:
			foundIn.append(library)

		# Keep track of where it's available
		# Yes, I'm really going to Regex my way through a script tag
		# Cause its simpler than anything else I can think of
		regex = re.search(r'\"availableCopies\"\:(\d)', result("script:eq(0)").text())
		if regex and regex.group(1) > 0:
			availableIn.append(library)

	print "Found " + urllib.unquote_plus(query).decode('utf-8') + " in ", foundIn
	print "Available in ", availableIn
