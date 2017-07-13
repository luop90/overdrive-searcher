from pyquery import PyQuery as pq
import urllib
import re
import webbrowser

# Load libraries
try:
	libraries = open("userdata/libraries.txt", "r")
except Exception as e:
	print "No libraries found. Please run add_library.py first"
	print e

while True:
	# Grab query, then escape it
	query = raw_input("Search for: ")
	query = urllib.quote_plus(query)

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

		if int(regex.group(1)) >= 1:
			availableIn.append(library)

	print "Found " + urllib.unquote_plus(query).decode('utf-8') + " in ", foundIn
	print "Available in ", availableIn

	openBrowser = raw_input("Open in browser? [y/n]: ")
	if openBrowser is 'y':
		if len(availableIn) > 0:
			webbrowser.open("https://" + availableIn[0] + ".overdrive.com/search?query=" + query + "&format=audiobook-mp3&sortBy=relevance")
		elif len(foundIn) > 0:
			webbrowser.open("https://" + foundIn[0] + ".overdrive.com/search?query=" + query + "&format=audiobook-mp3&sortBy=relevance")
