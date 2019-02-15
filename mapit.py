import webbrowser, sys

if len(sys.argv) > 1:
	#Get address from command Line
	address = ' '.join(sys.argv[1:])
else:
	print("No arguments specified")

webbrowser.open('https://www.google.co.in/maps/place/' +address)
