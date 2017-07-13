print("Ctrl+C at any time to finish\n\n")

try:
	f = open("userdata/libraries.txt", 'r')
except Exception as e:
	print ("No libraries.txt found, creating...")
	f = open("userdata/libraries.txt", 'w')

while True:
	f = open("userdata/libraries.txt", 'a')
	name = raw_input("Enter library name: ")
	f.write(name + "\n")

	print("Added " + name + " to libraries.txt")
