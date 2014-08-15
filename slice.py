#!/usr/bin/env python
#
# slice.py
# ========
#
# This utility spits out slice of a given file.
#
# Usage:
# python slice.py <filename> <offset_start> <offset_end>
#
# NOTE: Using range <0;2> means slicing bytes 0-1-2. ;)

import os
import sys

def main():
	fd = open(FILENAME, "r+b")

	data = fd.read()
	data = data[OFFSET_START:OFFSET_END] # isn't convenient? :D
	sys.stdout.write(data) # we want RAW data that we can redirect/pipe
	
	fd.close()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print sys.argv[0] + " <filename> <offset_start> <offset_end>"
		sys.exit(1)
	elif len(sys.argv) == 3:
		FILENAME = sys.argv[1]
		OFFSET_START = int(sys.argv[2])
		OFFSET_END = -1	
	else:
		FILENAME = sys.argv[1]
		OFFSET_START = int(sys.argv[2])
		OFFSET_END = int(sys.argv[3]) + 1

	# If <offset_end> arg is empty, slicing is done until EOF
	if OFFSET_END == -1:
		OFFSET_END = os.path.getsize(FILENAME)

	main()

