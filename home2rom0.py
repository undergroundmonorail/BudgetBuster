#!/usr/bin/env python3

import re
import sys
import os

def get_includes(code):
	return re.findall(r'INCLUDE\s+"(.+\.z80)"', code, flags=re.IGNORECASE)

def fix_section_name(filename): 
	with open(filename, 'r+') as f:
		fixed, n = re.subn(r'(SECTION\s+".+",\s+)HOME', r'\1ROM0', f.read(), flags=re.IGNORECASE)
		if n: # don't touch unchanged files
			f.seek(0)
			f.write(fixed)
		return n

def main(args):
	with open(args[0]) as code:
		filenames = get_includes(code.read())
	subs = sum((fix_section_name(file) for file in filenames))
	if subs:
		print("Fixed {} deprecated section name{}.".format(subs, '' if subs == 1 else 's'))


if __name__ == "__main__":
	args = sys.argv[1:]
	if not args:
		sys.exit("Usage: {} main_game_file.z80".format(os.path.basename('./' + __file__)))
	main(args)