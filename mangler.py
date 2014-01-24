#  mangler.py
#  =========
#
#  This utility applies user defined function mangle() for given byte range
#  inside given file. (Comes in handy *way* too often.)
#
#  Usage:
#  python mangler.py <filename> <offset_start> <offset_end>
#
#  NOTE: Using range <0;2> means mangling bytes 0-1-2. ;)
#

import os
import sys
import mmap

# Basic inefficient example that XOR-es given byte range with 0x20
def mangle(fd, start, end):
   mapped = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_WRITE)
   mapped.seek(start)
   XOR = 0x20
   while(start < end):
      mapped[start] = chr(ord(mapped[start]) ^ XOR)
      start += 1

   mapped.close()


if len(sys.argv) < 3:
   print sys.argv[0] + " <filename> <offset_start> <offset_end>"
   sys.exit(1)

if len(sys.argv) == 3:
   FILENAME = sys.argv[1]
   OFFSET_START = int(sys.argv[2])
   OFFSET_END = -1

if len(sys.argv) >= 4:
   FILENAME = sys.argv[1]
   OFFSET_START = int(sys.argv[2])
   OFFSET_END = int(sys.argv[3]) + 1

fd = open(FILENAME, "r+b")

# If <offset_end> arg is empty, mangle() is used until EOF
if OFFSET_END == -1:
   OFFSET_END = os.path.getsize(FILENAME)

mangle(fd, OFFSET_START, OFFSET_END)

fd.close()

