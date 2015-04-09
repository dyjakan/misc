#
# addr2offset.py (IDAPython)
# Andrzej Dyjak <dyjakan@sigsegv.pl>
#
# Because rebasing all-teh-time is tiring.
#

from idaapi import *

def main():

	ea = get_screen_ea()
	if ea == idaapi.BADADDR:
		print("[-] Error: get_screen_ea()")
		return

	if DEBUG:
		print "[+] Base address at 0x%x" % (get_imagebase(ea)) # Base Address
		print "[+] Current function at: 0x%x" % (ea) # Current cursor address

	# This isn't perfect solution; is there a way to get an original file name
	# instead of the name of IDA database?
	fname = (idaapi.cvar.database_idb)
	fname = fname.split('\\')
	fname = fname[-1]
	fname = fname.strip(".idb")
	fname = fname.strip(".i64")

	print "WinDBG: bp %s+0x%x" % (fname, ea-get_imagebase(ea))

	return

if __name__=='__main__':
	DEBUG = 0

	CompileLine('static shift_b() { RunPythonStatement("main()"); }')
	AddHotkey("Shift-B", 'shift_b')

	print "[+] addr2offset successfuly loaded"
	print "Use Shift-B to get breakpoint with an offset"