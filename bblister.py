#
# Basic Block Lister (IDAPython)
# Andrzej Dyjak <dyjakan@sigsegv.pl>
#
# List addresses of all functions along with their BB.
#

from idaapi import *

def main():
	print "=== Basic Block Lister ==="
	print "[+] Processing..."

	ea = get_screen_ea()
	if ea == idaapi.BADADDR:
		print("[-] Error: get_screen_ea()")
		return

	seg = getseg(ea)

	if VERBOSE == 0:
		output = GetInputFile().replace(".", "_") + "-bb-list.txt"
		fd = open(output, "w+b")

	print "[+] Loaded at 0x%x" % (get_imagebase(ea))

	func = get_func(seg.startEA)
	seg_end = seg.endEA
	while func is not None and func.startEA < seg_end:
		funcea = func.startEA
		if VERBOSE == 1:
			print "Function %s at 0x%x" % (GetFunctionName(funcea), funcea)
		else:
			out = "Function %s at 0x%x\n" % (GetFunctionName(funcea), funcea)
			fd.write(out)

		bb = FlowChart(get_func(funcea))
		for block in bb:
			if VERBOSE == 1:
				# block.startEA-get_imagebase(ea) to get only offset from base
				print "[#%d]\t0x%x" % (block.id, block.startEA)
			else:
				out = "[#%d]\t%x\n" % (block.id, block.startEA)
				fd.write(out)

		func = get_next_func(funcea)

	if VERBOSE == 0:
		fd.close()

	return

if __name__=='__main__':
	VERBOSE = 0
	main()
	print "[+] Great success!"
