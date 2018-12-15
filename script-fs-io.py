# This program demonstrate how to run a python script and pass any input data
# (arguments) using file system and get the result back as well.

# It should be invoked like this:
#	python script-fs-io.py /path/to/input-file /path/to/output-file

import sys

# Wait for user to press Enter key
def wait_for_enter():
	a = input("Press Enter to continue...")

# Greet the given name
def say_hello(name):
	print("Hello dear " + name)

# Greet the given name, nothing printed result returned
def get_say_hello(name):
        return "Hello dear " + name

# Write content to given filename
def write_data(filename, content):
        outfile = filename
        fout = open(outfile, "w")
        fout.write(content)
        fout.close()

# Program entry
def main():
	# For debugging ...
	#print(sys.argv)
	#print(len(sys.argv))
	#print(sys.argv[0])

	# Program must not continue unless there are three arguments
	if len(sys.argv) != 3:
		print("Invalid arguments")
		exit()
	
	# First argument is the python script (current file)
	# Second argument is input data file path
	print("Arguments file: " + sys.argv[1])

	# Open the input file and read its content (stripping whitespace chars)
	fin = open(sys.argv[1], "r")
	text = fin.readlines()
	theName = text[0].strip()


	# Write the outfile data to output file path
	write_data(sys.argv[2], get_say_hello(theName))
	#wait_for_enter()

main()
